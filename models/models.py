#gravacao_lg = db.define_table("gravacao_lg",
#      Field("datetime"),
#      Field("acao"),
#      Field("pastas"),
#      #auth.signature
#      format="%(nome)s")

Audios = db.define_table("audios",
	Field("nome", notnull=True, unique=True),
	Field('audio', 'upload', uploadfolder='/aldeia/etc/asterisk/audio/cliente', autodelete=True),
	format="%(nome)s")

Uras = db.define_table("uras",
	Field("nome", notnull=True, unique=True),
	Field("id_audio", db.audios),
	Field("timeout"),
	Field("loop_ura"),
	Field("digitos"),
	format="%(nome)s")

Acoes = db.define_table("acoes",
	Field("nome"),
	Field("acao"),
	format="%(nome)s")

Ura_acoes = db.define_table("ura_acoes",
	Field("id_ura", db.uras),
	Field("dtmf"),
	Field("id_acao", db.acoes),
	Field("variavel"),
	format="%(nome)s")

if db(db.acoes.id>0).count() == 0:
    db.acoes.insert(nome='Discar', acao='goto(ramais,#,LIGUSUARIO)')
    db.acoes.insert(nome='Ura', acao='goto(from-pstn,1011,URA_PARAMETRO)')
    db.acoes.insert(nome='Audio', acao='playback(#)')
    db.acoes.insert(nome='Desligar', acao='Hangup()')
    db.commit()






