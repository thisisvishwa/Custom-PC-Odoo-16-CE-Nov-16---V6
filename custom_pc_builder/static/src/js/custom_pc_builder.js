odoo.define('custom_pc_builder.main', function (require) {
    "use strict";

    var core = require('web.core');
    var Widget = require('web.Widget');
    var ajax = require('web.ajax');

    var QWeb = core.qweb;
    var _t = core._t;

    var CustomPCBuilder = Widget.extend({
        template: 'custom_pc_builder',
        events: {
            'click .component-selection': 'onComponentSelection',
            'click .save-build': 'onSaveBuild',
            'click .load-build': 'onLoadBuild',
        },

        start: function () {
            this.loadComponents();
            return this._super.apply(this, arguments);
        },

        loadComponents: function () {
            var self = this;
            ajax.jsonRpc('/custom_pc_builder/components', 'call', {}).then(function (data) {
                self.$('.components-list').html(QWeb.render('ComponentList', {components: data}));
            });
        },

        onComponentSelection: function (event) {
            var componentId = $(event.currentTarget).data('id');
            this.$('.selected-components').append(QWeb.render('SelectedComponent', {componentId: componentId}));
        },

        onSaveBuild: function () {
            var selectedComponents = this.$('.selected-components .component').map(function () {
                return $(this).data('id');
            }).get();
            ajax.jsonRpc('/custom_pc_builder/save', 'call', {components: selectedComponents}).then(function (response) {
                if (response.success) {
                    alert(_t("Build saved successfully!"));
                } else {
                    alert(_t("Error saving build."));
                }
            });
        },

        onLoadBuild: function () {
            var self = this;
            ajax.jsonRpc('/custom_pc_builder/load', 'call', {}).then(function (data) {
                self.$('.selected-components').html(QWeb.render('SelectedComponents', {components: data}));
            });
        },
    });

    core.action_registry.add('custom_pc_builder', CustomPCBuilder);

    return CustomPCBuilder;
});