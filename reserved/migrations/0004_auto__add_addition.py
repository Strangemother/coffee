# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Addition'
        db.create_table(u'reserved_addition', (
            (u'namedobject_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['reserved.NamedObject'], unique=True, primary_key=True)),
            ('min_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('max_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'reserved', ['Addition'])

        # Adding M2M table for field extras on 'Category'
        m2m_table_name = db.shorten_name(u'reserved_category_extras')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('category', models.ForeignKey(orm[u'reserved.category'], null=False)),
            ('addition', models.ForeignKey(orm[u'reserved.addition'], null=False))
        ))
        db.create_unique(m2m_table_name, ['category_id', 'addition_id'])

        # Adding M2M table for field extras on 'Menu'
        m2m_table_name = db.shorten_name(u'reserved_menu_extras')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('menu', models.ForeignKey(orm[u'reserved.menu'], null=False)),
            ('addition', models.ForeignKey(orm[u'reserved.addition'], null=False))
        ))
        db.create_unique(m2m_table_name, ['menu_id', 'addition_id'])

        # Adding M2M table for field extras on 'Product'
        m2m_table_name = db.shorten_name(u'reserved_product_extras')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('product', models.ForeignKey(orm[u'reserved.product'], null=False)),
            ('addition', models.ForeignKey(orm[u'reserved.addition'], null=False))
        ))
        db.create_unique(m2m_table_name, ['product_id', 'addition_id'])


    def backwards(self, orm):
        # Deleting model 'Addition'
        db.delete_table(u'reserved_addition')

        # Removing M2M table for field extras on 'Category'
        db.delete_table(db.shorten_name(u'reserved_category_extras'))

        # Removing M2M table for field extras on 'Menu'
        db.delete_table(db.shorten_name(u'reserved_menu_extras'))

        # Removing M2M table for field extras on 'Product'
        db.delete_table(db.shorten_name(u'reserved_product_extras'))


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
        u'reserved.addition': {
            'Meta': {'object_name': 'Addition', '_ormbases': [u'reserved.NamedObject']},
            'max_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'min_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'namedobject_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['reserved.NamedObject']", 'unique': 'True', 'primary_key': 'True'})
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
            'extras': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['reserved.Addition']", 'null': 'True', 'blank': 'True'}),
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
            'location_id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'reserved.menu': {
            'Meta': {'object_name': 'Menu', '_ormbases': [u'reserved.NamedObject']},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['reserved.Category']", 'null': 'True', 'blank': 'True'}),
            'extras': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['reserved.Addition']", 'null': 'True', 'blank': 'True'}),
            u'namedobject_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['reserved.NamedObject']", 'unique': 'True', 'primary_key': 'True'}),
            'products': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['reserved.Product']", 'null': 'True', 'blank': 'True'}),
            'times': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['reserved.Timing']", 'null': 'True', 'blank': 'True'})
        },
        u'reserved.namedobject': {
            'Meta': {'object_name': 'NamedObject'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'icon_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'reserved.product': {
            'Meta': {'object_name': 'Product', '_ormbases': [u'reserved.NamedObject']},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['reserved.Category']", 'null': 'True', 'blank': 'True'}),
            'extras': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['reserved.Addition']", 'null': 'True', 'blank': 'True'}),
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
            'Meta': {'object_name': 'Timing', '_ormbases': [u'reserved.NamedObject']},
            'active_time': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'deactive_time': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'namedobject_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['reserved.NamedObject']", 'unique': 'True', 'primary_key': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
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