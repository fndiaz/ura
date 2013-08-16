# coding=UTF-8
import commands, os

def audio():
	response.title = 'Audios'
	db.audios.id.readable=False

	grid = SQLFORM.grid(db.audios, csv=False,
					details=False, searchable=True, editable=True, 
					create=False,  user_signature=False)
	
	return response.render("initial/show_grid_audio.html", grid=grid)


def add_audio():
	response.title = 'Audios'
	form = SQLFORM(db.audios, submit_button='Enviar', deletable=True, 
		fields=['nome', 'audio'])
	
	if form.process().accepted:
		audio = form.vars.audio
		#print request.vars.nome
		audio_nome=audio.replace('.wav', '') #tirando extensão do nome

		saida = os.system("sox /aldeia/etc/asterisk/audio/cliente/%s -t" 
			"raw -r 8000 /aldeia/etc/asterisk/audio/cliente/%s.sln" % (audio, audio_nome)) #convertendo audio
		if saida is 0: #testa conversão do audio
			print 'ok'
			session.flash = 'audio recebido com sucesso'
			redirect(URL("initial", "/audio"))
		else:
			response.flash = 'Erro de conversão, contate o desenvolvedor'	
	elif form.errors:
		response.flash = 'erro, algo não deu certo'
	
	return response.render("initial/show_form_audio.html", form=form)


def uras():
	response.title = 'Atendimentos'
	db.uras.id.readable=False

	links = [ lambda row: A('+', _class='btn', 
				_title='Adicionar ação', 
				_href=URL("initial", "/add_ura_acoes", 
				vars=dict(id=row.id))),
			  lambda row: A('Ações', _class='btn', 
				_title='Ver ações', 
				_href=URL("initial", "/ura_acoes", 
				vars=dict(id=row.id))) ]

	grid = SQLFORM.grid(db.uras, csv=False,
					details=False, searchable=True, editable=True, 
					create=False,  user_signature=False, links=links)
	
	return response.render("initial/show_grid_uras.html", grid=grid)

def add_uras():
	response.title = 'Atendimentos'
	form = SQLFORM(db.uras, submit_button='Criar', deletable=True)
	
	if form.process().accepted:
		#print form.vars.audio
		#print request.vars.nome
		session.flash = 'ura criada com sucesso'
		redirect(URL("initial", "/uras"))
	elif form.errors:
		response.flash = 'erro, algo não deu certo'
	
	return response.render("initial/show_form_uras.html", form=form)

def acoes():
	response.title = 'Ações'
	db.acoes.id.readable=False

	grid = SQLFORM.grid(db.acoes, csv=False, maxtextlength=103,
					details=False, searchable=True, editable=False,  
					create=False,  user_signature=False, deletable=False)
	
	return response.render("initial/show_grid.html", grid=grid)

def add_acoes():
	response.title = 'Padrão'
	form = SQLFORM(db.acoes, deletable=True)
	
	if form.process().accepted:
		#print form.vars.audio
		#print request.vars.nome
		session.flash = 'audio recebido com sucesso'
		redirect(URL("initial", "/acoes"))
	elif form.errors:
		response.flash = 'erro, algo não deu certo'
	
	return response.render("initial/show_form.html", form=form)

def ura_acoes():
	response.title = 'Detalhada'
	id_ura = request.vars.id
	db.ura_acoes.id.readable=False

	query = (db.ura_acoes.id_ura == id_ura)

	grid = SQLFORM.grid(query, csv=False, orderby=db.ura_acoes.dtmf, 
					details=False, searchable=True, editable=True, 
					create=False,  user_signature=False)
	
	return response.render("initial/show_grid_uraacoes.html", grid=grid)

def add_ura_acoes():
	#nao estou usando sqlform -- formulario puro
	uras = db.executesql("SELECT nome FROM uras")
	lista_uras=[]
	for ura in uras:
		lista_uras.append(ura[0])

	form = SQLFORM.factory(
		Field('teste', requires=IS_IN_DB(db, 'acoes.id', '%(nome)s')),
		Field('dep1', requires=IS_IN_SET(lista_uras)),
		Field('dep2', requires=IS_IN_DB(db, 'uras.id', '%(nome)s'))
		)
	if form.process().accepted:
		print form.teste
		print form.dep1
		print form.dep2
	
	return response.render("initial/show_form_ext.html", form=form)

def ajax_uras():
	#print request.vars['teste']
	uras = db.executesql("SELECT id, nome FROM uras")
	print uras
	drop2=[dict([x]) for x in uras]

	return response.json(uras)

def ajax_ramais():
	ramais = db.executesql("SELECT ramal_virtual FROM ramal_virtual")

	return response.json(ramais)

def ajax_acoes():
	acoes = db.executesql("SELECT id, nome FROM acoes")

	return response.json(acoes)

def ajax_audios():
	audios = db.executesql("SELECT id, nome FROM audios")

	return response.json(audios)


def form_ura_acoes():
	#processa o form ura_acoes e insere no banco
	ura = request.vars['ura']
	dtmf = request.vars['dtmf']
	acao = request.vars['acao']
	opc = request.vars['opc']
	print ura

	db.executesql("INSERT INTO ura_acoes (id_ura, dtmf, id_acao, variavel) values ('%s', '%s', '%s', '%s')" % (ura, dtmf, acao, opc))
	redirect(URL("initial", "/ura_acoes?id=%s" % (ura)))

def sobre():
	response.title = 'Sobre'
	return response.render("initial/principal.html")

def principal():
	redirect(URL("initial", "/audio"))

def valida_form():
	#confere campo dtmf do form ura_acoes
	id_ura = request.vars['id']
	dtmf = request.vars['dtmf']
	dtmf_ok = "'"+dtmf+"'"
	var = db.executesql("SELECT count(*) FROM ura_acoes WHERE id_ura = %s and dtmf = %s" % (id_ura, dtmf_ok))
	var2 = var[0][0]
	if var2  == 0:
		a = True
	if var2 == 1:
		a = False

	return response.json(a)



def user():
	print a

def register():
	return auth.register()

def login():
        return auth.login()

def account():
    return dict(register=auth.register(),
                login=auth.login())
	
def download():
	return response.download(request, db)



	



