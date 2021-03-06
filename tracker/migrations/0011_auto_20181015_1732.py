# Generated by Django 2.1 on 2018-10-15 22:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0010_auto_20181010_1640'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category', models.CharField(max_length=50)),
                ('SubCategory', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='workhour',
            name='Work_Code',
        ),
        migrations.AddField(
            model_name='workhour',
            name='Rework',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='WorkCode',
        ),
        migrations.AddField(
            model_name='workhour',
            name='Task_Category',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='tracker.Cat'),
            preserve_default=False,
        ),
    ]
