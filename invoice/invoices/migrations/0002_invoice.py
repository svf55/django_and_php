import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('invoices', '0001_create_superuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(db_index=True, max_length=256, unique=True, verbose_name='Номер')),
                ('orders', django.contrib.postgres.fields.jsonb.JSONField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Создана')),
            ],
            options={
                'verbose_name': 'Накладная',
                'verbose_name_plural': 'Накладные',
            },
        ),
    ]
