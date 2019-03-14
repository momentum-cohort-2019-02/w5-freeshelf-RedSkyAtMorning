# Generated by Django 2.1.7 on 2019-03-14 01:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_matron_userid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Resemblance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=1000, null=True)),
                ('order_by_help', models.PositiveSmallIntegerField(blank=True, null=True)),
            ],
            options={
                'ordering': ['order_by_help'],
            },
        ),
        migrations.AddField(
            model_name='bead',
            name='author',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='bead',
            name='citationURL',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bead',
            name='first_sponsor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.Matron'),
        ),
        migrations.AddField(
            model_name='bead',
            name='name_slug',
            field=models.SlugField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='matron',
            name='is_crone',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='matron',
            name='last_rating',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True),
        ),
        migrations.AddField(
            model_name='matron',
            name='last_rating_on',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='matron',
            name='linkedin',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='resemblance',
            name='bead_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.Bead'),
        ),
        migrations.AddField(
            model_name='resemblance',
            name='bowl_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.Bowl'),
        ),
        migrations.AddField(
            model_name='membership',
            name='bead_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.Bead'),
        ),
        migrations.AddField(
            model_name='membership',
            name='necklace_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.Necklace'),
        ),
        migrations.AddField(
            model_name='bead',
            name='collected_by',
            field=models.ManyToManyField(related_name='bead_id', through='core.Resemblance', to='core.Bowl'),
        ),
        migrations.AddField(
            model_name='bead',
            name='strung_with',
            field=models.ManyToManyField(related_name='bead_id', through='core.Membership', to='core.Necklace'),
        ),
        migrations.AddField(
            model_name='bowl',
            name='collecting',
            field=models.ManyToManyField(related_name='bowl_id', through='core.Resemblance', to='core.Bead'),
        ),
        migrations.AddField(
            model_name='necklace',
            name='stringing',
            field=models.ManyToManyField(related_name='necklace_id', through='core.Membership', to='core.Bead'),
        ),
    ]
