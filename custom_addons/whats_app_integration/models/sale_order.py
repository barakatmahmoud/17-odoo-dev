from odoo import models, fields, _
from odoo.exceptions import ValidationError, UserError
import os
import re
import requests

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        self.send_sold_whatsapp()
        return res

    def send_sold_whatsapp(self):
        self.ensure_one()

        # 1. Get the owner's phone number
        phone = self.partner_id.phone if self.partner_id else False

        if not phone:
            raise UserError(
                _("Please enter a phone number for the property owner.")
            )

        # 2. Normalize the phone number
        phone = re.sub(r'[\s()+-]', '', phone)

        if not phone.isdigit():
            raise UserError(
                _("The owner's WhatsApp number is invalid.")
            )

        # 3. Read WhatsApp configuration
        access_token = os.getenv('WHATSAPP_ACCESS_TOKEN')
        phone_number_id = os.getenv('WHATSAPP_PHONE_NUMBER_ID')
        api_version = os.getenv('WHATSAPP_API_VERSION')

        if not all([access_token, phone_number_id, api_version]):
            raise UserError(
                _("WhatsApp API configuration is incomplete.")
            )

        # 4. Build the API endpoint
        url = (
            f"https://graph.facebook.com/"
            f"{api_version}/{phone_number_id}/messages"
        )

        # 5. Prepare the test message
        payload = {
            "messaging_product": "whatsapp",
            "to": phone,
            "type": "template",
            "template": {
                "name": "hello_world",
                "language": {
                    "code": "en_US"
                }
            }
        }

        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        }

        # 6. Send the request to WhatsApp
        try:
            response = requests.post(
                url,
                headers=headers,
                json=payload,
                timeout=20,
            )
            result = response.json()

        except requests.RequestException:
            raise UserError(
                _("Could not connect to WhatsApp. Please try again.")
            )

        except ValueError:
            raise UserError(
                _("WhatsApp returned an invalid response.")
            )

        # 7. Handle API errors
        if not response.ok or result.get('error'):
            error = result.get('error', {})
            message = error.get('message') or _(
                "Unknown WhatsApp API error."
            )
            raise UserError(
                _("WhatsApp sending failed: %s") % message
            )

        # 8. Show confirmation in Odoo
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': _('WhatsApp'),
                'message': _(
                    'WhatsApp accepted the message for sending.'
                ),
                'type': 'success',
                'sticky': False,
            },
        }