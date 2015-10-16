import sqlalchemy as sa
from sqlalchemy import orm

from neutron.db import model_base
from neutron.db import models_v2
from neutron.openstack.common import uuidutils

class PhysicalAttachmentPoint(model_base.BASEV2, models_v2.HasId, models_v2.HasTenant):

    __tablename__ = "physical_attachment_points"

    name = sa.Column(sa.String(255))
    hash_mod = sa.Column(sa.String(255))
    lacp_off = sa.Column(sa.Boolean)

class Interface(model_base.BASEV2, models_v2.HasId):

    host_name = sa.Column(sa.String(255))
    interface  = sa.Column(sa.String(255))
    pap_id = sa.Column(sa.String(36),
             sa.ForeignKey("physical_attachment_points.id", ondelete="CASCADE"),
             nullable=False)
    pap = orm.relationship(PhysicalAttachmentPoint, 
                           backref=orm.backref("interfaces", lazy="joined", cascade="all,delete"),
                           primaryjoin="PhysicalAttachmentPoint.id==Interface.pap_id")