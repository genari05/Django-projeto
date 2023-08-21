from django.db import models

from django.db.models import signals
from django.template.defaultfilters import slugify


class Base (models.Model):
    criador = models.DateField('Data de criação', auto_now_add=True)
    motivador = models.DateField('Data de atualização', auto_now= True)
    ativo = models.BooleanField('data de alteração', default=True)

    class Meta:
        abstract = True


class Produto(Base):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('preco', max_digits=8, decimal_places=2)
    estoque = models.IntegerField('estoque')
    imagem = models.ImageField('imagem', upload_to='produtos')
    slug = models.SlugField('slug', max_length=100, blank=True, editable=False)

    def __str__(self):
        return self.nome


def produto_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)


signals.pre_save.connect(produto_pre_save, sender=Produto)
