from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('plants', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=255)),
                ('reminder_time', models.DateTimeField(blank=True, null=True)),
                ('is_completed', models.BooleanField(default=False)),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plants.plant')),
            ],
        ),
        migrations.RunSQL(
            sql="""
                ALTER TABLE reminders_reminder
                ALTER COLUMN reminder_time TYPE timestamp with time zone
                USING (CASE 
                    WHEN reminder_time IS NOT NULL THEN reminder_time::timestamp with time zone
                    ELSE NULL 
                END);
            """,
            reverse_sql="""
                ALTER TABLE reminders_reminder
                ALTER COLUMN reminder_time TYPE time without time zone
                USING (reminder_time::time);
            """,
        ),
    ]