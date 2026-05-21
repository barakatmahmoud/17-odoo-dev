// use Jquery to make validation
// $('#id_number').on('input', function () {
//     this.value = this.value.replace(/\D/g, '').slice(0, 14);
// });

// use public widget
/** @odoo-module **/

import publicWidget from "@web/legacy/js/public/public_widget";

publicWidget.registry.IDCardsValidation = publicWidget.Widget.extend({
    selector: '.id_cards_form',

    events: {
        'input #id_number': '_onIdNumberInput',
        'input #phone_number': '_onPhoneNumberInput',
        'submit': '_onSubmit',
    },

    _onIdNumberInput(ev) {
        ev.currentTarget.value = ev.currentTarget.value.replace(/\D/g, '').slice(0, 14);
    },
    _onPhoneNumberInput(ev){
        ev.currentTarget.value = ev.currentTarget.value.replace(/\D/g, '').slice(0, 11);
    },
    _onSubmit(ev){
        const idNumber = this.$('#id_number').val();
        const phoneNumber = this.$('#phone_number').val();
        const email = this.$('#email').val()
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

        if(idNumber.length !== 14){
            ev.preventDefault();
            alert('You Must Enter 14 Number in ID Number');
            return;
        }
        if(phoneNumber.length !== 11){
            ev.preventDefault();
            alert('You Must Enter 11 Number in ID Number');
            return;
        }
        if (!/^01/.test(phoneNumber)) {
            ev.preventDefault();
            alert('رقم الهاتف يجب أن يبدأ بـ 01');
            return;
        }
        if(!emailPattern.test(email)){
            ev.preventDefault();
            alert('من فضلك أدخل بريد إلكتروني صحيح');
            return;
        }
    }
});
