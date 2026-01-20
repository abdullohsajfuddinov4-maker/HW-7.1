from rest_framework import serializers
from .models import CustomUser
from rest_framework.exceptions import ValidationError


class SignUpSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id','address', 'password')

    def validate_password(self, password):
        if password is None:
            raise ValidationError({
                'success': False,
                'message': 'Siz parol kiritmadingiz'
            })

        if len(password) < 7 or len(password) > 20:
            raise ValidationError({
                'success': False,
                'message': 'Parolingiz 7 tadan kam va 20 tadan ko‘p bo‘lmasligi kerak'
            })


        if password.isdigit() or password.isalpha():
            raise ValidationError({
                'success': False,
                'message': 'Parolda harflar va sonlar birga bo‘lishi shart'
            })


        special_chars = [c for c in password if not c.isdigit() and not c.isalpha()]
        if len(special_chars) == 0:
            raise ValidationError({
                'success': False,
                'message': 'Siz belgilar (!, @, # ...) dan ham foydalanishingiz kerak'
            })

        return password

    def validate_username(self, username):
        username = username.lower()

        if not 5 < len(username) < 10:
            raise ValidationError({
                'success': False,
                'message': 'Username uzunligi 6 va 9 orasida bo‘lishi kerak'
            })


        if ' ' in username:
            raise ValidationError({
                'success': False,
                'message': 'Username ichida probel bo‘lishi mumkin emas'
            })

        if not re.fullmatch(r'[a-z0-9_]+', username):
            raise ValidationError({
                'success': False,
                'message': 'Faqat harflar, raqamlar va "_" ruxsat etiladi'
            })

        if username[0].isdigit() or username[-1].isdigit():
            raise ValidationError({
                'success': False,
                'message': 'Username raqam bilan boshlanishi yoki tugashi mumkin emas'
            })

        if username.count('_') > 1:
            raise ValidationError({
                'success': False,
                'message': 'Faqat bitta "_" ishlatish mumkin'
            })

        if username.startswith('_') or username.endswith('_'):
            raise ValidationError({
                'success': False,
                'message': '"_" boshida yoki oxirida bo‘lishi mumkin emas'
            })

        return username

