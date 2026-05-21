/** @odoo-module **/

import publicWidget from "@web/legacy/js/public/public_widget";
import { rpc } from "@web/core/network/rpc";

publicWidget.registry.IDCardsChange = publicWidget.Widget.extend({
    selector: '.id_cards_form',
    events: {
        'change #country_id': '_onChangeCountry',
    },
    async _onChangeCountry(ev) {
        const countryId = ev.currentTarget.value;
        $('#city_id').empty();
        $('#city_id').append('<option value="">Select City</option>');

        if (!countryId){
             return;
        };
        
        const cities = await rpc('/get/cities', {country_id: countryId});

        if(cities.length > 0){
            $('#city_id').prop('required', true);
        }
        else{
             $('#city_id').prop('required', false);
        }

        cities.forEach(city => {
            $('#city_id').append(
                `<option value="${city.id}">${city.name}</option>`
            );
        });
    },
});