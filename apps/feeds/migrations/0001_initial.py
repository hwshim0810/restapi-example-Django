# Generated by Django 2.0.7 on 2018-08-02 01:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('content_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='feeds.Content')),
                ('path', models.CharField(max_length=200)),
                ('caption', models.TextField(blank=True, max_length=3000)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('feeds.content',),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('content_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='feeds.Content')),
                ('title', models.CharField(max_length=50)),
                ('text', models.TextField(max_length=3000)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('feeds.content',),
        ),
        migrations.AddField(
            model_name='content',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_feeds.content_set+', to='contenttypes.ContentType'),
        ),
    ]