# encoding: utf8

from django.db import migrations


def load_data(apps, schema_editor):
    order = apps.get_model("orders", "Order")

    order(description='order 1', is_ready=True).save()
    order(description='order 2', is_ready=False).save()
    order(description='order 3', is_ready=True).save()
    order(description='order 4', is_ready=False).save()
    order(description='order 5', is_ready=True).save()


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_initial'),
    ]

    operations = [
        migrations.RunPython(load_data, reverse_code=lambda apps, schema_editor: None)
    ]

