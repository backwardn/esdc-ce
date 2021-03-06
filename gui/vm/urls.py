from django.conf.urls import patterns, url

urlpatterns = patterns(
    'gui.vm.views',

    url(r'^$', 'my_list', name='vm_list'),
    url(r'^settings/$', 'multi_settings_form', name='vm_multi_settings_form'),
    url(r'^import/sample/$', 'vm_import_sample', name='vm_import_sample'),
    url(r'^export/$', 'vm_export', name='vm_export'),

    url(r'^add/settings/$', 'add_settings_form', name='vm_add_settings_form'),
    url(r'^add/import/$', 'add_import_form', name='vm_add_import_form'),
    url(r'^add/$', 'add', name='vm_add'),

    url(r'^(?P<hostname>[A-Za-z0-9\._-]+)/$', 'details', name='vm_details'),
    url(r'^(?P<hostname>[A-Za-z0-9\._-]+)/console/$', 'console', name='vm_console'),
    url(r'^(?P<hostname>[A-Za-z0-9\._-]+)/console/vnc/$', 'vnc', name='vnc'),
    url(r'^(?P<hostname>[A-Za-z0-9\._-]+)/snapshot/$', 'snapshot', name='vm_snapshot'),
    url(r'^(?P<hostname>[A-Za-z0-9\._-]+)/snapshot/form/$', 'snapshot_form', name='vm_snapshot_form'),
    url(r'^(?P<hostname>[A-Za-z0-9\._-]+)/snapshot/list/$', 'snapshot_list', name='vm_snapshot_list'),
    url(r'^(?P<hostname>[A-Za-z0-9\._-]+)/snapshot/define/form/$', 'snapshot_define_form',
        name='vm_snapshot_define_form'),
    url(r'^(?P<hostname>[A-Za-z0-9\._-]+)/snapshot/image/form/$', 'snapshot_image_form',
        name='vm_snapshot_image_form'),
    url(r'^(?P<hostname>[A-Za-z0-9\._-]+)/backup/$', 'backup', name='vm_backup'),
    url(r'^(?P<hostname>[A-Za-z0-9\._-]+)/backup/form/$', 'backup_form', name='vm_backup_form'),
    url(r'^(?P<hostname>[A-Za-z0-9\._-]+)/backup/list/$', 'backup_list', name='vm_backup_list'),
    url(r'^(?P<hostname>[A-Za-z0-9\._-]+)/backup/define/form/$', 'backup_define_form',
        name='vm_backup_define_form'),
    url(r'^(?P<hostname>[A-Za-z0-9\._-]+)/nic/(?P<nic_id>\d{1,2})/ptr/$', 'ptr_form', name='vm_ptr_form'),
    url(r'^(?P<hostname>[A-Za-z0-9\._-]+)/settings/nic/$', 'nic_settings_form', name='vm_nic_settings_form'),
    url(r'^(?P<hostname>[A-Za-z0-9\._-]+)/settings/disk/$', 'disk_settings_form', name='vm_disk_settings_form'),
    url(r'^(?P<hostname>[A-Za-z0-9\._-]+)/settings/undo/$', 'undo_settings', name='vm_undo_settings'),
    url(r'^(?P<hostname>[A-Za-z0-9\._-]+)/settings/$', 'settings_form', name='vm_settings_form'),
    url(r'^(?P<hostname>[A-Za-z0-9\._-]+)/installed/$', 'set_installed', name='vm_installed'),
    url(r'^(?P<hostname>[A-Za-z0-9\._-]+)/monitoring/$', 'monitoring', name='vm_monitoring'),
    url(r'^(?P<hostname>[A-Za-z0-9\._-]+)/monitoring/(?P<graph_type>[A-Za-z0-9-]+)/$', 'monitoring',
        name='vm_monitoring_graphs'),
    url(r'^(?P<hostname>[A-Za-z0-9\._-]+)/tasklog/$', 'tasklog', name='vm_tasklog'),
)
