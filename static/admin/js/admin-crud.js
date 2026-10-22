(function ($) {
    'use strict';
        const csrfToken = $('meta[name="csrf-token"]').attr('content');
    window.AdminCRUD = {
        initStatusToggle: function (url, successMsg = 'Status updated successfully') {
            $('input[type="checkbox"][data-toggle="toggle"]')
                .bootstrapToggle()
                .off('change')
                .on('change', function () {
                    const checkbox = $(this);
                    const form = checkbox.closest('form');
                    const statusId = form.find('input[name="status_id"]').val();
                    
                    checkbox.prop('disabled', true);

                    $.ajax({
                        url: url,
                        method: 'POST',
                        headers: { 'X-CSRFToken': csrfToken },
                        data: { status_id: statusId }, 
                        success: function (response) {
                            checkbox.prop('disabled', false);
                            if (response.status === 200 || response.success) {
                                toastr.success(response.message || successMsg);
                            } else {
                                checkbox.prop('checked', !checkbox.prop('checked'));
                                toastr.error(response.message || 'Failed to update status');
                            }
                        },
                        error: function (xhr) {
                            checkbox.prop('disabled', false);
                            checkbox.prop('checked', !checkbox.prop('checked'));
                            toastr.error(xhr.responseJSON?.message || 'Connection error');
                        }
                    });
                });
        },

        initOrderLevel: function (url, successMsg = 'Order updated successfully') {
            $('.order-level-input').off('change').on('change', function () {
                const input = $(this);
                const id = input.data('id');
                const value = input.val();
                const original = input.data('original') || value;

                $.ajax({
                    url: url,
                    type: 'POST',
                    headers: { 'X-CSRFToken': csrfToken },
                    data: { id: id, order_level: value }, 
                    success: function (response) {
                        toastr.success(response.message || successMsg);
                        input.data('original', value);
                    },
                    error: function (xhr) {
                        toastr.error(xhr.responseJSON?.message || 'Error updating order');
                        input.val(original);
                    }
                });
            });
        },

        initFilterAutoSubmit: function (formId = '#filterForm', delay = 300) {
            let timeout;
            $(`${formId} input, ${formId} select`)
                .off('change keyup')
                .on('change keyup', function () {
                    clearTimeout(timeout);
                    timeout = setTimeout(() => {
                        $(formId).submit(); 
                    }, delay);
                });
        }
    };


    window.confirmDelete = function(event, formId) {
        event.preventDefault();
        Swal.fire({
            title: 'Are you sure?',
            text: 'This action cannot be undone.',
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Yes, delete it!'
        }).then((result) => {
            if (result.isConfirmed) {
                document.getElementById(formId).submit();
            }
        });
    };

})(jQuery);