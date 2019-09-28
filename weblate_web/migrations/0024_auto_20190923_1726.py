# Generated by Django 2.2.3 on 2019-09-23 15:26

from django.db import migrations


def migrate_service(apps, schema_editor):
    Report = apps.get_model("weblate_web", "Report")
    for report in Report.objects.all():
        report.service = report.subscription.service
        report.save(update_fields=["service"])


class Migration(migrations.Migration):

    dependencies = [("weblate_web", "0023_report_service")]

    operations = [
        migrations.RunPython(migrate_service, migrations.RunPython.noop, elidable=True)
    ]