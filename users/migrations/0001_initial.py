# Generated by Django 2.2 on 2020-09-07 22:36

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import users.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_producer', models.BooleanField(blank=True, default=False, null=True)),
                ('role', models.CharField(blank=True, choices=[('خریدار', 'خریدار'), ('فروشنده', 'فروشنده'), ('هر دو', 'هر دو')], max_length=12, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('خانم', 'خانم'), ('آقای', 'آقای')], max_length=17, verbose_name='جنسیت')),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='', verbose_name='تصویر پروفایل')),
                ('province', models.CharField(blank=True, max_length=132, null=True, verbose_name='استان')),
                ('city', models.CharField(blank=True, max_length=132, null=True, verbose_name='شهر')),
                ('company_name', models.CharField(blank=True, max_length=132, null=True, verbose_name='نام شرکت')),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True, validators=[users.validators.validate_phone_number])),
                ('company_address', models.TextField(blank=True, null=True, verbose_name='آدرس کارخانه یا شرکت')),
                ('office_address', models.TextField(blank=True, null=True, verbose_name='آدرس دفتر')),
                ('office_phone_num', models.CharField(blank=True, max_length=20, null=True, validators=[users.validators.validate_phone_number], verbose_name='شماره تلفن دفتر')),
                ('introduce_yourself', models.TextField(blank=True, null=True, verbose_name='معرفی مختصر شرکت')),
                ('description', models.TextField(blank=True, null=True, verbose_name='توضیحات')),
                ('date_created_at', models.DateTimeField(auto_now=True)),
                ('web_site', models.CharField(blank=True, max_length=120, null=True, verbose_name='آدرس وبسایت')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProducerProfile',
            fields=[
                ('profile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.Profile')),
                ('department', models.CharField(blank=True, max_length=132, null=True, verbose_name='دپارتمان')),
                ('job_title', models.CharField(blank=True, max_length=132, null=True, verbose_name='عنوان شغلی')),
                ('postal_code', models.CharField(blank=True, max_length=12, null=True, validators=[users.validators.validate_phone_number], verbose_name='کد پستی')),
                ('alternative_phone', models.CharField(blank=True, max_length=15, null=True, validators=[users.validators.validate_phone_number], verbose_name='شماره اضطراری')),
                ('fax_number', models.CharField(blank=True, max_length=20, null=True, validators=[users.validators.validate_phone_number], verbose_name='فکس')),
                ('business_type', models.CharField(blank=True, choices=[('تولید کننده', 'تولید کننده'), ('پخش کننده', 'پخش کننده'), ('وارد کننده', 'وارد کننده'), ('خدمات', 'خدمات'), ('عمده فروش', 'عمده فروش'), ('بنک دار', 'بنک دار'), ('دولتی', 'دولتی'), ('متفرقه', 'متفرقه')], max_length=20, null=True, verbose_name='زمینه کاری')),
                ('categoty', models.ManyToManyField(to='categories.Category')),
            ],
            bases=('users.profile',),
        ),
    ]
