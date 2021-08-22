from django.contrib.auth.base_user import BaseUserManager
from .moodle import MoodleAuth


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, user_id, email, password, **extra_fields):
        if not email or not user_id:
            raise ValueError('Не передан ID или Email')
        email = self.normalize_email(email)
        moodle = MoodleAuth(email, password)
        moodle_data = moodle.check_account()
        if 'error_message' in moodle_data:
            raise ValueError(moodle_data['error_message'])
        extra_fields.update(moodle_data)

        user = self.model(user_id=user_id, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, user_id, email, password=None, **extra_fields):
        extra_fields.setdefault('is_admin', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(user_id, email, password, **extra_fields)

    def create_superuser(self, user_id, email, password, **extra_fields):
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_admin') is not True:
            raise ValueError('Суперпользователь должен иметь права администратора')

        return self._create_user(user_id, email, password, **extra_fields)
