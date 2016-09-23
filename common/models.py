
from django.db import models
from django.shortcuts import render

from wagtail.wagtailcore.models import Page
from wagtail.wagtailimages.models import Image
from wagtail.wagtailsnippets.models import register_snippet

from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore import blocks
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailembeds.blocks import EmbedBlock

from wagtail.wagtailsnippets.edit_handlers import SnippetChooserPanel
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel
from wagtail.wagtailadmin.edit_handlers import MultiFieldPanel
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailadmin.edit_handlers import FieldRowPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailadmin.edit_handlers import PageChooserPanel
from wagtail.wagtailsearch import index

from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from taggit.models import TaggedItemBase
from taggit.managers import TaggableManager
from modelcluster.contrib.taggit import ClusterTaggableManager


COLOUR_CHOICES = [
    ('white', 'White'),
    ('grey', 'Grey'),
    ('blue', 'Blue'),
]

COLUMN_CHOICES = [
    ('12', '12/12'),
    ('11', '11/12'),
    ('10', '10/12'),
    ('9', '9/12'),
    ('8', '8/12'),
    ('7', '7/12'),
    ('6', '6/12'),
    ('5', '5/12'),
    ('4', '4/12'),
    ('3', '3/12'),
    ('2', '2/12'),
    ('1', '1/12'),
    ('0', '0/12'),
]

class GoogleMapBlock(blocks.StructBlock):
    address = blocks.CharBlock(required=True,max_length=255)
    map_zoom_level = blocks.CharBlock(default=14,required=True,max_length=3)

    class Meta:
        template = 'common/blocks/google_map.html'
        icon = 'cogs'
        label = 'Google Map'


class COSPhotoStreamBlock(blocks.StructBlock):

    class Meta:
        template = 'common/blocks/flickr.html'
        icon = 'image'
        label = 'Photo Stream'


class TwitterBlock(blocks.StructBlock):
    username = blocks.CharBlock(required=True)

    class Meta:
        template = 'common/blocks/twitter.html'
        icon = 'placeholder'
        label = 'Twitter Stream'


class ThreeColumnBlock(blocks.StructBlock):
 
    background = blocks.ChoiceBlock(choices=COLOUR_CHOICES,default="white")
    left_column = blocks.StreamBlock([
            ('heading', blocks.CharBlock(classname="full title")),
            ('paragraph', blocks.RichTextBlock()),
            ('image', ImageChooserBlock(template='common/blocks/image.html')),
            ('appeal', blocks.StructBlock([
                    ('icon', blocks.ChoiceBlock(required=True, choices=[
                        ('none', 'none'),
                        ('flask', 'flask'),
                        ('group', 'group'),
                        ('laptop', 'laptop'),
                        ('sitemap', 'sitemap'),
                        ('user', 'user'),
                        ('book', 'book'),
                        ('download', 'download'),
                    ])),
                    ('topic', blocks.CharBlock(required=True, max_length=30)),
                    ('content', blocks.TextBlock(required=True, max_length=255)),
            ], classname='appeal', icon='tick', template='common/blocks/appeal.html')),
            ('embedded_video', EmbedBlock()),
            ('google_map', GoogleMapBlock()),
            ('twitter_feed', TwitterBlock()),
            ('photo_stream', COSPhotoStreamBlock()),
        ], icon='arrow-left', label='Left column content', classname='col4')
 
    center_column = blocks.StreamBlock([
            ('heading', blocks.CharBlock(classname="full title")),
            ('paragraph', blocks.RichTextBlock()),
            ('image', ImageChooserBlock(template='common/blocks/image.html')),
            ('appeal', blocks.StructBlock([
                    ('icon', blocks.ChoiceBlock(required=True, choices=[
                        ('none', 'none'),
                        ('flask', 'flask'),
                        ('group', 'group'),
                        ('laptop', 'laptop'),
                        ('sitemap', 'sitemap'),
                        ('user', 'user'),
                        ('book', 'book'),
                        ('download', 'download'),
                    ])),
                    ('topic', blocks.CharBlock(required=True, max_length=30)),
                    ('content', blocks.TextBlock(required=True, max_length=255)),
            ], classname='appeal', icon='tick', template='common/blocks/appeal.html')),
            ('embedded_video', EmbedBlock()),
            ('google_map', GoogleMapBlock()),
            ('twitter_feed', TwitterBlock()),
            ('photo_stream', COSPhotoStreamBlock()),
        ], icon='arrow-right', label='Center column content', classname='col4')
    
    right_column = blocks.StreamBlock([
            ('heading', blocks.CharBlock(classname="full title")),
            ('paragraph', blocks.RichTextBlock()),
            ('image', ImageChooserBlock()),
            ('appeal', blocks.StructBlock([
                    ('icon', blocks.ChoiceBlock(required=True, choices=[
                        ('none', 'none'),
                        ('flask', 'flask'),
                        ('group', 'group'),
                        ('laptop', 'laptop'),
                        ('sitemap', 'sitemap'),
                        ('user', 'user'),
                        ('book', 'book'),
                        ('download', 'download'),
                    ])),
                    ('topic', blocks.CharBlock(required=True, max_length=30)),
                    ('content', blocks.TextBlock(required=True, max_length=255)),
            ], classname='appeal', icon='tick', template='common/blocks/appeal.html')),
            ('embedded_video', EmbedBlock()),
            ('google_map', GoogleMapBlock()),
            ('twitter_feed', TwitterBlock()),
            ('photo_stream', COSPhotoStreamBlock()),
        ], icon='arrow-right', label='Right column content', classname='col4')
 
    class Meta:
        template = 'common/blocks/three_column_block.html'
        icon = 'placeholder'
        label = 'Three Columns'

class TwoColumnBlock(blocks.StructBlock):
    
    background = blocks.ChoiceBlock(choices=COLOUR_CHOICES,default="white")
    left_column_size = blocks.ChoiceBlock(choices=COLUMN_CHOICES,default="6")
    right_column_size = blocks.ChoiceBlock(choices=COLUMN_CHOICES, default="6")
    left_column = blocks.StreamBlock([
            ('heading', blocks.CharBlock(classname="full title")),
            ('paragraph', blocks.RichTextBlock()),
            ('image', ImageChooserBlock(template='common/blocks/image.html')),
            ('appeal', blocks.StructBlock([
                    ('icon', blocks.ChoiceBlock(required=True, choices=[
                        ('none', 'none'),
                        ('flask', 'flask'),
                        ('group', 'group'),
                        ('laptop', 'laptop'),
                        ('sitemap', 'sitemap'),
                        ('user', 'user'),
                        ('book', 'book'),
                        ('download', 'download'),
                    ])),
                    ('topic', blocks.CharBlock(required=True, max_length=30)),
                    ('content', blocks.TextBlock(required=True, max_length=255)),
            ], classname='appeal', icon='tick', template='common/blocks/appeal.html')),
            ('embedded_video', EmbedBlock()),
            ('google_map', GoogleMapBlock()),
            ('twitter_feed', TwitterBlock()),
        ], icon='arrow-left', label='Left column content', classname='col4')
 
    right_column = blocks.StreamBlock([
            ('heading', blocks.CharBlock(classname="full title")),
            ('paragraph', blocks.RichTextBlock()),
            ('image', ImageChooserBlock(template='common/blocks/image.html')),
            ('appeal', blocks.StructBlock([
                    ('icon', blocks.ChoiceBlock(required=True, choices=[
                        ('none', 'none'),
                        ('flask', 'flask'),
                        ('group', 'group'),
                        ('laptop', 'laptop'),
                        ('sitemap', 'sitemap'),
                        ('user', 'user'),
                        ('book', 'book'),
                        ('download', 'download'),
                    ])),
                    ('topic', blocks.CharBlock(required=True, max_length=30)),
                    ('content', blocks.TextBlock(required=True, max_length=255)),
            ], classname='appeal', icon='tick', template='common/blocks/appeal.html')),
            ('embedded_video', EmbedBlock()),
            ('google_map', GoogleMapBlock()),
            ('twitter_feed', TwitterBlock()),
        ], icon='arrow-right', label='Right column content', classname='col4')
 
    class Meta:
        template = 'common/blocks/two_column_block.html'
        icon = 'placeholder'
        label = 'Two Columns'


class TabBlock(blocks.StructBlock):
    id = blocks.CharBlock(required=True)
    isActive = blocks.BooleanBlock(default=False, required=False)
    container = blocks.StreamBlock([('two_column_block', TwoColumnBlock()), ('paragraph', blocks.RichTextBlock())])
    class Meta:
        template = 'common/blocks/tab_block.html'
        icon = 'plus'
        label = 'Tab'


class TabContainerBlock(blocks.StructBlock):
    tabs = blocks.StreamBlock([('tab', TabBlock())])
    class Meta:
        template = 'common/blocks/tabs_container_block.html'
        icon = 'placeholder'
        label = 'Tab Container'


class TabIndexBlock(blocks.StructBlock):
    tabsIndexes = blocks.StreamBlock([('tab_id', blocks.TextBlock(max_length=25))])

    class Meta:
        template = 'common/blocks/tab_index_block.html'
        icon = 'list-ul'
        label = "Tab index"


@register_snippet
class Person(ClusterableModel, index.Indexed):
    
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255)
    bio = RichTextField(blank=True)

    photo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    other_info = StreamField([
        ('position', blocks.TextBlock(max_legnth=140)),
        ('term', blocks.TextBlock(max_length=9)),
        ('linked_in', blocks.URLBlock()),
        ('blog', blocks.PageChooserBlock()),
        ('osf_profile', blocks.URLBlock()),
        ('phone_number', blocks.IntegerBlock(min_value=0000000000, max_value=9999999999)),
        ('email_address', blocks.EmailBlock()),
        ('title', blocks.TextBlock(max_length=140)),
        ('fave_food', blocks.TextBlock(max_length=45))
    ])

    tags = TaggableManager(through='common.PersonTag', blank=True)

    panels = [
        MultiFieldPanel([
            FieldPanel('first_name'),
            FieldPanel('middle_name'),
            FieldPanel('last_name'),
            FieldPanel('bio'),
            FieldPanel('tags'),
        ], heading='Basic Information'),
        ImageChooserPanel('photo'),
        StreamFieldPanel('other_info')
    ]
    
    def __str__(self):
        return '{self.last_name}, {self.first_name}'.format(self=self)


class PersonTag(TaggedItemBase):
    content_object = ParentalKey(Person, related_name='tagged_person')


@register_snippet
class Footer(models.Model):

    title = models.CharField(default='untitled', max_length=255)    

    active = models.BooleanField(default=False)

    content = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('twocolumn', TwoColumnBlock()),
        ('threecolumn', ThreeColumnBlock()),
        ('raw_html', blocks.RawHTMLBlock(help_text='With great power comes great responsibility. This HTML is unescaped. Be careful!')),
        ('google_map', GoogleMapBlock()),
        ('twitter_feed', TwitterBlock()),
        ('photo_stream', COSPhotoStreamBlock()),
    ], null=True, blank=True)

    class Meta:
        verbose_name = "Footer"
        verbose_name_plural = "Footers"

    panels = [
        FieldPanel('title'),
        FieldPanel('active'),
        StreamFieldPanel('content'),
    ]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.active:
            for footer in Footer.objects.filter(active=True):
                footer.active = False
                footer.save()
            
        return super(Footer, self).save(*args, **kwargs)


class PeoplePage(Page):

    available_tags = models.ForeignKey(
        'taggit.Tag',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    subtitle = models.CharField(default='untitled', max_length=30)
    statement = models.CharField(max_length=1000)
    display_style = models.CharField(verbose_name='display style', max_length=16,
                                     choices=(('concise', 'Concise Style'), ('detail', 'Detailed Style')))

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('statement'),
        FieldPanel('available_tags'),
        FieldPanel('display_style')
    ]

    def serve(self, request):
        return render(request, self.template, {
            'page': self,
            'people': Person.objects.filter(tags__name=self.available_tags)
        })


class HomePage(Page):

    content = StreamField([
         ('appeal', blocks.StructBlock([
                    ('icon', blocks.ChoiceBlock(required=True, choices=[
                        ('none', 'none'),
                        ('flask', 'flask'),
                        ('group', 'group'),
                        ('laptop', 'laptop'),
                        ('sitemap', 'sitemap'),
                        ('user', 'user'),
                        ('book', 'book'),
                        ('download', 'download'),
                    ])),
            ('topic', blocks.CharBlock(required=True, max_length=30)),
            ('content', blocks.TextBlock(required=True, max_length=255)),
        ], classname='appeal', icon='tick', template='common/blocks/appeal.html')),
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('twocolumn', TwoColumnBlock()),
        ('threecolumn', ThreeColumnBlock()),
        ('tab_index', TabIndexBlock()),
        ('tabcontainerblock', TabContainerBlock()),
        ('raw_html', blocks.RawHTMLBlock(help_text='With great power comes great responsibility. This HTML is unescaped. Be careful!'))
    ], null=True, blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('content'),
    ]


class NewsArticle(Page):
    main_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    date = models.DateField("Post date")
    intro = models.CharField(max_length=1000, blank=True)
    body = RichTextField(blank=True)
    external_link = models.CharField("External Article Link",max_length=255,blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        ImageChooserPanel('main_image'),
        FieldPanel('intro'),
        FieldPanel('body'),
        FieldPanel('external_link'),
    ]

    def serve(self, request):
        return render(request, self.template, {
            'page':self,
            'recent_articles': NewsArticle.objects.all().order_by('-date')[0:5]
        })


class NewsIndexPage(Page):
    statement = models.CharField(blank=True, max_length=1000)

    content_panels = Page.content_panels + [
        FieldPanel('statement', classname="full")
    ]

    def serve(self, request):
        return render(request, self.template, {
            'page': self,
            'newsArticles': NewsArticle.objects.all()
        })


