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
    render_table: function (data) {
        $('#table_body').empty()
        for (let index = 0; index < cause_table.length; index++) {
            let ct = cause_table[index]
            ct.age = age_table[data[index] - 1].name
            $('#table_body').append(`
                <tr>
                    <td>${ct.id}</td>
                    <td>${ct.name}</td>
                    <td>${ct.age}</td>
                    <td>${ct.icd}</td>
                </tr>
            `)
        }

        let total = 0;
        for (var index = 0; index < data.length; index++) {
            age_code = parseInt(data[index])
            switch (age_code) {
                case 1:
                case 99:
                    break
                case 2:
                case 3:
                case 4:
                case 5:
                case 6:
                    total += 1
                    break
                default:
                    let n = (age_code - 7) + 1 // 7+(n-1)*1 = Y
                    total += (7 + (n - 1) * 5) // 7+(n-1)*5 = Z
                    break
            }
        }
        $('#average').text((total / data.length).toFixed(1))
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
        $('.result').hide()
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
                Page.render_table(data)
                $('#submit').prop('disabled', false)
                $('.loading').hide()
                $('.result').show()
            }, 666)
        }).fail((jqXHR, textStatus, errorThrown) => {
            console.log(`${textStatus}: ${errorThrown}`)
        })
    })
})
