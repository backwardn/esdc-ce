var DC_USERS = null;
function DcUserList(all) {
  var self = this;
  var nosort;

  if (all) {
    nosort = [4, -1];
  } else {
    nosort = [4];
  }

  // Sortable list
  this.list = new ObjList($.noop, nosort, {'icon-tag': [3, 5, 6]}, null);

  // Edit modal (attach/detach, delete, update)
  this.list.elements.table.find('a.obj_edit, a.obj_edit_or_add_dc').click(function() {

    self.list.modal = new obj_form_modal($(this), '#obj_form_modal', function(mod) {
      var btn_delete_dc = mod.mod.find('a.vm_modal_delete_dc');
      var btn_create_dc = mod.mod.find('a.vm_modal_create_dc');
      var btn_edit_profile = mod.mod.find('a.vm_modal_profile');

      btn_delete_dc.hide();
      btn_create_dc.hide();
      btn_edit_profile.hide();

      if (!mod.add) {
        if (mod.btn.hasClass('obj_edit_or_add_dc')) {
          btn_create_dc.show();
          btn_edit_profile.hide();
          mod.mod.find('span.title_edit_or_add_dc').show();
          mod.mod.find('span.title_edit').hide();
        } else {
          btn_delete_dc.show();
          btn_edit_profile.show();
          mod.mod.find('span.title_edit_or_add_dc').hide();
        }
      }

      // User pressed Edit Profile button, redirect to profile update URL
      btn_edit_profile.click(function() {
        ajax_move(self, mod.btn.data('profileUrl'));
      });

    });

    return false;
  });

  // Add modal
  this.list.elements.table.find('a.obj_add_admin').click(function() {

    self.list.modal = new obj_form_modal($(this), '#obj_form_modal', function(mod) {

      var btn_edit_profile = mod.mod.find('a.vm_modal_profile');
      var alias = $('#id_adm-alias');
      var name = $('#id_adm-name');

      btn_edit_profile.hide();

      name.off('focusout').focusout(function() {
        if (!alias.val()) {
          alias.val(name.val().replace('_', ' ').replace('-', ' '));
        }
      });

      mod.btn_more.click();
    });

    return false;
  });

  // Attach modal
  this.list.elements.table.find('a.obj_add_dc').click(function() {
    self.list.modal = new obj_form_modal($(this), '#obj_add_dc_modal', _update_name_choices);
    return false;
  });
} // DcUserList
