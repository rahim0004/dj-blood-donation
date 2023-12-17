# Generated by Django 4.2.7 on 2023-12-17 04:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_user_division'),
    ]

    operations = [
        migrations.CreateModel(
            name='StemCellDonor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('female', 'Female'), ('male', 'Male')], default='male', max_length=8)),
                ('first_name', models.CharField(max_length=155)),
                ('surname', models.CharField(max_length=155)),
                ('mother_tongue', models.CharField(blank=True, choices=[('bangla', 'Bangla'), ('english', 'English')], max_length=10, null=True)),
                ('on_whatsapp', models.BooleanField(verbose_name='Can We Connect On Whatsapp')),
                ('mobile', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=155)),
            ],
            options={
                'db_table': 'bl_stem_cell_donor',
            },
        ),
        migrations.CreateModel(
            name='SCDonorShippingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(choices=[('bangladesh', 'Bangladesh'), ('others', 'Others')], default='bangladesh', max_length=100)),
                ('divistion', models.CharField(choices=[('Dhaka', 'Dhaka'), ('Chittagong', 'Chittagong'), ('Khulna', 'Khulna'), ('Rajshahi', 'Rajshahi'), ('Barisal', 'Barisal'), ('Sylhet', 'Sylhet'), ('Rangpur', 'Rangpur'), ('Mymensingh', 'Mymensingh')], max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('street', models.CharField(max_length=255)),
                ('area', models.CharField(max_length=255)),
                ('postal_code', models.CharField(max_length=255)),
                ('donor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.stemcelldonor')),
            ],
            options={
                'db_table': 'bl_stem_cell_donor_shipping',
            },
        ),
        migrations.CreateModel(
            name='SCDonorContactPerson2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=155)),
                ('surname', models.CharField(max_length=155)),
                ('relationship', models.CharField(choices=[('brother', 'Brother'), ('sister', 'Sister'), ('cousin', 'Cousin'), ('friend', 'Friend'), ('husband', 'Husband'), ('wife', 'Wife'), ('aunt', 'Aunt'), ('uncle', 'Uncle')], max_length=20)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('donor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.stemcelldonor')),
            ],
            options={
                'db_table': 'bl_stem_cell_donor_contact_2',
            },
        ),
        migrations.CreateModel(
            name='SCDonorContactPerson1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=155)),
                ('surname', models.CharField(max_length=155)),
                ('relationship', models.CharField(choices=[('brother', 'Brother'), ('sister', 'Sister'), ('cousin', 'Cousin'), ('friend', 'Friend'), ('husband', 'Husband'), ('wife', 'Wife'), ('aunt', 'Aunt'), ('uncle', 'Uncle')], max_length=20)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('donor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.stemcelldonor')),
            ],
            options={
                'db_table': 'bl_stem_cell_donor_contact_1',
            },
        ),
    ]
