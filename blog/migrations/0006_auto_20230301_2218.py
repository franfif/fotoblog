# Generated by Django 4.1.7 on 2023-03-01 22:18

from django.db import migrations


def replace_author_with_contributor(apps, schema_editor):
    Blog = apps.get_model('blog', 'Blog')

    for blog in Blog.objects.all():
        blog.contributors.add(blog.author,
                              through_defaults={'contribution': 'Primary Author'})


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_blog_author_blogcontributor_blog_contributors'),
    ]

    operations = [
        migrations.RunPython(replace_author_with_contributor)
    ]