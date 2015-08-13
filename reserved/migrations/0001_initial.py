# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'NamedObject'
        db.create_table(u'reserved_namedobject', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('icon_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'reserved', ['NamedObject'])

        # Adding model 'Category'
        db.create_table(u'reserved_category', (
            (u'namedobject_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['reserved.NamedObject'], unique=True, primary_key=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reserved.Category'], null=True, blank=True)),
        ))
        db.send_create_signal(u'reserved', ['Category'])

        # Adding model 'Product'
        db.create_table(u'reserved_product', (
            (u'namedobject_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['reserved.NamedObject'], unique=True, primary_key=True)),
            ('price', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'reserved', ['Product'])

        # Adding M2M table for field category on 'Product'
        m2m_table_name = db.shorten_name(u'reserved_product_category')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('product', models.ForeignKey(orm[u'reserved.product'], null=False)),
            ('category', models.ForeignKey(orm[u'reserved.category'], null=False))
        ))
        db.create_unique(m2m_table_name, ['product_id', 'category_id'])

        # Adding model 'Timing'
        db.create_table(u'reserved_timing', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')()),
            ('active_time', self.gf('django.db.models.fields.TimeField')()),
            ('deactive_time', self.gf('django.db.models.fields.TimeField')()),
        ))
        db.send_create_signal(u'reserved', ['Timing'])

        # Adding model 'Menu'
        db.create_table(u'reserved_menu', (
            (u'namedobject_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['reserved.NamedObject'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'reserved', ['Menu'])

        # Adding M2M table for field categories on 'Menu'
        m2m_table_name = db.shorten_name(u'reserved_menu_categories')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('menu', models.ForeignKey(orm[u'reserved.menu'], null=False)),
            ('category', models.ForeignKey(orm[u'reserved.category'], null=False))
        ))
        db.create_unique(m2m_table_name, ['menu_id', 'category_id'])

        # Adding M2M table for field products on 'Menu'
        m2m_table_name = db.shorten_name(u'reserved_menu_products')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('menu', models.ForeignKey(orm[u'reserved.menu'], null=False)),
            ('product', models.ForeignKey(orm[u'reserved.product'], null=False))
        ))
        db.create_unique(m2m_table_name, ['menu_id', 'product_id'])

        # Adding M2M table for field times on 'Menu'
        m2m_table_name = db.shorten_name(u'reserved_menu_times')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('menu', models.ForeignKey(orm[u'reserved.menu'], null=False)),
            ('timing', models.ForeignKey(orm[u'reserved.timing'], null=False))
        ))
        db.create_unique(m2m_table_name, ['menu_id', 'timing_id'])

        # Adding model 'Location'
        db.create_table(u'reserved_location', (
            (u'address_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['easy_maps.Address'], unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'reserved', ['Location'])

        # Adding model 'Customer'
        db.create_table(u'reserved_customer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
        ))
        db.send_create_signal(u'reserved', ['Customer'])

        # Adding M2M table for field address on 'Customer'
        m2m_table_name = db.shorten_name(u'reserved_customer_address')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('customer', models.ForeignKey(orm[u'reserved.customer'], null=False)),
            ('location', models.ForeignKey(orm[u'reserved.location'], null=False))
        ))
        db.create_unique(m2m_table_name, ['customer_id', 'location_id'])

        # Adding model 'TelephoneType'
        db.create_table(u'reserved_telephonetype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'reserved', ['TelephoneType'])

        # Adding model 'Telephone'
        db.create_table(u'reserved_telephone', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reserved.TelephoneType'])),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reserved.Customer'])),
            ('number', self.gf('phonenumber_field.modelfields.PhoneNumberField')(max_length=128)),
        ))
        db.send_create_signal(u'reserved', ['Telephone'])

        # Adding model 'Company'
        db.create_table(u'reserved_company', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'reserved', ['Company'])

        # Adding M2M table for field addresses on 'Company'
        m2m_table_name = db.shorten_name(u'reserved_company_addresses')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('company', models.ForeignKey(orm[u'reserved.company'], null=False)),
            ('location', models.ForeignKey(orm[u'reserved.location'], null=False))
        ))
        db.create_unique(m2m_table_name, ['company_id', 'location_id'])

        # Adding M2M table for field contact on 'Company'
        m2m_table_name = db.shorten_name(u'reserved_company_contact')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('company', models.ForeignKey(orm[u'reserved.company'], null=False)),
            ('userprofile', models.ForeignKey(orm[u'account.userprofile'], null=False))
        ))
        db.create_unique(m2m_table_name, ['company_id', 'userprofile_id'])

        # Adding M2M table for field telephone on 'Company'
        m2m_table_name = db.shorten_name(u'reserved_company_telephone')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('company', models.ForeignKey(orm[u'reserved.company'], null=False)),
            ('telephone', models.ForeignKey(orm[u'reserved.telephone'], null=False))
        ))
        db.create_unique(m2m_table_name, ['company_id', 'telephone_id'])

        # Adding model 'Venue'
        db.create_table(u'reserved_venue', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('address', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reserved.Location'], null=True, blank=True)),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reserved.Company'])),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['account.UserProfile'], null=True, blank=True)),
        ))
        db.send_create_signal(u'reserved', ['Venue'])

        # Adding M2M table for field contact on 'Venue'
        m2m_table_name = db.shorten_name(u'reserved_venue_contact')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('venue', models.ForeignKey(orm[u'reserved.venue'], null=False)),
            ('customer', models.ForeignKey(orm[u'reserved.customer'], null=False))
        ))
        db.create_unique(m2m_table_name, ['venue_id', 'customer_id'])

        # Adding model 'Booking'
        db.create_table(u'reserved_booking', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('arrival', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('depature', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reserved.Company'], null=True, blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(default='initial', max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'reserved', ['Booking'])

        # Adding M2M table for field customers on 'Booking'
        m2m_table_name = db.shorten_name(u'reserved_booking_customers')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('booking', models.ForeignKey(orm[u'reserved.booking'], null=False)),
            ('customer', models.ForeignKey(orm[u'reserved.customer'], null=False))
        ))
        db.create_unique(m2m_table_name, ['booking_id', 'customer_id'])

        # Adding model 'Event'
        db.create_table(u'reserved_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reserved.Company'], null=True, blank=True)),
            ('start_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('end_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'reserved', ['Event'])

        # Adding M2M table for field venues on 'Event'
        m2m_table_name = db.shorten_name(u'reserved_event_venues')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('event', models.ForeignKey(orm[u'reserved.event'], null=False)),
            ('venue', models.ForeignKey(orm[u'reserved.venue'], null=False))
        ))
        db.create_unique(m2m_table_name, ['event_id', 'venue_id'])

        # Adding M2M table for field bookings on 'Event'
        m2m_table_name = db.shorten_name(u'reserved_event_bookings')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('event', models.ForeignKey(orm[u'reserved.event'], null=False)),
            ('booking', models.ForeignKey(orm[u'reserved.booking'], null=False))
        ))
        db.create_unique(m2m_table_name, ['event_id', 'booking_id'])


    def backwards(self, orm):
        # Deleting model 'NamedObject'
        db.delete_table(u'reserved_namedobject')

        # Deleting model 'Category'
        db.delete_table(u'reserved_category')

        # Deleting model 'Product'
        db.delete_table(u'reserved_product')

        # Removing M2M table for field category on 'Product'
        db.delete_table(db.shorten_name(u'reserved_product_category'))

        # Deleting model 'Timing'
        db.delete_table(u'reserved_timing')

        # Deleting model 'Menu'
        db.delete_table(u'reserved_menu')

        # Removing M2M table for field categories on 'Menu'
        db.delete_table(db.shorten_name(u'reserved_menu_categories'))

        # Removing M2M table for field products on 'Menu'
        db.delete_table(db.shorten_name(u'reserved_menu_products'))

        # Removing M2M table for field times on 'Menu'
        db.delete_table(db.shorten_name(u'reserved_menu_times'))

        # Deleting model 'Location'
        db.delete_table(u'reserved_location')

        # Deleting model 'Customer'
        db.delete_table(u'reserved_customer')

        # Removing M2M table for field address on 'Customer'
        db.delete_table(db.shorten_name(u'reserved_customer_address'))

        # Deleting model 'TelephoneType'
        db.delete_table(u'reserved_telephonetype')

        # Deleting model 'Telephone'
        db.delete_table(u'reserved_telephone')

        # Deleting model 'Company'
        db.delete_table(u'reserved_company')

        # Removing M2M table for field addresses on 'Company'
        db.delete_table(db.shorten_name(u'reserved_company_addresses'))

        # Removing M2M table for field contact on 'Company'
        db.delete_table(db.shorten_name(u'reserved_company_contact'))

        # Removing M2M table for field telephone on 'Company'
        db.delete_table(db.shorten_name(u'reserved_company_telephone'))

        # Deleting model 'Venue'
        db.delete_table(u'reserved_venue')

        # Removing M2M table for field contact on 'Venue'
        db.delete_table(db.shorten_name(u'reserved_venue_contact'))

        # Deleting model 'Booking'
        db.delete_table(u'reserved_booking')

        # Removing M2M table for field customers on 'Booking'
        db.delete_table(db.shorten_name(u'reserved_booking_customers'))

        # Deleting model 'Event'
        db.delete_table(u'reserved_event')

        # Removing M2M table for field venues on 'Event'
        db.delete_table(db.shorten_name(u'reserved_event_venues'))

        # Removing M2M table for field bookings on 'Event'
        db.delete_table(db.shorten_name(u'reserved_event_bookings'))


    models = {
        u'account.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'date_deleted': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'deleted_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['account.UserProfile']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'middle_names': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '256', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'easy_maps.address': {
            'Meta': {'object_name': 'Address'},
            'address': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'computed_address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'geocode_error': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        u'reserved.booking': {
            'Meta': {'object_name': 'Booking'},
            'arrival': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reserved.Company']", 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'customers': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['reserved.Customer']", 'null': 'True', 'blank': 'True'}),
            'depature': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'initial'", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'})
        },
        u'reserved.category': {
            'Meta': {'object_name': 'Category', '_ormbases': [u'reserved.NamedObject']},
            u'namedobject_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['reserved.NamedObject']", 'unique': 'True', 'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reserved.Category']", 'null': 'True', 'blank': 'True'})
        },
        u'reserved.company': {
            'Meta': {'object_name': 'Company'},
            'addresses': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['reserved.Location']", 'symmetrical': 'False'}),
            'contact': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['account.UserProfile']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'telephone': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['reserved.Telephone']", 'symmetrical': 'False'})
        },
        u'reserved.customer': {
            'Meta': {'object_name': 'Customer'},
            'address': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['reserved.Location']", 'symmetrical': 'False'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'reserved.event': {
            'Meta': {'object_name': 'Event'},
            'bookings': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['reserved.Booking']", 'null': 'True', 'blank': 'True'}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reserved.Company']", 'null': 'True', 'blank': 'True'}),
            'end_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'venues': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['reserved.Venue']", 'symmetrical': 'False'})
        },
        u'reserved.location': {
            'Meta': {'object_name': 'Location', '_ormbases': [u'easy_maps.Address']},
            u'address_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['easy_maps.Address']", 'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'reserved.menu': {
            'Meta': {'object_name': 'Menu', '_ormbases': [u'reserved.NamedObject']},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['reserved.Category']", 'null': 'True', 'blank': 'True'}),
            u'namedobject_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['reserved.NamedObject']", 'unique': 'True', 'primary_key': 'True'}),
            'products': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['reserved.Product']", 'null': 'True', 'blank': 'True'}),
            'times': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['reserved.Timing']", 'null': 'True', 'blank': 'True'})
        },
        u'reserved.namedobject': {
            'Meta': {'object_name': 'NamedObject'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'icon_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'reserved.product': {
            'Meta': {'object_name': 'Product', '_ormbases': [u'reserved.NamedObject']},
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['reserved.Category']", 'null': 'True', 'blank': 'True'}),
            u'namedobject_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['reserved.NamedObject']", 'unique': 'True', 'primary_key': 'True'}),
            'price': ('django.db.models.fields.IntegerField', [], {})
        },
        u'reserved.telephone': {
            'Meta': {'object_name': 'Telephone'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reserved.TelephoneType']"}),
            'number': ('phonenumber_field.modelfields.PhoneNumberField', [], {'max_length': '128'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reserved.Customer']"})
        },
        u'reserved.telephonetype': {
            'Meta': {'object_name': 'TelephoneType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'reserved.timing': {
            'Meta': {'object_name': 'Timing'},
            'active_time': ('django.db.models.fields.TimeField', [], {}),
            'deactive_time': ('django.db.models.fields.TimeField', [], {}),
            'end_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {})
        },
        u'reserved.venue': {
            'Meta': {'object_name': 'Venue'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reserved.Location']", 'null': 'True', 'blank': 'True'}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reserved.Company']"}),
            'contact': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['reserved.Customer']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['account.UserProfile']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['reserved']