# Generated by Django 2.1.7 on 2019-03-17 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_beat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drumming',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beat_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.Beat')),
                ('matron_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.Matron')),
            ],
        ),
        migrations.AddField(
            model_name='beat',
            name='drummed_by',
            field=models.ManyToManyField(related_name='beat_id', through='core.Drumming', to='core.Beat'),
        ),
        migrations.AddField(
            model_name='matron',
            name='drumming_with',
            field=models.ManyToManyField(related_name='matron_id', through='core.Drumming', to='core.Beat'),
        ),
    ]
