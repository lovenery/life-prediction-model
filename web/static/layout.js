var i18n = {
    NOW_LANG: localStorage.getItem('lang') !== null ? localStorage.getItem('lang') : 'en',
    changeLanguage: function (lang) {
        if (i18n[lang] === undefined) {
            $.getJSON('static/locales/' + lang + '.json')
                .done((json) => {
                    i18n[lang] = json
                    this.updateContent(lang)
                })
        } else {
            this.updateContent(lang)
        }
    },
    updateContent: function (lang) {
        let tags = i18n[lang]
        for (let tag_key in tags) {
            let obj = tags[tag_key]
            for (let key in obj) {
                let element = document.getElementById(`i18n-${tag_key}-${key}`)
                if (element !== null) {
                    element.innerHTML = obj[key]
                }
            }
        }
    }
}
i18n.changeLanguage(i18n.NOW_LANG)

// events
$(function() {
    $('.translate').click(() => {
        $('.button-collapse').sideNav('hide')
        if (i18n.NOW_LANG == 'en') {
            i18n.NOW_LANG = 'zh-tw'
            localStorage.setItem('lang', i18n.NOW_LANG)
        } else {
            i18n.NOW_LANG = 'en'
            localStorage.setItem('lang', i18n.NOW_LANG)
        }
        i18n.changeLanguage(i18n.NOW_LANG)
    })
    $('.clear').click(() => {
        localStorage.removeItem('lang')
        localStorage.removeItem('sex')
        localStorage.removeItem('county')
        location.reload()
    })
})