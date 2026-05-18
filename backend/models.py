from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, ForeignKey, Enum
from sqlalchemy.orm import relationship
from database import Base
import enum
import uuid
from datetime import datetime

class UserRole(str, enum.Enum):
    USER = "user"
    ADMIN = "admin"

class OrderStatus(str, enum.Enum):
    PENDING = "pending"
    PREPARING = "preparing"
    READY = "ready"
    CANCELLED = "cancelled"

class User(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(String, default=UserRole.USER)
    orders = relationship("Order", back_populates="user")

class MenuItem(Base):
    __tablename__ = "menu_items"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=False)
    description = Column(String, default="")
    price = Column(Float, nullable=False)
    category = Column(String, default="Основное")
    is_available = Column(Boolean, default=True)

class TimeSlot(Base):
    __tablename__ = "time_slots"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    capacity = Column(Integer, default=20)
    booked_count = Column(Integer, default=0)
    orders = relationship("Order", back_populates="slot")

class Order(Base):
    __tablename__ = "orders"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, ForeignKey("users.id"), nullable=False)
    slot_id = Column(String, ForeignKey("time_slots.id"), nullable=False)
    status = Column(String, default=OrderStatus.PENDING)
    created_at = Column(DateTime, default=datetime.utcnow)
    user = relationship("User", back_populates="orders")
    slot = relationship("TimeSlot", back_populates="orders")
    items = relationship("OrderItem", back_populates="order")

class OrderItem(Base):
    __tablename__ = "order_items"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    order_id = Column(String, ForeignKey("orders.id"), nullable=False)
    menu_item_id = Column(String, ForeignKey("menu_items.id"), nullable=False)
    quantity = Column(Integer, default=1)
    price_snapshot = Column(Float, nullable=False)
    order = relationship("Order", back_populates="items")