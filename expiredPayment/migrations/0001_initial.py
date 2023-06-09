# Generated by Django 4.2 on 2023-04-05 03:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpiredPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('penalty_fee_amount', models.FloatField(default=0.0)),
                ('payment_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_payment', to='payment.userpayment')),
            ],
            options={
                'db_table': 'ExpiredPayments',
            },
        ),
    ]
