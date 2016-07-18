# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-18 13:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import share.models.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0018_auto_20160710_2132'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThroughAwardEntities',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('award', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='share.Award')),
                ('award_version', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='share.AwardVersion')),
                ('change', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='affected_throughawardentities', to='share.Change')),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='share.Entity')),
                ('entity_version', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='share.EntityVersion')),
                ('extra', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='share.ExtraData')),
                ('extra_version', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='share.ExtraDataVersion')),
                ('same_as', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.ThroughAwardEntities')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ThroughAwardEntitiesVersion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.TextField(max_length=10)),
                ('persistent_id', models.PositiveIntegerField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('award', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='share.Award')),
                ('award_version', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='share.AwardVersion')),
                ('change', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='affected_throughawardentitiesversion', to='share.Change')),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='share.Entity')),
                ('entity_version', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='share.EntityVersion')),
                ('extra', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='share.ExtraData')),
                ('extra_version', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='share.ExtraDataVersion')),
                ('same_as', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.ThroughAwardEntities')),
                ('same_as_version', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.ThroughAwardEntitiesVersion')),
                ('sources', models.ManyToManyField(related_name='source_throughawardentitiesversion', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'ordering': ('-date_modified',),
            },
        ),
        migrations.AddField(
            model_name='throughawardentities',
            name='same_as_version',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='share.ThroughAwardEntitiesVersion'),
        ),
        migrations.AddField(
            model_name='throughawardentities',
            name='sources',
            field=models.ManyToManyField(related_name='source_throughawardentities', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='throughawardentities',
            name='version',
            field=models.OneToOneField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='share_throughawardentities_version', to='share.ThroughAwardEntitiesVersion'),
        ),
        migrations.AddField(
            model_name='award',
            name='entitie_versions',
            field=share.models.fields.TypedManyToManyField(through='share.ThroughAwardEntities', to='share.EntityVersion'),
        ),
        migrations.AddField(
            model_name='award',
            name='entities',
            field=share.models.fields.TypedManyToManyField(through='share.ThroughAwardEntities', to='share.Entity'),
        ),
        migrations.AddField(
            model_name='awardversion',
            name='entitie_versions',
            field=share.models.fields.TypedManyToManyField(through='share.ThroughAwardEntities', to='share.EntityVersion'),
        ),
        migrations.AddField(
            model_name='awardversion',
            name='entities',
            field=share.models.fields.TypedManyToManyField(through='share.ThroughAwardEntities', to='share.Entity'),
        ),
    ]
