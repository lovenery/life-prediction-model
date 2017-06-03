var Page = {
    sex: '',
    county: '',
    init: function () {
        // data
        this.sex = localStorage.getItem('sex')
        this.county = localStorage.getItem('county')
        this.toggle_submit_button()

        // check radio button
        if (parseInt(this.sex) == 1) {
            $('#male').prop('checked', true)
        } else if (parseInt(this.sex) == 2) {
            $('#female').prop('checked', true)
        }

        // render select tag
        for (let index = 0; index < county_table.length; index++) {
            let ct = county_table[index]
            let element = `<option value="${ct.id}">${ct.name}</option>`
            if (ct.id === parseInt(this.county)) {
                element = `<option value="${ct.id}" selected>${ct.name}</option>`
            }
            $('#county').append(element)
        }
    },
    toggle_submit_button: function () {
        if (this.sex === null || this.county === null) {
            $('#submit').prop('disabled', true)
        } else {
            $('#submit').prop('disabled', false)
        }
    },
    render_result: function (data) {
        $('#result').empty()
        for (let index = 0; index < cause_table.length; index++) {
            let ct = cause_table[index]
            ct.age = age_table[data[index] - 1].name
            $('#result').append(`
                <tr>
                    <td>${ct.id}</td>
                    <td>${ct.name}</td>
                    <td>${ct.age}</td>
                    <td>${ct.icd}</td>
                </tr>
            `)
        }
    }
}
Page.init()

// events
$(function() {
    $('input[name=gender]').change(function () {
        Page.sex = this.value
        localStorage.setItem('sex', Page.sex)
        Page.toggle_submit_button()
    })
    $('#county').change(function() {
        Page.county = this.value
        localStorage.setItem('county', Page.county)
        Page.toggle_submit_button()
    })
    $('#submit').click((e) => {
        e.preventDefault()
        $('#submit').prop('disabled', true)
        $('.loading').show()
        $('#table').hide()
        let data = {
            county: Page.county,
            sex: Page.sex
        }
        $.ajax({
            url: '/api',
            method: 'POST',
            data: JSON.stringify(data),
        }).done((data, textStatus, jqXHR) => {
            setTimeout(() => {
                Page.render_result(data)
                $('#submit').prop('disabled', false)
                $('.loading').hide()
                $('#table').show()
            }, 666)
        }).fail((jqXHR, textStatus, errorThrown) => {
            console.log(`${textStatus}: ${errorThrown}`)
        })
    })
})
