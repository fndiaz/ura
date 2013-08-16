##Agenda
#db.agenda.empresa.requires = IS_NOT_EMPTY(error_message=
#						T("valor não pode ser nulo"))

#db.agenda.telefone.requires = [IS_NOT_EMPTY(error_message=T("o telefone deve conter de 9 a 11 números")),
#IS_NOT_IN_DB(db, 'agenda.telefone', error_message=T("este número está em uso")),
#IS_LENGTH(minsize=9, maxsize=11, error_message=T("o telefone deve conter de 9 a 11 números")),
#IS_MATCH('[0-9]+', error_message=T("somente números"))]

##Audios
db.audios.nome.requires = [IS_NOT_EMPTY(error_message=T("valor não pode ser nulo")),
IS_NOT_IN_DB(db, 'audios.nome', error_message=T("O valor já existe"))]

db.audios.audio.requires = IS_UPLOAD_FILENAME(extension='wav', error_message=
								T("arquivo precisa conter formato .WAV"))

##Uras
db.uras.nome.requires = [IS_NOT_EMPTY(error_message=T("valor não pode ser nulo")),
IS_NOT_IN_DB(db, 'uras.nome', error_message=T("O valor já existe"))]

db.uras.id_audio.requires = IS_IN_DB(db,db.audios.id, '%(nome)s', error_message=
							T("valor não pode ser nulo"))
db.uras.timeout.requires = IS_NOT_EMPTY(error_message=
								T("valor não pode ser nulo"))
db.uras.loop_ura.requires = IS_NOT_EMPTY(error_message=
								T("valor não pode ser nulo"))
db.uras.digitos.requires = IS_NOT_EMPTY(error_message=
								T("valor não pode ser nulo"))



