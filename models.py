class Trabalho(db.Model):
    __tablename__ = 'trabalhos'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    titulo = db.Column(
        db.String(255),
        nullable=False
    )

    resumo = db.Column(
        db.Text
    )

    status = db.Column(
        db.String(50),
        default='AGUARDANDO_CORRECAO'
    )

    nota_final = db.Column(
        db.Float
    )

    feedback = db.Column(
        db.Text
    )

    estudante_id = db.Column(
        db.Integer,
        db.ForeignKey('usuario.id')
    )