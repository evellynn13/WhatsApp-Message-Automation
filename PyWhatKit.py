import pywhatkit as kit

# Envia mensagem e fecha a aba do navegador automaticamente
# Formato do número: código do país + DDD + número (sem espaços)
kit.sendwhatmsg_instantly(
    phone_no="+5585",   # substitua pelo número real
    message="Olá! Esta é uma mensagem automática enviada com Python. MENSAGEM 02",
    wait_time=10,                 # segundos de espera antes de enviar (dá tempo do WhatsApp Web carregar)
    tab_close=True,               # fecha a aba após enviar
    close_time=5                 # espera 3 segundos antes de fechar a aba
)