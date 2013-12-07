from oec import db
from oec.utils import AutoSerialize, exist_or_404

class Hs(db.Model, AutoSerialize):

    __tablename__ = 'attr_hs'
    
    id = db.Column(db.String(8), primary_key=True)
    hs = db.Column(db.String(6))
    color = db.Column(db.String(7))
    
    name = db.relationship("Hs_name", backref = 'hs', lazy = 'dynamic')
    
    # def name(self):
    #     lang = getattr(g, "locale", "en")
    #     return title_case(getattr(self,"name_"+lang))
    #     
    # def icon(self):
    #     return "/static/img/icons/hs/hs_%s.png" % (self.id[:2])

    def __repr__(self):
        return '<Hs %r>' % (self.hs)

class Hs_name(db.Model, AutoSerialize):

    __tablename__ = 'attr_hs_name'
    
    hs_id = db.Column(db.String(8), db.ForeignKey(Hs.id), primary_key=True)
    lang = db.Column(db.String(5), primary_key=True)
    name = db.Column(db.String(255))
    keywords = db.Column(db.String(255))
    desc = db.Column(db.Text())
    gender = db.Column(db.String(1))
    plural = db.Column(db.Boolean())
    article = db.Column(db.Boolean())
    
    def __repr__(self):
        return '<Hs Name %r:%r>' % (self.hs_id, self.lang)

class Sitc(db.Model, AutoSerialize):

    __tablename__ = 'attr_sitc'
    
    id = db.Column(db.String(8), primary_key=True)
    sitc = db.Column(db.String(6))
    color = db.Column(db.String(7))
    
    name = db.relationship("Sitc_name", backref = 'sitc', lazy = 'dynamic')
    
    # def name(self):
    #     lang = getattr(g, "locale", "en")
    #     return title_case(getattr(self,"name_"+lang))
    #     
    # def icon(self):
    #     return "/static/img/icons/hs/hs_%s.png" % (self.id[:2])

    def __repr__(self):
        return '<Sitc %r>' % (self.sitc)

class Sitc_name(db.Model, AutoSerialize):

    __tablename__ = 'attr_sitc_name'
    
    sitc_id = db.Column(db.String(8), db.ForeignKey(Sitc.id), primary_key=True)
    lang = db.Column(db.String(5), primary_key=True)
    name = db.Column(db.String(255))
    keywords = db.Column(db.String(255))
    desc = db.Column(db.Text())
    gender = db.Column(db.String(1))
    plural = db.Column(db.Boolean())
    article = db.Column(db.Boolean())
    
    def __repr__(self):
        return '<Sitc Name %r:%r>' % (self.sitc_id, self.lang)