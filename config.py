from_email = '@mail.ru'
password = ''
name = 'Иван'
contacts = {
    "ВКонтакте": "https://vk.com/id12345",
    "Telegram": "telegrammm"
}

html = """
<html>
  <head></head>
  <body>
    <p>   
    Здравствуйте, {0}!<br>
    <br><br>
    Меня зовут {1}. Я студент 2 курса магистратуры факультета цифровых технологий и химического инжиниринга (ЦиТХИн). Вы подали документы на одно из направлений подготовки нашего факультета, и я предлагаю Вам мою помощь в вопросах, связанных с выбором факультета и направления подготовки. Вы можете спросить меня об изучаемых дисциплинах, процессе обучения, студенческой жизни, досуге и спорте, общественной и культурной работе. Задавайте любые вопросы, которые Вас будут интересовать. Я постараюсь ответить на большинство из них, а на какие не смогу (например, по поводу процедуры поступления или перспектив прохождения по конкурсу), перенаправлю их для квалифицированного ответа сотрудникам отборочной комиссии нашего факультета.<br><br>
    Вы можете со мной связаться ответным электронным письмом или с использованием одного из следующих моих контактов:
    <br><br>
    {2}
    <br>
    Также Вы можете самостоятельно познакомиться с жизнью нашего факультета по следующим ссылкам:
    <br><br>
    – https://vk.com/dekanat_itu – Виртуальный деканат факультета ЦиТХИн – группа для официальной и почти официальной информации для всех студентов и абитуриентов;
    <br><br>
    – https://vk.com/activ_fakulteta_cithin – ЦиТХИн-News – группа студенческого актива нашего факультета для информации о студенческой жизни до и после учёбы;
    <br><br>
    – https://vk.com/ab_itu – группа только для абитуриентов нашего факультета, где для них более компактно и целенаправленно собрана и представляется вся актуальная информация;
    <br><br>
    – https://vk.me/join/4d3nPT/VAWDA8N3LIMlo6x/wg7iUk7NzjTU= – беседа Вконтакте для абитуриентов факультета ЦиТХИн В ней можно задать вопросы декану, студентам нашего факультета и сотрудникам Приемной комиссии.
    <br><br>
    Будет очень здорово, если скоро Вы присоединитесь к нашей дружной семье. Желаю Вам удачного поступления!
    <br><br>
    С уважением, {1}<br>
    </p>
  </body>
</html>
"""