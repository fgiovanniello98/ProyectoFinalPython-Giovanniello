from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import ckeditor_uploader.fields

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Pagina",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("titulo", models.CharField(max_length=120)),
                ("subtitulo", models.CharField(max_length=160)),
                ("slug", models.SlugField(blank=True, max_length=160, unique=True)),
                ("contenido", ckeditor_uploader.fields.RichTextUploadingField()),
                ("imagen", models.ImageField(blank=True, null=True, upload_to="paginas")),
                ("fecha_publicacion", models.DateTimeField(auto_now_add=True)),
                ("autor", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="paginas", to=settings.AUTH_USER_MODEL)),
            ],
            options={"ordering": ["-fecha_publicacion"]},
        ),
    ]
