# Generated by Django 2.2.16 on 2020-09-17 10:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('permissions', '0002_auto_20200221_2126'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('environments', '0014_auto_20200917_1032'),
        ('users', '0027_ffadminuser_github_user_id'),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.CreateModel(
                    name='EnvironmentPermissionModel',
                    fields=[
                    ],
                    options={
                        'proxy': True,
                        'indexes': [],
                        'constraints': [],
                    },
                    bases=('permissions.permissionmodel',),
                ),
                migrations.CreateModel(
                    name='UserPermissionGroupEnvironmentPermission',
                    fields=[
                        ('id', models.AutoField(auto_created=True, primary_key=True,
                                                serialize=False, verbose_name='ID')),
                        ('admin', models.BooleanField(default=False)),
                        ('environment',
                         models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                           related_query_name='grouppermission',
                                           to='environments.Environment')),
                        ('group',
                         models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                           to='users.UserPermissionGroup')),
                        ('permissions', models.ManyToManyField(blank=True,
                                                               to='permissions.PermissionModel')),
                    ],
                    options={
                        'db_table': 'environments_userpermissiongroupenvironmentpermission',
                    },
                ),
                migrations.CreateModel(
                    name='UserEnvironmentPermission',
                    fields=[
                        ('id', models.AutoField(auto_created=True, primary_key=True,
                                                serialize=False, verbose_name='ID')),
                        ('admin', models.BooleanField(default=False)),
                        ('environment',
                         models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                           related_query_name='userpermission',
                                           to='environments.Environment')),
                        ('permissions', models.ManyToManyField(blank=True,
                                                               to='permissions.PermissionModel')),
                        ('user',
                         models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                           to=settings.AUTH_USER_MODEL)),
                    ],
                    options={
                        'db_table': 'environments_userenvironmentpermission',
                    },
                ),
            ],
            database_operations=[]
        )
    ]
