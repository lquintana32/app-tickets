# Generated by Django 4.0.5 on 2022-06-06 07:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aplicacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('ticket_id', models.AutoField(primary_key=True, serialize=False)),
                ('timestamp', models.DateField(default=django.utils.timezone.now)),
                ('categoy', models.CharField(choices=[('rrhh', 'Recusos Humanos'), ('contabilidad', 'Contabilidad'), ('gerencia', 'Gerencia')], max_length=200)),
                ('content', models.TextField()),
                ('timeclosing', models.DateField(blank=True, null=True)),
                ('solution', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]