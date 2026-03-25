from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
                            QPushButton, QLineEdit, QTableWidget, QTableWidgetItem,
                            QMessageBox, QStyle, QApplication, QFrame, QGroupBox, QComboBox,
                            QInputDialog, QHeaderView, QTabWidget, QTreeWidget, QTreeWidgetItem,
                            QStatusBar, QDialog, QMainWindow, QScrollArea, QFileDialog, QSizePolicy,
                            QTextEdit, QSplitter, QListWidget, QListWidgetItem, QCheckBox,
                            QDateEdit, QSpinBox, QProgressBar, QMenu, QAction, QGraphicsDropShadowEffect,
                            QAbstractItemView, QGridLayout, QDesktopWidget)
from PyQt5.QtCore import Qt, QDateTime, QDate, pyqtSignal, QTimer, QPropertyAnimation, QEasingCurve, QRect, QSize
from PyQt5.QtGui import QFont, QPalette, QColor, QPainter, QIcon, QPixmap, QDesktopServices, QLinearGradient, QCursor
import json
import os
import sys
import uuid
import time
from datetime import datetime
import logging
import shutil
from urllib.parse import urlparse
import subprocess
from pathlib import Path
import platform


class DesignSystem:
    """统一设计系统 - 现代扁平化风格
    
    遵循以下原则：
    1. 颜色统一：只使用定义好的颜色常量
    2. 圆角统一：按钮8px，卡片12px，输入框6px
    3. 间距统一：使用4px为基础单位
    4. 字体统一：只使用定义好的字体大小
    5. 无装饰：移除所有emoji，使用纯文字
    """
    
    # 浅色主题颜色
    LIGHT_COLORS = {
        'primary': '#007AFF',
        'primary_hover': '#0066D6',
        'primary_pressed': '#0055BB',
        'primary_light': '#E5F1FF',
        'primary_bg': 'rgba(0, 122, 255, 0.08)',
        
        'success': '#34C759',
        'success_hover': '#2DB84E',
        'success_pressed': '#28A745',
        'success_light': '#E8F8ED',
        
        'danger': '#FF3B30',
        'danger_hover': '#E6352B',
        'danger_pressed': '#CC2A26',
        'danger_light': '#FFEBEA',
        
        'warning': '#FF9500',
        'warning_hover': '#E68600',
        'warning_pressed': '#CC7700',
        'warning_light': '#FFF4E5',
        
        'info': '#5AC8FA',
        'info_hover': '#4AB8EA',
        'info_pressed': '#3AA8DA',
        'info_light': '#E8F7FD',
        
        'text_primary': '#1D1D1F',
        'text_secondary': '#86868B',
        'text_tertiary': '#AEAEB2',
        'text_disabled': '#C7C7CC',
        
        'background': '#F5F5F7',
        'surface': '#FFFFFF',
        'surface_hover': '#FAFAFA',
        'surface_pressed': '#F0F0F2',
        
        'border': 'rgba(0, 0, 0, 0.08)',
        'border_hover': 'rgba(0, 122, 255, 0.3)',
        'divider': 'rgba(0, 0, 0, 0.05)',
    }
    
    COLORS = LIGHT_COLORS
    
    RADIUS = {
        'sm': 6,
        'md': 8,
        'lg': 12,
        'xl': 16,
    }
    
    SPACING = {
        'xs': 4,
        'sm': 8,
        'md': 12,
        'lg': 16,
        'xl': 20,
        'xxl': 24,
    }
    
    FONT_SIZES = {
        'xs': 11,
        'sm': 12,
        'md': 13,
        'lg': 14,
        'xl': 16,
        'xxl': 18,
    }
    
    LINE_HEIGHTS = {
        'tight': 1.2,
        'normal': 1.4,
        'relaxed': 1.6,
    }
    
    SHADOWS = {
        'sm': '0 1px 2px rgba(0, 0, 0, 0.04)',
        'md': '0 2px 8px rgba(0, 0, 0, 0.06)',
        'lg': '0 4px 16px rgba(0, 0, 0, 0.08)',
    }
    
    @classmethod
    def button_style(cls, button_type='primary'):
        """获取按钮样式"""
        c = cls.COLORS
        r = cls.RADIUS['md']
        fs = cls.FONT_SIZES['lg']
        
        styles = {
            'primary': f"""
                QPushButton {{
                    background-color: {c['primary']};
                    color: white;
                    border: none;
                    border-radius: {r}px;
                    font-weight: 500;
                    padding: 10px 20px;
                    font-size: {fs}px;
                }}
                QPushButton:hover {{
                    background-color: {c['primary_hover']};
                }}
                QPushButton:pressed {{
                    background-color: {c['primary_pressed']};
                }}
                QPushButton:disabled {{
                    background-color: {c['text_disabled']};
                }}
            """,
            'secondary': f"""
                QPushButton {{
                    background-color: {c['surface']};
                    color: {c['text_primary']};
                    border: 1px solid {c['border']};
                    border-radius: {r}px;
                    font-weight: 500;
                    padding: 10px 20px;
                    font-size: {fs}px;
                }}
                QPushButton:hover {{
                    background-color: {c['surface_hover']};
                    border-color: {c['border_hover']};
                }}
                QPushButton:pressed {{
                    background-color: {c['surface_pressed']};
                }}
                QPushButton:disabled {{
                    background-color: {c['surface']};
                    color: {c['text_disabled']};
                }}
            """,
            'danger': f"""
                QPushButton {{
                    background-color: {c['danger']};
                    color: white;
                    border: none;
                    border-radius: {r}px;
                    font-weight: 500;
                    padding: 10px 20px;
                    font-size: {fs}px;
                }}
                QPushButton:hover {{
                    background-color: {c['danger_hover']};
                }}
                QPushButton:pressed {{
                    background-color: {c['danger_pressed']};
                }}
            """,
            'success': f"""
                QPushButton {{
                    background-color: {c['success']};
                    color: white;
                    border: none;
                    border-radius: {r}px;
                    font-weight: 500;
                    padding: 10px 20px;
                    font-size: {fs}px;
                }}
                QPushButton:hover {{
                    background-color: {c['success_hover']};
                }}
                QPushButton:pressed {{
                    background-color: {c['success_pressed']};
                }}
            """,
            'warning': f"""
                QPushButton {{
                    background-color: {c['warning']};
                    color: white;
                    border: none;
                    border-radius: {r}px;
                    font-weight: 500;
                    padding: 10px 20px;
                    font-size: {fs}px;
                }}
                QPushButton:hover {{
                    background-color: {c['warning_hover']};
                }}
                QPushButton:pressed {{
                    background-color: {c['warning_pressed']};
                }}
            """,
            'ghost': f"""
                QPushButton {{
                    background-color: transparent;
                    color: {c['primary']};
                    border: none;
                    border-radius: {r}px;
                    font-weight: 500;
                    padding: 10px 20px;
                    font-size: {fs}px;
                }}
                QPushButton:hover {{
                    background-color: {c['primary_bg']};
                }}
                QPushButton:pressed {{
                    background-color: {c['primary_light']};
                }}
            """,
        }
        return styles.get(button_type, styles['secondary'])
    
    @classmethod
    def card_style(cls):
        """获取卡片样式"""
        c = cls.COLORS
        r = cls.RADIUS['lg']
        return f"""
            background-color: {c['surface']};
            border: 1px solid {c['border']};
            border-radius: {r}px;
        """
    
    @classmethod
    def input_style(cls):
        """获取输入框样式"""
        c = cls.COLORS
        r = cls.RADIUS['sm']
        fs = cls.FONT_SIZES['lg']
        return f"""
            QLineEdit, QTextEdit, QComboBox {{
                background-color: {c['surface']};
                border: 1px solid {c['border']};
                border-radius: {r}px;
                padding: 8px 12px;
                font-size: {fs}px;
                color: {c['text_primary']};
            }}
            QLineEdit:focus, QTextEdit:focus, QComboBox:focus {{
                border-color: {c['primary']};
            }}
            QLineEdit:disabled, QTextEdit:disabled, QComboBox:disabled {{
                background-color: {c['surface_pressed']};
                color: {c['text_disabled']};
            }}
        """
    
    @classmethod
    def table_style(cls):
        """获取表格样式"""
        c = cls.COLORS
        r = cls.RADIUS['lg']
        return f"""
            QTableWidget {{
                background-color: {c['surface']};
                border: 1px solid {c['border']};
                border-radius: {r}px;
                gridline-color: {c['divider']};
                selection-background-color: {c['primary_bg']};
            }}
            QTableWidget::item {{
                padding: 12px 8px;
                border-bottom: 1px solid {c['divider']};
                color: {c['text_primary']};
            }}
            QTableWidget::item:selected {{
                background-color: {c['primary_light']};
                color: {c['primary']};
            }}
            QHeaderView::section {{
                background-color: {c['surface']};
                padding: 12px 8px;
                border: none;
                border-bottom: 1px solid {c['border']};
                font-weight: 600;
                color: {c['text_primary']};
                font-size: {cls.FONT_SIZES['md']}px;
            }}
            QHeaderView::section:hover {{
                background-color: {c['primary_bg']};
                color: {c['primary']};
            }}
        """
    
    @classmethod
    def tree_style(cls):
        """获取树形控件样式"""
        c = cls.COLORS
        r = cls.RADIUS['lg']
        return f"""
            QTreeWidget {{
                background-color: {c['surface']};
                border: 1px solid {c['border']};
                border-radius: {r}px;
                color: {c['text_primary']};
            }}
            QTreeWidget::item {{
                padding: 8px 4px;
                border-bottom: 1px solid {c['divider']};
                border-radius: {cls.RADIUS['sm']}px;
                color: {c['text_primary']};
            }}
            QTreeWidget::item:hover {{
                background-color: {c['primary_bg']};
            }}
            QTreeWidget::item:selected {{
                background-color: {c['primary_light']};
                color: {c['primary']};
            }}
        """
    
    @classmethod
    def list_style(cls):
        """获取列表控件样式"""
        c = cls.COLORS
        r = cls.RADIUS['md']
        return f"""
            QListWidget {{
                border: 1px solid {c['border']};
                border-radius: {r}px;
                background-color: {c['surface']};
                padding: 8px;
                font-size: {cls.FONT_SIZES['lg']}px;
            }}
            QListWidget::item {{
                padding: 8px;
                border-radius: {cls.RADIUS['sm']}px;
                margin: 2px 0;
            }}
            QListWidget::item:selected {{
                background-color: {c['primary_light']};
                color: {c['primary']};
            }}
            QListWidget::item:hover {{
                background-color: {c['primary_bg']};
            }}
        """
    
    @classmethod
    def tab_style(cls):
        """获取选项卡样式"""
        c = cls.COLORS
        r = cls.RADIUS['lg']
        return f"""
            QTabWidget::pane {{
                border: none;
                border-radius: {r}px;
                background-color: {c['surface']};
            }}
            QTabWidget::tab-bar {{
                alignment: center;
            }}
            QTabBar::tab {{
                background-color: transparent;
                border: none;
                padding: 10px 24px;
                margin-right: 4px;
                font-weight: 500;
                color: {c['text_secondary']};
                font-size: {cls.FONT_SIZES['lg']}px;
            }}
            QTabBar::tab:selected {{
                background-color: {c['primary_bg']};
                color: {c['primary']};
                border-radius: {cls.RADIUS['sm']}px;
            }}
            QTabBar::tab:hover:!selected {{
                background-color: {c['divider']};
                border-radius: {cls.RADIUS['sm']}px;
            }}
        """
    
    @classmethod
    def menu_style(cls):
        """获取菜单样式"""
        c = cls.COLORS
        return f"""
            QMenuBar {{
                background-color: {c['surface']};
                border-bottom: 1px solid {c['border']};
                color: {c['text_primary']};
                font-size: {cls.FONT_SIZES['lg']}px;
                padding: 4px;
            }}
            QMenuBar::item {{
                background-color: transparent;
                padding: 6px 12px;
                border-radius: {cls.RADIUS['sm']}px;
            }}
            QMenuBar::item:selected {{
                background-color: {c['primary_bg']};
                color: {c['primary']};
            }}
            QMenu {{
                background-color: {c['surface']};
                border: 1px solid {c['border']};
                border-radius: {cls.RADIUS['md']}px;
                padding: 4px 0;
            }}
            QMenu::item {{
                padding: 8px 16px;
                color: {c['text_primary']};
                border-radius: {cls.RADIUS['sm']}px;
                margin: 2px 4px;
            }}
            QMenu::item:selected {{
                background-color: {c['primary_bg']};
                color: {c['primary']};
            }}
        """
    
    @classmethod
    def status_bar_style(cls):
        """获取状态栏样式"""
        c = cls.COLORS
        return f"""
            QStatusBar {{
                background-color: {c['surface']};
                border-top: 1px solid {c['border']};
                color: {c['text_secondary']};
                font-size: {cls.FONT_SIZES['sm']}px;
                padding: 4px 12px;
            }}
        """
    
    @classmethod
    def label_style(cls, label_type='default'):
        """获取标签样式"""
        c = cls.COLORS
        styles = {
            'default': f"color: {c['text_primary']};",
            'secondary': f"color: {c['text_secondary']};",
            'tertiary': f"color: {c['text_tertiary']};",
            'title': f"color: {c['text_primary']}; font-weight: 600; font-size: {cls.FONT_SIZES['xl']}px;",
            'subtitle': f"color: {c['text_secondary']}; font-size: {cls.FONT_SIZES['md']}px;",
            'tag': f"""
                background-color: {c['primary_bg']};
                color: {c['primary']};
                padding: 4px 10px;
                border-radius: {cls.RADIUS['sm']}px;
                font-size: {cls.FONT_SIZES['sm']}px;
                font-weight: 500;
            """,
            'success_tag': f"""
                background-color: {c['success_light']};
                color: {c['success']};
                padding: 4px 10px;
                border-radius: {cls.RADIUS['sm']}px;
                font-size: {cls.FONT_SIZES['sm']}px;
                font-weight: 500;
            """,
            'danger_tag': f"""
                background-color: {c['danger_light']};
                color: {c['danger']};
                padding: 4px 10px;
                border-radius: {cls.RADIUS['sm']}px;
                font-size: {cls.FONT_SIZES['sm']}px;
                font-weight: 500;
            """,
        }
        return styles.get(label_type, styles['default'])
    
    @classmethod
    def dialog_style(cls):
        """获取对话框样式"""
        c = cls.COLORS
        return f"""
            QDialog {{
                background-color: {c['background']};
            }}
        """
    
    @classmethod
    def table_action_button_style(cls, button_type='default'):
        """获取表格操作按钮样式
        
        统一的表格操作按钮样式，只使用三种颜色：
        - primary: 主要操作（编辑、查看）
        - danger: 危险操作（删除）
        - default: 次要操作（添加资源等）
        """
        c = cls.COLORS
        r = cls.RADIUS['sm']
        
        styles = {
            'primary': f"""
                QPushButton {{
                    background-color: {c['primary']};
                    color: white;
                    border: none;
                    border-radius: {r}px;
                    padding: 4px 8px;
                    font-size: {cls.FONT_SIZES['xs']}px;
                    font-weight: 500;
                    min-width: 40px;
                    max-height: 22px;
                }}
                QPushButton:hover {{
                    background-color: {c['primary_hover']};
                }}
                QPushButton:pressed {{
                    background-color: {c['primary_pressed']};
                }}
            """,
            'danger': f"""
                QPushButton {{
                    background-color: {c['danger']};
                    color: white;
                    border: none;
                    border-radius: {r}px;
                    padding: 4px 8px;
                    font-size: {cls.FONT_SIZES['xs']}px;
                    font-weight: 500;
                    min-width: 40px;
                    max-height: 22px;
                }}
                QPushButton:hover {{
                    background-color: {c['danger_hover']};
                }}
                QPushButton:pressed {{
                    background-color: {c['danger_pressed']};
                }}
            """,
            'default': f"""
                QPushButton {{
                    background-color: {c['text_secondary']};
                    color: white;
                    border: none;
                    border-radius: {r}px;
                    padding: 4px 8px;
                    font-size: {cls.FONT_SIZES['xs']}px;
                    font-weight: 500;
                    min-width: 40px;
                    max-height: 22px;
                }}
                QPushButton:hover {{
                    background-color: {c['text_primary']};
                }}
                QPushButton:pressed {{
                    background-color: {c['text_primary']};
                }}
            """,
        }
        return styles.get(button_type, styles['default'])
    
    @classmethod
    def dateedit_style(cls):
        """获取日期选择器样式"""
        c = cls.COLORS
        r = cls.RADIUS['md']
        fs = cls.FONT_SIZES['lg']
        return f"""
            QDateEdit {{
                border: 1px solid {c['border']};
                border-radius: {r}px;
                padding: 8px 12px;
                background-color: {c['surface']};
                font-size: {fs}px;
                color: {c['text_primary']};
                font-weight: 500;
            }}
            QDateEdit:hover {{
                border-color: {c['border_hover']};
                background-color: {c['surface_hover']};
            }}
            QDateEdit:focus {{
                border: 2px solid {c['primary']};
                background-color: {c['surface_hover']};
                outline: none;
            }}
            QDateEdit::drop-down {{
                subcontrol-origin: padding;
                subcontrol-position: center right;
                width: 24px;
                border: none;
                background: transparent;
            }}
            QDateEdit::down-arrow {{
                width: 14px;
                height: 14px;
                background: {c['text_secondary']};
            }}
        """


def is_mac():
    """检测当前是否为macOS系统"""
    return platform.system() == "Darwin"


def is_windows():
    """检测当前是否为Windows系统"""
    return platform.system() == "Windows"


def is_linux():
    """检测当前是否为Linux系统"""
    return platform.system() == "Linux"


def get_optimal_window_size():
    """根据屏幕分辨率动态计算最佳窗口尺寸
    
    返回:
        tuple: (width, height) 窗口宽度和高度
    """
    screen = QDesktopWidget().screenGeometry()
    screen_width = screen.width()
    screen_height = screen.height()
    
    width = int(screen_width * 0.65)
    height = int(screen_height * 0.75)
    
    return width, height


def get_optimal_dialog_size(base_width=500, base_height=400):
    """根据屏幕分辨率计算对话框最佳尺寸
    
    Args:
        base_width: 基础宽度，默认 500px
        base_height: 基础高度，默认 400px
        
    Returns:
        tuple: (width, height) 对话框宽度和高度
    """
    screen = QDesktopWidget().screenGeometry()
    
    max_width = int(screen.width() * 0.6)
    max_height = int(screen.height() * 0.7)
    
    min_width = 350
    min_height = 250
    
    width = min(max_width, max(min_width, base_width))
    height = min(max_height, max(min_height, base_height))
    
    return width, height


def center_window(window):
    """将窗口移动到屏幕中央（考虑任务栏）
    
    Args:
        window: QWidget 或 QDialog 实例
    """
    available_geometry = QDesktopWidget().availableGeometry()
    
    x = (available_geometry.width() - window.width()) // 2 + available_geometry.x()
    y = (available_geometry.height() - window.height()) // 2 + available_geometry.y()
    
    window.move(x, y)


def get_system_font(fallback_size=10):
    """获取适合当前系统的字体
    
    Args:
        fallback_size: 默认字体大小
        
    Returns:
        QFont: 适合当前系统的字体
    """
    font = QFont()
    
    if is_mac():
        font.setFamily("SF Pro Text")
    elif is_windows():
        font.setFamily("Segoe UI")
    else:
        font.setFamily("Ubuntu")
    
    font.setPointSize(fallback_size)
    return font

class PromptListItemWidget(QWidget):
    """提示词列表项小部件，包含提示词文本和复制按钮"""
    def __init__(self, prompt_text, parent=None):
        super().__init__(parent)
        self.prompt_text = prompt_text
        self.init_ui()
    
    def init_ui(self):
        layout = QHBoxLayout(self)
        s = DesignSystem.SPACING
        layout.setContentsMargins(s['sm'], s['sm'], s['sm'], s['sm'])
        layout.setSpacing(s['md'])
        
        # 提示词文本
        self.text_label = QLabel(self.prompt_text)
        self.text_label.setWordWrap(True)
        self.text_label.setStyleSheet(DesignSystem.label_style('default'))
        layout.addWidget(self.text_label, 1)  # 占据大部分空间
        
        # 复制按钮
        self.copy_button = ModernButton("复制", "secondary")
        self.copy_button.setFixedSize(80, 32)
        self.copy_button.clicked.connect(self.copy_to_clipboard)
        layout.addWidget(self.copy_button)
        
        # 设置初始高度
        self.setMinimumHeight(40)
        
        # 使用定时器在组件显示后调整高度
        QTimer.singleShot(100, self.adjust_widget_height)
    
    def adjust_widget_height(self):
        """根据文本内容调整组件高度"""
        # 使用QTextDocument来更准确地计算文本所需的高度
        from PyQt5.QtGui import QTextDocument
        
        # 创建一个临时的QTextDocument来计算文本高度
        doc = QTextDocument()
        doc.setDefaultFont(self.text_label.font())
        doc.setPlainText(self.prompt_text)
        
        # 获取可用宽度（组件宽度减去按钮和边距）
        available_width = self.width() - 80 - 20  # 减去按钮宽度和边距
        if available_width <= 0:
            available_width = 400  # 默认宽度
        
        # 设置文本宽度并计算所需高度
        doc.setTextWidth(available_width)
        text_height = doc.size().height()
        
        # 组件高度 = 文本高度 + 上下边距
        widget_height = int(text_height) + 10
        # 确保最小高度不小于按钮高度
        widget_height = max(widget_height, 40)
        
        # 设置组件的最小高度和推荐高度
        self.setMinimumHeight(widget_height)
        self.resize(self.width(), widget_height)
    
    def resizeEvent(self, event):
        """重写大小调整事件，在组件大小改变时重新计算高度"""
        super().resizeEvent(event)
        # 在组件大小改变后，重新调整高度
        self.adjust_widget_height()
        # 确保父列表项的大小也更新
        if self.parent() and hasattr(self.parent(), 'quick_launch_list'):
            # 找到包含此小部件的列表项
            for i in range(self.parent().quick_launch_list.count()):
                item = self.parent().quick_launch_list.item(i)
                if item and self.parent().quick_launch_list.itemWidget(item) == self:
                    item.setSizeHint(self.sizeHint())
                    break
    
    def copy_to_clipboard(self):
        """复制提示词到剪贴板"""
        clipboard = QApplication.clipboard()
        # 只复制提示词内容，不包括场景和备注
        lines = self.prompt_text.split('\n')
        for line in lines:
            if line.startswith('[') and ']' in line:
                # 找到场景行，提取提示词内容
                prompt_content = line.split('] ', 1)[1] if '] ' in line else line
                clipboard.setText(prompt_content)
                break
        else:
            # 如果没有找到场景格式，直接复制全部内容
            clipboard.setText(self.prompt_text)
        
        # 显示复制成功提示
        self.copy_button.setText("✓ 已复制")
        c = DesignSystem.COLORS
        self.copy_button.setStyleSheet(f"""
            QPushButton {{
                background-color: {c['success']};
                border: 1px solid {c['success_hover']};
                border-radius: {DesignSystem.RADIUS['sm']}px;
                font-size: {DesignSystem.FONT_SIZES['sm']}px;
                color: white;
                padding: 2px 4px;
            }}
        """)
        
        # 2秒后恢复按钮状态
        QTimer.singleShot(2000, self.reset_button)
    
    def reset_button(self):
        """重置按钮状态"""
        self.copy_button.setText("📋 复制")
        c = DesignSystem.COLORS
        self.copy_button.setStyleSheet(f"""
            QPushButton {{
                background-color: {c['surface_pressed']};
                border: 1px solid {c['border']};
                border-radius: {DesignSystem.RADIUS['sm']}px;
                font-size: {DesignSystem.FONT_SIZES['sm']}px;
                color: {c['text_primary']};
                padding: 2px 4px;
            }}
            QPushButton:hover {{
                background-color: {c['surface_hover']};
                border-color: {c['border_hover']};
            }}
            QPushButton:pressed {{
                background-color: {c['surface_pressed']};
            }}
        """)
    
    def update_text(self, text):
        """更新提示词文本"""
        self.prompt_text = text
        self.text_label.setText(text)
        # 更新文本后重新调整组件高度
        self.adjust_widget_height()

class BoundPromptCardWidget(QWidget):
    """已绑定提示词卡片小部件，用于IA资源页面显示绑定的提示词"""
    def __init__(self, resource_data, parent=None, parent_tool=None):
        super().__init__(parent)
        self.resource_data = resource_data
        self.parent_tool = parent_tool  # 保存父工具引用，用于状态栏消息
        self.init_ui()
    
    def init_ui(self):
        # 设置卡片最小宽度和高度，允许根据内容自适应
        self.setMinimumWidth(380)
        self.setMinimumHeight(140)
        self.setMaximumHeight(180)  # 设置最大高度，防止过高
        
        # 苹果风格的卡片样式
        self.setStyleSheet("""
            BoundPromptCardWidget {
                background-color: white;
                border: 1px solid rgba(0, 0, 0, 0.08);
                border-radius: 12px;
                margin: 6px;
            }
            BoundPromptCardWidget:hover {
                background-color: rgba(0, 0, 0, 0.02);
                border-color: rgba(0, 122, 255, 0.3);
            }
        """)
        
        # 主布局
        layout = QVBoxLayout(self)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(10)
        
        # 顶部区域：场景标签和复制按钮
        top_layout = QHBoxLayout()
        top_layout.setContentsMargins(0, 0, 0, 0)
        top_layout.setSpacing(8)
        
        # 场景标签 - 苹果风格
        scene = self.resource_data.get('scene', '未分类')
        scene_label = QLabel(scene)
        scene_label.setStyleSheet("""
            QLabel {
                background-color: rgba(0, 122, 255, 0.9);
                color: white;
                padding: 4px 10px;
                border-radius: 6px;
                font-size: 12px;
                font-weight: 500;
            }
        """)
        top_layout.addWidget(scene_label)
        
        # 添加弹性空间
        top_layout.addStretch()
        
        # 复制按钮 - 苹果风格，使用图标
        copy_button = QPushButton()
        copy_button.setIcon(self.style().standardIcon(QStyle.SP_FileDialogDetailedView))
        copy_button.setIconSize(QSize(16, 16))
        copy_button.setFixedSize(32, 32)
        copy_button.setToolTip("复制提示词")
        copy_button.setStyleSheet("""
            QPushButton {
                background-color: rgba(0, 122, 255, 0.9);
                border: none;
                border-radius: 6px;
            }
            QPushButton:hover {
                background-color: rgba(0, 122, 255, 1.0);
            }
            QPushButton:pressed {
                background-color: rgba(0, 122, 255, 0.8);
            }
        """)
        copy_button.clicked.connect(self.copy_to_clipboard)
        top_layout.addWidget(copy_button)
        
        layout.addLayout(top_layout)
        
        # 中间区域：标题（截断的提示词内容）
        prompt_text = self.resource_data.get('prompt', '')
        title_text = prompt_text[:80] + "..." if len(prompt_text) > 80 else prompt_text
        title_label = QLabel(title_text)
        title_label.setWordWrap(True)
        title_label.setMinimumHeight(40)  # 确保有足够空间显示文本
        c = DesignSystem.COLORS
        title_label.setStyleSheet(f"""
            QLabel {{
                color: {c['text_primary']};
                font-size: 12px;
                font-weight: 400;
                line-height: {DesignSystem.LINE_HEIGHTS['normal']};
            }}
        """)
        layout.addWidget(title_label)
        
        # 底部区域：只显示绑定时间，不显示备注
        bottom_layout = QVBoxLayout()
        bottom_layout.setContentsMargins(0, 0, 0, 0)
        bottom_layout.setSpacing(4)
        
        # 绑定时间
        bind_time = self.resource_data.get('bind_time', '')
        if bind_time:
            # 尝试格式化时间显示
            try:
                # 如果是ISO格式，只显示日期部分
                if 'T' in bind_time:
                    formatted_time = bind_time.split('T')[0]
                else:
                    formatted_time = bind_time
                
                time_label = QLabel(f"绑定于 {formatted_time}")
                c = DesignSystem.COLORS
                time_label.setStyleSheet(f"""
                    QLabel {{
                        color: {c['text_secondary']};
                        font-size: 11px;
                    }}
                """)
                bottom_layout.addWidget(time_label)
            except:
                pass  # 如果时间格式有问题，不显示时间标签
        
        layout.addLayout(bottom_layout)
    
    def mouseDoubleClickEvent(self, event):
        """双击事件：显示完整内容对话框"""
        self.show_full_content_dialog()
        super().mouseDoubleClickEvent(event)
    
    def show_full_content_dialog(self):
        """显示完整内容对话框"""
        dialog = QDialog(self)
        dialog.setWindowTitle("提示词完整内容")
        dialog.setModal(True)
        width, height = get_optimal_dialog_size(600, 500)
        dialog.resize(width, height)
        center_window(dialog)
        
        # 设置苹果风格的背景
        c = DesignSystem.COLORS
        dialog.setStyleSheet(f"""
            QDialog {{
                background-color: {c['background']};
            }}
        """)
        
        layout = QVBoxLayout(dialog)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(16)
        
        # 场景标签 - 苹果风格
        scene = self.resource_data.get('scene', '未分类')
        scene_label = QLabel(f"场景: {scene}")
        c = DesignSystem.COLORS
        scene_label.setStyleSheet(f"""
            QLabel {{
                background-color: {c['primary']};
                color: white;
                padding: 6px 12px;
                border-radius: {DesignSystem.RADIUS['md']}px;
                font-size: {DesignSystem.FONT_SIZES['lg']}px;
                font-weight: 500;
            }}
        """)
        layout.addWidget(scene_label)
        
        # 提示词内容标题
        prompt_label = QLabel("提示词正文如下:")
        c = DesignSystem.COLORS
        prompt_label.setStyleSheet(f"""
            QLabel {{
                font-size: {DesignSystem.FONT_SIZES['lg']}px;
                font-weight: 600;
                color: {c['text_primary']};
                margin-bottom: 4px;
            }}
        """)
        layout.addWidget(prompt_label)
        
        # 提示词内容文本框
        prompt_text = QTextEdit()
        prompt_text.setPlainText(self.resource_data.get('prompt', ''))
        prompt_text.setReadOnly(True)
        prompt_text.setMinimumHeight(120)
        prompt_text.setStyleSheet("""
            QTextEdit {
                border: 1px solid rgba(0, 0, 0, 0.1);
                border-radius: 8px;
                padding: 12px;
                font-size: 12px;
                background-color: white;
                line-height: 1.5;
            }
        """)
        layout.addWidget(prompt_text)
        
        # 备注 - 可编辑
        remark = self.resource_data.get('remark', '')
        remark_title = QLabel("备注:")
        c = DesignSystem.COLORS
        remark_title.setStyleSheet(f"""
            QLabel {{
                font-size: {DesignSystem.FONT_SIZES['lg']}px;
                font-weight: 600;
                color: {c['text_primary']};
                margin-top: 8px;
                margin-bottom: 4px;
            }}
        """)
        layout.addWidget(remark_title)
        
        remark_text = QTextEdit()
        remark_text.setPlainText(remark)
        remark_text.setMaximumHeight(80)
        remark_text.setStyleSheet("""
            QTextEdit {
                border: 1px solid rgba(0, 0, 0, 0.1);
                border-radius: 8px;
                padding: 12px;
                font-size: 13px;
                background-color: white;
                line-height: 1.4;
            }
            QTextEdit:focus {
                border: 2px solid rgba(0, 122, 255, 0.7);
            }
        """)
        layout.addWidget(remark_text)
        
        # 绑定时间
        bind_time = self.resource_data.get('bind_time', '')
        if bind_time:
            time_label = QLabel(f"绑定时间: {bind_time}")
            time_label.setStyleSheet("""
                QLabel {
                    color: #86868b;
                    font-size: 12px;
                    margin-top: 8px;
                }
            """)
            layout.addWidget(time_label)
        
        # 按钮区域
        button_layout = QHBoxLayout()
        button_layout.setContentsMargins(0, 16, 0, 0)
        
        # 复制按钮 - 苹果风格，使用图标
        copy_button = QPushButton()
        copy_button.setIcon(self.style().standardIcon(QStyle.SP_FileDialogDetailedView))
        copy_button.setIconSize(QSize(18, 18))
        copy_button.setFixedSize(36, 36)
        copy_button.setToolTip("复制提示词")
        copy_button.setStyleSheet("""
            QPushButton {
                background-color: rgba(0, 122, 255, 0.9);
                border: none;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: rgba(0, 122, 255, 1.0);
            }
            QPushButton:pressed {
                background-color: rgba(0, 122, 255, 0.8);
            }
        """)
        copy_button.clicked.connect(lambda: self.copy_to_clipboard())
        button_layout.addWidget(copy_button)
        
        button_layout.addStretch()
        
        # 保存备注按钮
        save_button = QPushButton("保存备注")
        save_button.setStyleSheet("""
            QPushButton {
                background-color: rgba(52, 199, 89, 0.9);
                color: white;
                border: none;
                border-radius: 8px;
                padding: 8px 16px;
                font-size: 14px;
                font-weight: 500;
            }
            QPushButton:hover {
                background-color: rgba(52, 199, 89, 1.0);
            }
            QPushButton:pressed {
                background-color: rgba(52, 199, 89, 0.8);
            }
        """)
        save_button.clicked.connect(lambda: self.save_remark(remark_text.toPlainText(), dialog))
        button_layout.addWidget(save_button)
        
        # 关闭按钮
        close_button = QPushButton("关闭")
        close_button.setStyleSheet("""
            QPushButton {
                background-color: rgba(142, 142, 147, 0.9);
                color: white;
                border: none;
                border-radius: 8px;
                padding: 8px 16px;
                font-size: 14px;
                font-weight: 500;
            }
            QPushButton:hover {
                background-color: rgba(142, 142, 147, 1.0);
            }
            QPushButton:pressed {
                background-color: rgba(142, 142, 147, 0.8);
            }
        """)
        close_button.clicked.connect(dialog.accept)
        button_layout.addWidget(close_button)
        
        layout.addLayout(button_layout)
        
        # 显示对话框
        dialog.exec_()
    
    def save_remark(self, new_remark, dialog):
        """保存备注到数据文件"""
        try:
            # 获取资源ID
            resource_id = self.resource_data.get('id')
            if not resource_id:
                # 使用状态栏显示错误消息
                self.parent_tool.status_bar.showMessage("❌ 无法获取资源ID，保存失败", 5000)
                return
            
            # 读取当前数据文件
            if getattr(sys, 'frozen', False):
                # 是打包后的exe
                app_dir = os.path.dirname(sys.executable)
            else:
                # 如果是开发环境
                app_dir = os.path.dirname(os.path.abspath(__file__))
            
            data_dir = os.path.join(app_dir, 'data')
            data_file = os.path.join(data_dir, 'knowledge_manager_data.json')
            
            if not os.path.exists(data_file):
                # 使用状态栏显示错误消息
                self.parent_tool.status_bar.showMessage("❌ 数据文件不存在", 5000)
                return
            
            with open(data_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # 找到并更新对应资源的备注
            found = False
            # 遍历所有项目
            for project in data.get('content', {}).get('projects', []):
                # 在项目的ia_resources中查找
                for resource in project.get('ia_resources', []):
                    if resource.get('id') == resource_id:
                        resource['remark'] = new_remark
                        found = True
                        break
                if found:
                    break
            
            if not found:
                # 使用状态栏显示错误消息
                self.parent_tool.status_bar.showMessage("❌ 未找到对应的资源", 5000)
                return
            
            # 保存更新后的数据
            with open(data_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            
            # 更新当前对象的resource_data
            self.resource_data['remark'] = new_remark
            
            # 使用状态栏显示成功消息
            self.parent_tool.status_bar.showMessage("✅ 备注已保存", 3000)
            
            # 关闭对话框
            dialog.accept()
            
        except Exception as e:
            # 使用状态栏显示错误消息
            self.parent_tool.status_bar.showMessage(f"❌ 保存备注时发生错误: {str(e)}", 5000)
    
    def copy_to_clipboard(self):
        """复制提示词到剪贴板"""
        clipboard = QApplication.clipboard()
        prompt_text = self.resource_data.get('prompt', '')
        clipboard.setText(prompt_text)
        
        # 使用状态栏显示复制成功提示
        self.parent_tool.status_bar.showMessage("✅ 提示词已复制到剪贴板", 3000)


class ModernPromptListItemWidget(QWidget):
    """现代化提示词对话框列表项小部件，用于提示词选择对话框"""
    def __init__(self, prompt_id, prompt_data, parent=None):
        super().__init__(parent)
        self.prompt_id = prompt_id
        self.prompt_data = prompt_data
        self.init_ui()
    
    def init_ui(self):
        # 设置整体布局 - 增加边距确保内容不会超出
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(16, 16, 16, 16)  # 增加上下边距
        self.main_layout.setSpacing(12)  # 增加各元素之间的间距
        
        # 设置卡片式背景
        c = DesignSystem.COLORS
        self.setStyleSheet(f"""
            ModernPromptListItemWidget {{
                background-color: {c['surface']};
                border: 1px solid {c['border']};
                border-radius: {DesignSystem.RADIUS['md']}px;
                margin: 2px;
            }}
            ModernPromptListItemWidget:hover {{
                background-color: {c['surface_hover']};
                border-color: {c['primary']};
                box-shadow: {DesignSystem.SHADOWS['md']};
            }}
        """)
        
        # 顶部区域：场景标签和ID
        top_layout = QHBoxLayout()
        top_layout.setContentsMargins(0, 0, 0, 0)
        top_layout.setSpacing(8)
        
        # 场景标签
        scene = self.prompt_data.get('scene', '未分类')
        self.scene_label = QLabel(scene)
        c = DesignSystem.COLORS
        self.scene_label.setStyleSheet(f"""
            QLabel {{
                background-color: {c['primary']};
                color: white;
                padding: 4px 8px;
                border-radius: {DesignSystem.RADIUS['sm']}px;
                font-size: {DesignSystem.FONT_SIZES['sm']}px;
                font-weight: bold;
            }}
        """)
        top_layout.addWidget(self.scene_label)
        
        # ID标签（较小，次要信息）
        id_text = f"ID: {self.prompt_id[:8]}..." if len(self.prompt_id) > 8 else f"ID: {self.prompt_id}"
        self.id_label = QLabel(id_text)
        c = DesignSystem.COLORS
        self.id_label.setStyleSheet(f"""
            QLabel {{
                color: {c['text_secondary']};
                font-size: 10px;
                font-style: italic;
            }}
        """)
        top_layout.addWidget(self.id_label)
        
        # 添加弹性空间
        top_layout.addStretch()
        
        # 添加到主布局
        self.main_layout.addLayout(top_layout)
        
        # 中间区域：提示词内容
        self.prompt_text = self.prompt_data.get('prompt', '')
        self.text_label = QLabel(self.prompt_text)
        self.text_label.setWordWrap(True)
        self.text_label.setTextFormat(Qt.PlainText)
        self.text_label.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.text_label.setStyleSheet(f"""
            QLabel {{
                color: {c['text_primary']};
                font-size: 15px;
                line-height: {DesignSystem.LINE_HEIGHTS['normal']};
                padding: 8px 0;
                background-color: transparent;
            }}
        """)
        # 设置文本标签的最小高度，确保有足够空间显示内容
        self.text_label.setMinimumHeight(40)
        self.main_layout.addWidget(self.text_label)
        
        # 底部区域：元数据
        bottom_layout = QHBoxLayout()
        bottom_layout.setContentsMargins(0, 0, 0, 0)
        bottom_layout.setSpacing(16)
        
        # 如果有其他元数据，可以在这里添加
        # 例如：创建时间、使用次数等
        
        # 添加弹性空间
        bottom_layout.addStretch()
        
        # 添加到主布局
        self.main_layout.addLayout(bottom_layout)
        
        # 设置初始高度 - 增加最小高度确保内容不会超出
        self.setMinimumHeight(90)
        
        # 使用定时器在组件显示后调整高度
        QTimer.singleShot(100, self.adjust_widget_height)
    
    def adjust_widget_height(self):
        """根据文本内容调整组件高度"""
        # 使用QTextDocument来更准确地计算文本所需的高度
        from PyQt5.QtGui import QTextDocument
        
        # 创建一个临时的QTextDocument来计算文本高度
        doc = QTextDocument()
        doc.setDefaultFont(self.text_label.font())
        doc.setPlainText(self.prompt_text)
        
        # 获取可用宽度（组件宽度减去边距）
        available_width = self.width() - 32  # 减去左右边距
        if available_width <= 0:
            available_width = 500  # 默认宽度
        
        # 设置文本宽度并计算所需高度
        doc.setTextWidth(available_width)
        text_height = doc.size().height()
        
        # 计算组件总高度 - 增加额外的边距确保文字不会超出
        # 顶部区域高度 + 文本高度 + 底部区域高度 + 边距 + 额外缓冲
        top_height = 30  # 场景标签和ID的高度（增加一些空间）
        bottom_height = 10  # 底部区域的高度
        margins = 32  # 上下边距（16+16）
        spacing = 24  # 各区域之间的间距（12+12）
        extra_padding = 15  # 额外的底部缓冲，确保文字不会超出
        
        widget_height = int(text_height) + top_height + bottom_height + margins + spacing + extra_padding
        # 确保最小高度
        widget_height = max(widget_height, 90)  # 增加最小高度
        
        # 设置组件的最小高度和推荐高度
        self.setMinimumHeight(widget_height)
        self.resize(self.width(), widget_height)
    
    def resizeEvent(self, event):
        """重写大小调整事件，在组件大小改变时重新计算高度"""
        super().resizeEvent(event)
        # 在组件大小改变后，重新调整高度
        self.adjust_widget_height()


class ModernQuickLaunchListItemWidget(QWidget):
    """现代化快速启动项对话框列表项小部件，用于快速启动项选择对话框"""
    def __init__(self, launch_id, launch_data, parent=None):
        super().__init__(parent)
        self.launch_id = launch_id
        self.launch_data = launch_data
        self.is_selected = False
        self.init_ui()
    
    def init_ui(self):
        # 设置整体布局
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(16, 12, 16, 12)
        self.main_layout.setSpacing(8)
        
        # 设置卡片式背景
        self.update_style()
        
        # 顶部区域：类型标签和ID
        top_layout = QHBoxLayout()
        top_layout.setContentsMargins(0, 0, 0, 0)
        top_layout.setSpacing(8)
        
        # 类型标签 - 使用亮色块样式
        launch_type = self.launch_data.get('type', '未分类')
        self.type_label = QLabel(launch_type)
        
        # 根据类型设置不同的颜色主题（使用 DesignSystem 颜色）
        c = DesignSystem.COLORS
        type_colors = {
            'URL': {'bg': c['primary'], 'text': '#ffffff'},
            '文件': {'bg': c['danger'], 'text': '#ffffff'},
            '文件夹': {'bg': c['warning'], 'text': '#ffffff'},
            '文档': {'bg': c['info'], 'text': '#ffffff'},
            '思维导图': {'bg': c['success'], 'text': '#ffffff'},
            '图片': {'bg': c['warning'], 'text': '#ffffff'},
            '媒体': {'bg': c['warning'], 'text': '#ffffff'},
            '压缩包': {'bg': c['text_primary'], 'text': '#ffffff'},
            '代码': {'bg': c['text_primary'], 'text': '#ffffff'},
            '未分类': {'bg': c['text_secondary'], 'text': '#ffffff'}
        }
        
        colors = type_colors.get(launch_type, type_colors['未分类'])
        
        self.type_label.setStyleSheet(f"""
            QLabel {{
                background-color: {colors['bg']};
                color: {colors['text']};
                padding: 4px 12px;
                border-radius: {DesignSystem.RADIUS['lg']}px;
                font-size: {DesignSystem.FONT_SIZES['sm']}px;
                font-weight: bold;
                border: 1px solid {colors['bg']};
                box-shadow: {DesignSystem.SHADOWS['md']};
            }}
        """)
        top_layout.addWidget(self.type_label)
        
        # ID标签（较小，次要信息）
        id_text = f"ID: {self.launch_id[:8]}..." if len(self.launch_id) > 8 else f"ID: {self.launch_id}"
        self.id_label = QLabel(id_text)
        c = DesignSystem.COLORS
        self.id_label.setStyleSheet(f"""
            QLabel {{
                color: {c['text_secondary']};
                font-size: 10px;
                font-style: italic;
            }}
        """)
        top_layout.addWidget(self.id_label)
        
        # 添加弹性空间
        top_layout.addStretch()
        
        # 添加到主布局
        self.main_layout.addLayout(top_layout)
        
        # 中间区域：启动项名称和描述
        name_text = self.launch_id
        self.name_label = QLabel(name_text)
        self.name_label.setWordWrap(True)
        self.name_label.setTextFormat(Qt.PlainText)
        self.name_label.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        # 设置字体，确保与样式表一致
        from PyQt5.QtGui import QFont
        name_font = QFont()
        name_font.setPointSize(12)
        name_font.setBold(True)
        self.name_label.setFont(name_font)
        c = DesignSystem.COLORS
        self.name_label.setStyleSheet(f"""
            QLabel {{
                color: {c['text_primary']};
                font-size: 12px;
                font-weight: bold;
                line-height: {DesignSystem.LINE_HEIGHTS['normal']};
                padding: 4px 0;
            }}
        """)
        self.main_layout.addWidget(self.name_label)
        
        # 描述文本
        description_text = self.launch_data.get('description', '')
        if description_text:
            self.desc_label = QLabel(description_text)
            self.desc_label.setWordWrap(True)
            self.desc_label.setTextFormat(Qt.PlainText)
            self.desc_label.setAlignment(Qt.AlignLeft | Qt.AlignTop)
            # 设置字体，确保与样式表一致
            desc_font = QFont()
            desc_font.setPointSize(12)
            self.desc_label.setFont(desc_font)
            c = DesignSystem.COLORS
            self.desc_label.setStyleSheet(f"""
                QLabel {{
                    color: {c['text_secondary']};
                    font-size: 12px;
                    line-height: {DesignSystem.LINE_HEIGHTS['normal']};
                    padding: 2px 0;
                }}
            """)
            self.main_layout.addWidget(self.desc_label)
        
        # 底部区域：元数据
        bottom_layout = QHBoxLayout()
        bottom_layout.setContentsMargins(0, 0, 0, 0)
        bottom_layout.setSpacing(16)
        
        # 如果有路径信息，显示路径
        if 'path' in self.launch_data:
            path_text = f"路径: {self.launch_data['path']}"
            self.path_label = QLabel(path_text)
            c = DesignSystem.COLORS
            self.path_label.setStyleSheet(f"""
                QLabel {{
                    color: {c['text_tertiary']};
                    font-size: 12px;
                    font-style: italic;
                }}
            """)
            bottom_layout.addWidget(self.path_label)
        
        # 添加弹性空间
        bottom_layout.addStretch()
        
        # 添加到主布局
        self.main_layout.addLayout(bottom_layout)
        
        # 设置初始高度
        self.setMinimumHeight(60)
        
        # 使用定时器在组件显示后调整高度
        QTimer.singleShot(100, self.adjust_widget_height)
    
    def update_style(self):
        """根据选中状态更新样式"""
        c = DesignSystem.COLORS
        if self.is_selected:
            self.setStyleSheet(f"""
                ModernQuickLaunchListItemWidget {{
                    background-color: {c['primary_light']};
                    border: 2px solid {c['primary']};
                    border-radius: {DesignSystem.RADIUS['md']}px;
                    margin: 2px;
                }}
                ModernQuickLaunchListItemWidget:hover {{
                    background-color: {c['primary_bg']};
                    border-color: {c['primary_hover']};
                    box-shadow: {DesignSystem.SHADOWS['md']};
                }}
            """)
        else:
            self.setStyleSheet(f"""
                ModernQuickLaunchListItemWidget {{
                    background-color: {c['surface']};
                    border: 1px solid {c['border']};
                    border-radius: {DesignSystem.RADIUS['md']}px;
                    margin: 2px;
                }}
                ModernQuickLaunchListItemWidget:hover {{
                    background-color: {c['surface_hover']};
                    border-color: {c['primary']};
                    box-shadow: {DesignSystem.SHADOWS['md']};
                }}
            """)
    
    def set_selected(self, selected):
        """设置选中状态"""
        self.is_selected = selected
        self.update_style()
    
    def adjust_widget_height(self):
        """根据文本内容调整组件高度"""
        # 使用QTextDocument来更准确地计算文本所需的高度
        from PyQt5.QtGui import QTextDocument, QFont
        
        # 计算名称文本高度
        name_doc = QTextDocument()
        # 创建一个与样式表设置一致的字体
        name_font = QFont()
        name_font.setPointSize(12)  # 与CSS中的12px对应
        name_font.setBold(True)     # 与CSS中的font-weight: bold对应
        name_doc.setDefaultFont(name_font)
        name_doc.setPlainText(self.launch_id)
        
        # 计算描述文本高度
        desc_text = self.launch_data.get('description', '')
        desc_doc = QTextDocument()
        # 创建一个与样式表设置一致的字体
        desc_font = QFont()
        desc_font.setPointSize(12)  # 与CSS中的12px对应
        desc_doc.setDefaultFont(desc_font)
        desc_doc.setPlainText(desc_text)
        
        # 获取可用宽度（组件宽度减去边距）
        available_width = self.width() - 32  # 减去左右边距
        if available_width <= 0:
            available_width = 500  # 默认宽度
        
        # 设置文本宽度并计算所需高度
        name_doc.setTextWidth(available_width)
        name_height = name_doc.size().height()
        
        desc_doc.setTextWidth(available_width)
        desc_height = desc_doc.size().height() if desc_text else 0
        
        # 计算组件总高度
        # 顶部区域高度 + 名称高度 + 描述高度 + 底部区域高度 + 边距
        top_height = 24  # 类型标签和ID的高度
        bottom_height = 8  # 底部区域的高度
        margins = 24  # 上下边距
        spacing = 16  # 各区域之间的间距
        
        widget_height = int(name_height + desc_height) + top_height + bottom_height + margins + spacing
        # 确保最小高度
        widget_height = max(widget_height, 60)
        
        # 设置组件的最小高度和推荐高度
        self.setMinimumHeight(widget_height)
        self.resize(self.width(), widget_height)
    
    def resizeEvent(self, event):
        """重写大小调整事件，在组件大小改变时重新计算高度"""
        super().resizeEvent(event)
        # 在组件大小改变后，重新调整高度
        self.adjust_widget_height()


class QuickLaunchItemWidget(QWidget):
    """快速启动项列表项小部件，包含启动项文本和启动按钮"""
    def __init__(self, launch_text, launch_id, parent=None):
        super().__init__(parent)
        self.launch_text = launch_text
        self.launch_id = launch_id
        self.init_ui()
    
    def init_ui(self):
        layout = QHBoxLayout(self)
        s = DesignSystem.SPACING
        layout.setContentsMargins(s['sm'], s['sm'], s['sm'], s['sm'])
        layout.setSpacing(s['md'])
        
        # 启动项文本
        self.text_label = QLabel(self.launch_text)
        self.text_label.setWordWrap(True)
        self.text_label.setTextFormat(Qt.PlainText)  # 确保纯文本格式
        self.text_label.setAlignment(Qt.AlignLeft | Qt.AlignTop)  # 左上对齐
        self.text_label.setStyleSheet(DesignSystem.label_style('default'))
        layout.addWidget(self.text_label, 1)  # 占据大部分空间
        
        # 启动按钮
        self.launch_button = ModernButton("启动", "secondary")
        self.launch_button.setFixedSize(70, 30)
        self.launch_button.clicked.connect(self.launch_item)
        layout.addWidget(self.launch_button)
        
        # 设置初始高度
        self.setMinimumHeight(40)
        
        # 使用定时器在组件显示后调整高度
        QTimer.singleShot(100, self.adjust_widget_height)
    
    def adjust_widget_height(self):
        """根据文本内容调整组件高度"""
        # 使用QTextDocument来更准确地计算文本所需的高度
        from PyQt5.QtGui import QTextDocument
        
        # 创建一个临时的QTextDocument来计算文本高度
        doc = QTextDocument()
        doc.setDefaultFont(self.text_label.font())
        doc.setPlainText(self.launch_text)
        
        # 获取可用宽度（组件宽度减去按钮和边距）
        # 考虑按钮宽度、边距和间隔
        available_width = self.width() - 70 - 40  # 减去按钮宽度和更多边距
        if available_width <= 0:
            available_width = 400  # 默认宽度
        
        # 设置文本宽度并计算所需高度
        doc.setTextWidth(available_width)
        text_height = doc.size().height()
        
        # 组件高度 = 文本高度 + 上下边距 + 按钮边距
        widget_height = int(text_height) + 15  # 减少边距
        # 确保最小高度不小于按钮高度 + 边距
        widget_height = max(widget_height, 45)  # 调整最小高度
        
        # 设置组件的最小高度和推荐高度
        self.setMinimumHeight(widget_height)
        self.resize(self.width(), widget_height)
        
        # 更新列表项的大小提示
        if self.parent() and hasattr(self.parent(), 'quick_launch_list'):
            # 找到包含此小部件的列表项
            for i in range(self.parent().quick_launch_list.count()):
                item = self.parent().quick_launch_list.item(i)
                if item and self.parent().quick_launch_list.itemWidget(item) == self:
                    item.setSizeHint(self.sizeHint())
                    break
    
    def resizeEvent(self, event):
        """重写大小调整事件，在组件大小改变时重新计算高度"""
        super().resizeEvent(event)
        # 在组件大小改变后，重新调整高度
        self.adjust_widget_height()
    
    def launch_item(self):
        """启动快速启动项"""
        try:
            c = DesignSystem.COLORS
            # 获取快速启动项配置
            quick_launch_file = os.path.join('config', 'quick_settings.json')
            if not os.path.exists(quick_launch_file):
                QMessageBox.warning(self, "警告", "快速启动配置文件不存在")
                return
            
            with open(quick_launch_file, 'r', encoding='utf-8') as f:
                quick_launch_data = json.load(f)
            
            # 确保launches节点存在
            if 'launches' not in quick_launch_data:
                QMessageBox.warning(self, "警告", "快速启动配置文件中没有找到launches节点")
                return
                
            if self.launch_id not in quick_launch_data['launches']:
                QMessageBox.warning(self, "警告", f"未找到快速启动项: {self.launch_id}")
                return
            
            launch_info = quick_launch_data['launches'][self.launch_id]
            launch_path = launch_info.get('path', '')
            
            if not launch_path:
                QMessageBox.warning(self, "警告", f"快速启动项 {self.launch_id} 没有配置路径")
                return
            
            # 根据文件类型启动
            launch_type = launch_info.get('type', '')
            
            if launch_type == 'URL':
                # 如果是URL，使用浏览器打开
                import webbrowser
                webbrowser.open(launch_path)
            elif os.path.isfile(launch_path):
                # 如果是文件，使用系统默认程序打开
                if sys.platform == 'win32':
                    os.startfile(launch_path)
                elif sys.platform == 'darwin':
                    subprocess.run(['open', launch_path])
                else:
                    subprocess.run(['xdg-open', launch_path])
            elif os.path.isdir(launch_path):
                # 如果是文件夹，打开文件夹
                if sys.platform == 'win32':
                    subprocess.run(['explorer', launch_path])
                elif sys.platform == 'darwin':
                    subprocess.run(['open', launch_path])
                else:
                    subprocess.run(['xdg-open', launch_path])
            else:
                QMessageBox.warning(self, "警告", f"路径不存在: {launch_path}")
                return
            
            # 显示启动成功提示
            self.launch_button.setText("✓ 已启动")
            self.launch_button.setStyleSheet(f"""
                QPushButton {{
                    background-color: {c['success']};
                    border: 1px solid {c['success_hover']};
                    border-radius: {DesignSystem.RADIUS['sm']}px;
                    font-size: {DesignSystem.FONT_SIZES['sm']}px;
                    color: white;
                    padding: 2px 4px;
                }}
            """)
            
            # 2秒后恢复按钮状态
            QTimer.singleShot(2000, self.reset_button)
            
        except Exception as e:
            QMessageBox.critical(self, "错误", f"启动快速启动项失败：{str(e)}")
    
    def reset_button(self):
        """重置按钮状态"""
        self.launch_button.setText("🚀 启动")
        c = DesignSystem.COLORS
        self.launch_button.setStyleSheet(f"""
            QPushButton {{
                background-color: {c['surface_pressed']};
                border: 1px solid {c['border']};
                border-radius: {DesignSystem.RADIUS['sm']}px;
                font-size: {DesignSystem.FONT_SIZES['sm']}px;
                color: {c['text_primary']};
                padding: 2px 4px;
            }}
            QPushButton:hover {{
                background-color: {c['surface_hover']};
                border-color: {c['border_hover']};
            }}
            QPushButton:pressed {{
                background-color: {c['surface_pressed']};
            }}
        """)
    
    def update_text(self, text):
        """更新启动项文本"""
        self.launch_text = text
        self.text_label.setText(text)
        # 更新文本后重新调整组件高度
        self.adjust_widget_height()


class ProjectTableWidget(QTableWidget):
    """支持拖拽功能的项目表格控件"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent_tool = parent
        self.setAcceptDrops(True)
        self.viewport().setAcceptDrops(True)
        self.setDragDropMode(QAbstractItemView.DropOnly)
        self.original_style = None
    
    def dragEnterEvent(self, event):
        """处理拖拽进入事件"""
        if event.mimeData().hasUrls():
            # 保存原始样式
            if self.original_style is None:
                self.original_style = self.styleSheet()
            
            # 应用拖拽效果样式 - 加深阴影、放大边框
            c = DesignSystem.COLORS
            self.setStyleSheet(f"""
                QTableWidget {{
                    background-color: {c['surface']};
                    border: 2px solid {c['primary']};
                    border-radius: {DesignSystem.RADIUS['lg']}px;
                    gridline-color: {c['divider']};
                    selection-background-color: {c['primary_bg']};
                    box-shadow: 0 8px 32px rgba(0, 122, 255, 0.2);
                }}
                QTableWidget::item {{
                    padding: 12px 8px;
                    border-bottom: 1px solid {c['divider']};
                    color: {c['text_primary']};
                }}
                QTableWidget::item:selected {{
                    background-color: {c['primary_light']};
                    color: {c['primary']};
                }}
                QHeaderView::section {{
                    background-color: {c['surface']};
                    padding: 12px 8px;
                    border: none;
                    border-bottom: 1px solid {c['border']};
                    font-weight: 600;
                    color: {c['text_primary']};
                    font-size: {DesignSystem.FONT_SIZES['md']}px;
                }}
            """)
            event.acceptProposedAction()
        else:
            event.ignore()
    
    def dragLeaveEvent(self, event):
        """处理拖拽离开事件"""
        # 恢复原始样式
        if self.original_style is not None:
            self.setStyleSheet(self.original_style)
        super().dragLeaveEvent(event)
    
    def dragMoveEvent(self, event):
        """处理拖拽移动事件"""
        if event.mimeData().hasUrls():
            # 获取当前鼠标位置下的行
            index = self.indexAt(event.pos())
            if index.isValid():
                # 高亮显示当前行
                self.setCurrentCell(index.row(), 0)
            event.acceptProposedAction()
        else:
            event.ignore()
    
    def dropEvent(self, event):
        """处理拖拽释放事件"""
        # 恢复原始样式
        if self.original_style is not None:
            self.setStyleSheet(self.original_style)
        
        if event.mimeData().hasUrls():
            # 获取鼠标释放位置对应的行
            index = self.indexAt(event.pos())
            if index.isValid():
                current_row = index.row()
                # 获取项目ID
                project_id = self.item(current_row, 0).text()
                
                # 获取拖拽的文件URL
                urls = event.mimeData().urls()
                if urls:
                    file_paths = [Path(url.toLocalFile()).as_posix() for url in urls]
                    
                    # 处理文件路径，包括文件夹的处理
                    valid_files = []
                    
                    for file_path in file_paths:
                        path_obj = Path(file_path)
                        if path_obj.is_file():
                            # 如果是文件，直接添加
                            valid_files.append(path_obj.as_posix())
                        elif path_obj.is_dir():
                            # 如果是文件夹，遍历所有子文件夹中的文件
                            for file_obj in path_obj.rglob('*'):
                                if file_obj.is_file():
                                    valid_files.append(file_obj.as_posix())
                    
                    if not valid_files:
                        QMessageBox.warning(self, "警告", "未找到有效文件！")
                        return
                    
                    # 如果是多个文件，使用批量添加对话框
                    if len(valid_files) > 1:
                        dialog = BatchAddResourceDialog(self, self.parent_tool.resource_categories, valid_files, project_id, self.parent_tool.resource_types)
                        if dialog.exec_() == QDialog.Accepted:
                            self.parent_tool.add_resources_to_project_by_id(project_id, dialog.batch_resources_data)
                    else:
                        # 单个文件，使用普通添加对话框
                        dialog = AddResourceDialog(self, self.parent_tool.resource_categories, self.parent_tool.resource_types)
                        dialog.set_file_path(valid_files[0])
                        if dialog.exec_() == QDialog.Accepted:
                            self.parent_tool.add_resource_to_project_by_id(project_id, dialog.get_resource_data())
                
                event.acceptProposedAction()
            else:
                event.ignore()
        else:
            event.ignore()

class ModernCard(QFrame):
    """现代化卡片组件 - 使用统一设计系统"""
    def __init__(self, title="", parent=None):
        super().__init__(parent)
        self.setFrameStyle(QFrame.NoFrame)
        c = DesignSystem.COLORS
        s = DesignSystem.SPACING
        r = DesignSystem.RADIUS['lg']
        
        self.setStyleSheet(f"""
            ModernCard {{
                background-color: {c['surface']};
                border: 1px solid {c['border']};
                border-radius: {r}px;
                margin: {s['xs']}px;
            }}
            ModernCard:hover {{
                border-color: {c['border_hover']};
            }}
        """)
        
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(s['xl'], s['xl'], s['xl'], s['xl'])
        self.layout.setSpacing(s['lg'])
        
        if title:
            self.title_label = QLabel(title)
            self.title_label.setStyleSheet(DesignSystem.label_style('title'))
            self.layout.addWidget(self.title_label)
    
    def addWidget(self, widget):
        self.layout.addWidget(widget)
    
    def addLayout(self, layout):
        self.layout.addLayout(layout)

class ModernButton(QPushButton):
    """现代化按钮组件 - 使用统一设计系统"""
    def __init__(self, text="", button_type="primary", parent=None):
        super().__init__(text, parent)
        self.button_type = button_type
        self.setMinimumHeight(40)
        self.setCursor(Qt.PointingHandCursor)
        self.apply_style()
    
    def apply_style(self):
        self.setStyleSheet(DesignSystem.button_style(self.button_type))

class ModernSearchBox(QWidget):
    """现代化搜索框 - 使用统一设计系统，带清除按钮"""
    def __init__(self, placeholder="搜索...", parent=None):
        super().__init__(parent)
        self.init_ui(placeholder)
    
    def init_ui(self, placeholder):
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        # 搜索框
        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText(placeholder)
        self.line_edit.setMinimumHeight(44)
        c = DesignSystem.COLORS
        r = DesignSystem.RADIUS['lg']
        fs = DesignSystem.FONT_SIZES['lg']
        self.line_edit.setStyleSheet(f"""
            QLineEdit {{
                background-color: {c['surface']};
                border: 1px solid {c['border']};
                border-top-left-radius: {r}px;
                border-bottom-left-radius: {r}px;
                border-top-right-radius: 0px;
                border-bottom-right-radius: 0px;
                padding: 10px 12px 10px 16px;
                font-size: {fs}px;
                color: {c['text_primary']};
            }}
            QLineEdit:focus {{
                border: 2px solid {c['primary']};
                padding: 9px 11px 9px 15px;
            }}
            QLineEdit::placeholder {{
                color: {c['text_tertiary']};
            }}
        """)
        layout.addWidget(self.line_edit, 1)
        
        # 清除按钮
        self.clear_button = QPushButton("✕")
        self.clear_button.setFixedSize(44, 44)
        self.clear_button.setCursor(Qt.PointingHandCursor)
        self.clear_button.setStyleSheet(f"""
            QPushButton {{
                background-color: {c['surface']};
                border: 1px solid {c['border']};
                border-left: none;
                border-top-right-radius: {r}px;
                border-bottom-right-radius: {r}px;
                color: {c['text_secondary']};
                font-size: 18px;
                font-weight: bold;
            }}
            QPushButton:hover {{
                background-color: {c['surface_hover']};
                color: {c['text_primary']};
            }}
            QPushButton:pressed {{
                background-color: {c['surface_pressed']};
            }}
        """)
        self.clear_button.clicked.connect(self.clear)
        self.clear_button.hide()
        layout.addWidget(self.clear_button)
        
        # 连接文本变化信号
        self.line_edit.textChanged.connect(self.on_text_changed)
    
    def text(self):
        return self.line_edit.text()
    
    def setText(self, text):
        self.line_edit.setText(text)
    
    def clear(self):
        self.line_edit.clear()
    
    def on_text_changed(self, text):
        self.clear_button.setVisible(len(text) > 0)
    
    @property
    def textChanged(self):
        return self.line_edit.textChanged

class ModernListWidget(QListWidget):
    """现代化列表组件 - 使用统一设计系统"""
    def __init__(self, parent=None):
        super().__init__(parent)
        c = DesignSystem.COLORS
        r = DesignSystem.RADIUS['sm']
        self.setStyleSheet(f"""
            QListWidget {{
                background-color: transparent;
                border: none;
                outline: none;
            }}
            QListWidget::item {{
                background-color: {c['surface']};
                border: 1px solid {c['border']};
                border-radius: {r}px;
                margin: 2px 0;
                padding: 10px;
                color: {c['text_primary']};
            }}
            QListWidget::item:hover {{
                background-color: {c['primary_bg']};
                border-color: {c['primary']};
            }}
            QListWidget::item:selected {{
                background-color: {c['primary_light']};
                border-color: {c['primary']};
                color: {c['primary']};
            }}
        """)

class ModernTreeWidget(QTreeWidget):
    """现代化树形组件 - 使用统一设计系统"""
    def __init__(self, parent=None):
        super().__init__(parent)
        c = DesignSystem.COLORS
        r = DesignSystem.RADIUS['lg']
        fs = DesignSystem.FONT_SIZES['lg']
        self.setStyleSheet(f"""
            QTreeWidget {{
                background-color: {c['surface']};
                border: 1px solid {c['border']};
                border-radius: {r}px;
                outline: none;
                font-size: {fs}px;
            }}
            QTreeWidget::item {{
                padding: 8px;
                border-bottom: 1px solid {c['divider']};
            }}
            QTreeWidget::item:hover {{
                background-color: {c['primary_bg']};
            }}
            QTreeWidget::item:selected {{
                background-color: {c['primary_light']};
                color: {c['primary']};
            }}
            QHeaderView::section {{
                background-color: {c['surface']};
                border: none;
                border-right: 1px solid {c['border']};
                padding: 12px 8px;
                font-weight: 600;
                color: {c['text_primary']};
            }}
        """)
        
        header = self.header()
        header.setDefaultSectionSize(150)
        header.setStretchLastSection(True)
        
        self.setDragEnabled(True)
        self.setAcceptDrops(True)
        self.setDropIndicatorShown(True)
        self.setDragDropMode(QTreeWidget.InternalMove)

class EmptyStateWidget(QWidget):
    """空状态组件 - 当没有数据时显示友好的空状态界面"""
    def __init__(self, icon_text="📭", title="暂无数据", description="点击下方按钮开始添加", action_text="立即添加", parent=None):
        super().__init__(parent)
        self.icon_text = icon_text
        self.title = title
        self.description = description
        self.action_text = action_text
        self.action_callback = None
        self.init_ui()
    
    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)
        layout.setContentsMargins(40, 60, 40, 60)
        layout.setSpacing(24)
        
        # 图标
        icon_label = QLabel(self.icon_text)
        icon_label.setAlignment(Qt.AlignCenter)
        c = DesignSystem.COLORS
        icon_label.setStyleSheet(f"""
            QLabel {{
                font-size: 80px;
                color: {c['text_tertiary']};
            }}
        """)
        layout.addWidget(icon_label)
        
        # 标题
        title_label = QLabel(self.title)
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet(DesignSystem.label_style('title'))
        layout.addWidget(title_label)
        
        # 描述
        desc_label = QLabel(self.description)
        desc_label.setAlignment(Qt.AlignCenter)
        desc_label.setStyleSheet(DesignSystem.label_style('secondary'))
        desc_label.setWordWrap(True)
        layout.addWidget(desc_label)
        
        # 操作按钮
        self.action_button = ModernButton(self.action_text, "primary")
        self.action_button.setFixedWidth(160)
        self.action_button.clicked.connect(self.on_action_clicked)
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.action_button)
        button_layout.addStretch()
        layout.addLayout(button_layout)
        
        layout.addStretch()
    
    def set_action_callback(self, callback):
        """设置操作按钮的回调函数"""
        self.action_callback = callback
    
    def on_action_clicked(self):
        """操作按钮点击事件"""
        if self.action_callback:
            self.action_callback()
    
    def set_content(self, icon_text=None, title=None, description=None, action_text=None):
        """更新空状态内容"""
        if icon_text is not None:
            self.icon_text = icon_text
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if action_text is not None:
            self.action_text = action_text
            self.action_button.setText(action_text)
        # 重新初始化UI
        self.init_ui()
        
        # 右键菜单将由父组件处理
    

    
    def dropEvent(self, event):
        """处理拖放事件"""
        # 调用父类方法处理拖放
        super().dropEvent(event)
        
        # 通知父窗口更新资源分组
        if hasattr(self.parent(), 'update_resource_groups_after_drop'):
            self.parent().update_resource_groups_after_drop()

class KnowledgeManagerTool(QMainWindow):
    """现代化知识管理工具"""
    
    TOOL_INFO = {
        'name': '个人知识管理工具',
        'description': '按项目和资源文件类型双维度管理文件的知识管理工具',
        'icon_type': 'system',
        'icon_value': QStyle.SP_DirIcon,
        'color': '#2196F3',
        'config_file': 'knowledge_manager_config.json',
        'data_file': 'knowledge_manager_data.json',
        'version': '2.0.0',
        'registry_class': 'KnowledgeManagerRegistry',
    }
    
    def __init__(self):
        """初始化方法"""
        super().__init__()
        
        # 确定应用程序目录，兼容开发环境和打包后的exe
        if getattr(sys, 'frozen', False):
            # 是打包后的exe
            self.app_dir = os.path.dirname(sys.executable)
        else:
            # 如果是开发环境
            self.app_dir = os.path.dirname(os.path.abspath(__file__))
        
        # 设置默认配置和数据目录
        default_config_dir = os.path.join(self.app_dir, 'config')
        default_data_dir = os.path.join(self.app_dir, 'data')
        
        # 确保默认目录存在
        os.makedirs(default_config_dir, exist_ok=True)
        os.makedirs(default_data_dir, exist_ok=True)
        
        # 设置配置和数据文件路径
        self.config_path = os.path.join(default_config_dir, 'knowledge_manager_config.json')
        self.data_path = os.path.join(default_data_dir, 'knowledge_manager_data.json')
        
        # 设置日志配置
        log_dir = os.path.join(self.app_dir, 'logs')
        os.makedirs(log_dir, exist_ok=True)
        log_file = os.path.join(log_dir, 'knowledge_manager.log')
        
        # 配置日志
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file, encoding='utf-8'),
                logging.StreamHandler()  # 同时输出到控制台
            ]
        )
        
        # 设置笔记目录
        self.notes_dir = os.path.join(default_data_dir, 'project_notes')
        os.makedirs(self.notes_dir, exist_ok=True)
        
        # 初始化数据结构
        self.projects = []
        self.selected_project_name = None
        self.project_types = ["学习项目", "工作项目", "研究项目", "个人项目", "团队项目", "实验项目", "文档整理", "代码开发", "数据分析", "其他"]
        # 文件类型配置（用于文件扩展名匹配和路径管理）
        self.resource_types = {
            '电子书': {
                'path': '', 
                'extensions': ['.pdf', '.epub', '.mobi', '.txt', '.azw3'],
                'extension_display_names': {
                    '.pdf': 'PDF文档',
                    '.epub': '电子书',
                    '.mobi': '电子书',
                    '.txt': '文本文件',
                    '.azw3': '电子书'
                }
            },
            '视频': {
                'path': '', 
                'extensions': ['.mp4', '.avi', '.mkv', '.mov', '.wmv'],
                'extension_display_names': {
                    '.mp4': '视频文件',
                    '.avi': '视频文件',
                    '.mkv': '视频文件',
                    '.mov': '视频文件',
                    '.wmv': '视频文件'
                }
            },
            '代码': {
                'path': '', 
                'extensions': ['.py', '.js', '.html', '.css', '.java', '.cpp'],
                'extension_display_names': {
                    '.py': 'Python脚本',
                    '.js': 'JavaScript',
                    '.html': 'HTML文档',
                    '.css': 'CSS样式',
                    '.java': 'Java代码',
                    '.cpp': 'C++代码'
                }
            },
            '文档': {
                'path': '', 
                'extensions': ['.md', '.doc', '.docx', '.txt', '.ppt', '.pptx', '.xls', '.xlsx'],
                'extension_display_names': {
                    '.md': 'Markdown文档',
                    '.doc': 'Word文档',
                    '.docx': 'Word文档',
                    '.txt': '文本文件',
                    '.ppt': 'PowerPoint演示文稿',
                    '.pptx': 'PowerPoint演示文稿',
                    '.xls': 'Excel工作表',
                    '.xlsx': 'Excel工作表'
                }
            },
            '图片': {
                'path': '', 
                'extensions': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
                'extension_display_names': {
                    '.jpg': 'JPEG图片',
                    '.jpeg': 'JPEG图片',
                    '.png': 'PNG图片',
                    '.gif': 'GIF图片',
                    '.bmp': 'BMP图片',
                    '.svg': 'SVG图片'
                }
            },
            '音频': {
                'path': '', 
                'extensions': ['.mp3', '.wav', '.ogg', '.flac', '.aac'],
                'extension_display_names': {
                    '.mp3': 'MP3音频',
                    '.wav': 'WAV音频',
                    '.ogg': 'OGG音频',
                    '.flac': 'FLAC音频',
                    '.aac': 'AAC音频'
                }
            },
            '网页链接': {
                'path': '', 
                'extensions': ['.url', '.html'],
                'extension_display_names': {
                    '.url': '网页链接',
                    '.html': 'HTML文档'
                }
            }
        }
        
        # 资源文件类型配置（用于资源分类管理）
        self.resource_categories = [
            "参考资料",
            "灵感火花", 
            "产出成品"
        ]
        
        # 自动扫描设置默认值
        # 自动扫描功能配置 - 默认禁用，由配置文件控制
        self.auto_scan_enabled = False  # 默认禁用，由配置文件控制
        self.auto_scan_interval = 30  # 扫描间隔（秒）
        self.auto_scan_file_types = ['.pdf', '.docx', '.txt', '.md', '.jpg', '.png', '.mp4', '.mp3', '.ppt', '.pptx', '.xls', '.xlsx', '.bmp']
        self.auto_scan_exclude_folders = ['.git', '__pycache__', 'node_modules', '.vscode']
        
        # 自动扫描定时器
        self.auto_scan_timer = None
        
        # 跟踪打开的项目详情对话框
        self.open_project_dialogs = []
        
        # 加载配置和数据
        self.load_config()
        
        # 先加载数据，再进行完整性检查
        self.load_data()
        
        # 初始化UI（优先显示界面）
        self.init_ui()
        self.setWindowTitle(f"个人知识管理工具 V{self.TOOL_INFO['version']}")
        
        # 以下操作延迟执行，确保UI快速显示
        # 使用QTimer.singleShot将耗时操作延迟到UI显示后执行
        QTimer.singleShot(100, self._delayed_startup_tasks)
    
    def _delayed_startup_tasks(self):
        """延迟执行的启动任务，避免阻塞UI显示"""
        # 启动时进行数据完整性检查
        self.startup_integrity_check()
        
        # 刷新项目列表显示
        self.refresh_project_list()
        
        # 启动自动扫描功能
        self.setup_auto_scan()
        
        # 程序启动时立即执行一次自动扫描（延迟执行，确保UI完全加载）
        # 只有在明确启用自动扫描时才执行
        if hasattr(self, 'auto_scan_enabled') and self.auto_scan_enabled:
            logging.info(f"自动扫描已启用，将在1秒后执行启动扫描")
            # 使用QTimer.singleShot延迟执行，确保UI完全加载后再执行扫描
            QTimer.singleShot(1000, self.perform_auto_scan)
        else:
            logging.info("自动扫描已禁用，跳过启动扫描")
        
    def setup_auto_scan(self):
        """设置自动扫描功能"""
        # 停止现有定时器
        if hasattr(self, 'auto_scan_timer') and self.auto_scan_timer:
            self.auto_scan_timer.stop()
            self.auto_scan_timer.deleteLater()
            self.auto_scan_timer = None
        
        # 只有在明确启用自动扫描时才创建和启动定时器
        if hasattr(self, 'auto_scan_enabled') and self.auto_scan_enabled:
            # 创建新的定时器
            self.auto_scan_timer = QTimer()
            self.auto_scan_timer.timeout.connect(self.perform_auto_scan)
            
            # 启动定时器（间隔转换为毫秒）
            self.auto_scan_timer.start(self.auto_scan_interval * 1000)
            self.show_status_message(f"自动扫描已启动，间隔 {self.auto_scan_interval} 秒")
        else:
            self.show_status_message("自动扫描已禁用")
    
    def perform_auto_scan(self):
        """执行自动扫描"""
        try:
            logging.info("开始执行自动扫描...")
            if not self.auto_scan_enabled:
                logging.info("自动扫描已禁用，跳过扫描")
                return
                
            self.show_status_message("正在执行自动扫描...")
            
            # 获取启用了自动扫描的项目路径
            project_paths = set()
            for project in self.projects:
                # 检查项目是否启用了自动扫描
                if not project.get('auto_scan_resources', False):
                    logging.info(f"项目 '{project.get('name', '未知')}' 未启用自动扫描，跳过")
                    continue
                
                # 检查两种可能的路径字段：path 和 folder_path
                project_path = None
                if 'path' in project and project['path'] and os.path.exists(project['path']):
                    project_path = project['path']
                elif 'folder_path' in project and project['folder_path'] and os.path.exists(project['folder_path']):
                    project_path = project['folder_path']
                
                if project_path:
                    project_paths.add(project_path)
                    logging.info(f"添加项目路径到扫描列表: {project_path}")
                    logging.info(f"项目名称: {project.get('name', '未知')}")
                else:
                    logging.warning(f"项目 '{project.get('name', '未知')}' 启用了自动扫描但没有有效的路径设置")
                    logging.warning(f"  path字段: {project.get('path', 'None')}")
                    logging.warning(f"  folder_path字段: {project.get('folder_path', 'None')}")
            
            if not project_paths:
                logging.info("没有有效的项目路径可供扫描")
                self.show_status_message("没有有效的项目路径可供扫描")
                return
            
            # 扫描每个项目路径
            new_files_found = 0
            for project_path in project_paths:
                logging.info(f"开始扫描项目路径: {project_path}")
                new_files = self.scan_directory_for_new_files(project_path)
                new_files_found += len(new_files)
                logging.info(f"在路径 {project_path} 中发现 {len(new_files)} 个新文件")
                
                # 如果找到新文件，添加到对应项目中
                for file_info in new_files:
                    logging.info(f"添加新文件到项目: {file_info['path']}")
                    self.add_file_to_project_by_path(file_info['path'], project_path)
            
            # 更新状态栏
            if new_files_found > 0:
                self.show_status_message(f"自动扫描完成，发现 {new_files_found} 个新文件")
                # 保存数据后刷新项目列表
                self.save_data()
                self.refresh_project_list()  # 刷新项目列表
                logging.info(f"自动扫描完成，发现 {new_files_found} 个新文件")
            else:
                self.show_status_message("自动扫描完成，未发现新文件")
                logging.info("自动扫描完成，未发现新文件")
                
        except Exception as e:
            error_msg = f"自动扫描出错: {str(e)}"
            self.show_status_message(error_msg)
            logging.error(error_msg, exc_info=True)
    
    def scan_directory_for_new_files(self, directory):
        """扫描目录以查找新文件"""
        new_files = []
        
        try:
            # 遍历目录
            for root, dirs, files in os.walk(directory):
                # 检查是否应该跳过此目录
                dirs[:] = [d for d in dirs if not any(exclude in d for exclude in self.auto_scan_exclude_folders)]
                
                for file in files:
                    file_path = os.path.join(root, file)
                    file_ext = os.path.splitext(file)[1].lower()
                    
                    # 检查文件扩展名是否在扫描列表中
                    if file_ext in self.auto_scan_file_types:
                        # 检查文件是否已经存在于任何项目中
                        if not self.is_file_already_tracked(file_path):
                            # 获取文件信息
                            file_info = {
                                'path': file_path,
                                'name': file,
                                'extension': file_ext,
                                'size': os.path.getsize(file_path),
                                'modified_time': os.path.getmtime(file_path)
                            }
                            new_files.append(file_info)
                            
        except Exception as e:
            self.show_status_message(f"扫描目录 {directory} 时出错: {str(e)}")
            
        return new_files
    
    def is_file_already_tracked(self, file_path):
        """检查文件是否已被跟踪"""
        # 标准化文件路径
        normalized_path = os.path.normpath(file_path)
        
        for project in self.projects:
            if 'resources' in project:
                for resource in project['resources']:
                    if 'path' in resource:
                        resource_path = os.path.normpath(resource['path'])
                        if normalized_path == resource_path:
                            return True
        return False
    
    def add_file_to_project_by_path(self, file_path, project_path):
        """根据文件路径和项目路径将文件添加到对应项目"""
        try:
            # 查找对应的项目
            target_project = None
            normalized_project_path = os.path.normpath(project_path)
            
            for project in self.projects:
                # 检查两种可能的路径字段：path 和 folder_path
                project_path_field = None
                if 'path' in project and project['path']:
                    project_path_field = os.path.normpath(project['path'])
                elif 'folder_path' in project and project['folder_path']:
                    project_path_field = os.path.normpath(project['folder_path'])
                
                if project_path_field and project_path_field == normalized_project_path:
                    # 确保项目启用了自动扫描
                    if not project.get('auto_scan_resources', False):
                        logging.warning(f"项目 '{project.get('name', '未知')}' 未启用自动扫描，跳过添加文件")
                        return False
                    target_project = project
                    break
            
            if not target_project:
                logging.warning(f"未找到路径为 {project_path} 的项目")
                return False
                
            # 确定资源类型
            file_ext = os.path.splitext(file_path)[1].lower()
            resource_type = self.determine_resource_type(file_ext)
            
            # 创建资源对象
            file_name = os.path.basename(file_path)
            file_size = os.path.getsize(file_path)
            modified_time = os.path.getmtime(file_path)
            
            new_resource = {
                'name': file_name,
                'path': file_path,
                'type': resource_type,
                'category': '参考资料',  # 默认分类
                'size': file_size,
                'modified_time': modified_time,
                'added_time': time.time()
            }
            
            # 添加到项目资源列表
            if 'resources' not in target_project:
                target_project['resources'] = []
            target_project['resources'].append(new_resource)
            
            # 更新项目的资源数量
            target_project['resource_count'] = len(target_project['resources'])
            
            # 更新项目修改时间
            target_project['modified_time'] = time.time()
            
            # 记录日志
            self.add_project_log(
                target_project['name'],
                f"自动扫描添加资源: {file_name} ({resource_type})"
            )
            
            logging.info(f"成功添加文件 {file_name} 到项目 {target_project['name']}")
            return True
            
        except Exception as e:
            error_msg = f"添加文件到项目时出错: {str(e)}"
            self.show_status_message(error_msg)
            logging.error(error_msg, exc_info=True)
            return False
    
    def determine_resource_type(self, file_ext):
        """根据文件扩展名确定资源类型"""
        for resource_type, config in self.resource_types.items():
            if 'extensions' in config and file_ext in config['extensions']:
                return resource_type
        return '其他'  # 默认类型
        
    def show_status_message(self, message, timeout=3000):
        """在状态栏显示消息"""
        if hasattr(self, 'status_bar'):
            self.status_bar.showMessage(message, timeout)
        
    def focusInEvent(self, event):
        """窗口获得焦点时的事件处理"""
        super().focusInEvent(event)
        # 当窗口获得焦点时，刷新项目列表以读取最新文件中的项目信息
        self.refresh_project_list()
        
    def init_ui(self):
        """初始化现代化界面 - 使用统一设计系统"""
        width, height = get_optimal_window_size()
        self.resize(width, height)
        self.setMinimumSize(800, 600)
        center_window(self)
        
        self.create_menu_bar()
        
        c = DesignSystem.COLORS
        s = DesignSystem.SPACING
        self.setStyleSheet(f"""
            QMainWindow {{
                background-color: {c['background']};
            }}
            {DesignSystem.tab_style()}
        """)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QHBoxLayout(central_widget)
        main_layout.setContentsMargins(s['lg'], s['lg'], s['lg'], s['lg'])
        main_layout.setSpacing(s['lg'])
        
        splitter = QSplitter(Qt.Horizontal)
        main_layout.addWidget(splitter)
        
        left_panel = self.create_project_management_panel()
        splitter.addWidget(left_panel)
        
        right_panel = self.create_resource_file_type_panel()
        splitter.addWidget(right_panel)
        
        splitter.setSizes([1400, 600])
        splitter.setChildrenCollapsible(False)
        
        self.create_modern_status_bar()
        
    def create_menu_bar(self):
        """创建菜单栏 - 使用统一设计系统"""
        menubar = self.menuBar()
        menubar.setStyleSheet(DesignSystem.menu_style())
        
        file_menu = menubar.addMenu('文件')
        
        new_project_action = QAction('新建项目', self)
        new_project_action.setShortcut('Ctrl+N')
        new_project_action.triggered.connect(self.new_project)
        file_menu.addAction(new_project_action)
        
        file_menu.addSeparator()
        
        import_action = QAction('导入项目', self)
        import_action.setShortcut('Ctrl+I')
        import_action.triggered.connect(self.import_projects)
        file_menu.addAction(import_action)
        
        export_action = QAction('导出项目', self)
        export_action.setShortcut('Ctrl+E')
        export_action.triggered.connect(self.export_projects)
        file_menu.addAction(export_action)
        
        file_menu.addSeparator()
        
        exit_action = QAction('退出', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        
        resource_menu = menubar.addMenu('资源')
        
        resource_inventory_action = QAction('资源清单', self)
        resource_inventory_action.triggered.connect(self.show_resource_inventory)
        resource_menu.addAction(resource_inventory_action)
        
        # 检查灵感池文件是否存在，如果不存在则不添加菜单项
        inspiration_pool_file = os.path.join(os.path.dirname(__file__), "inspiration_pool_tool.py")
        if os.path.exists(inspiration_pool_file):
            inspiration_pool_action = QAction('灵感池', self)
            inspiration_pool_action.setShortcut('Ctrl+P')
            inspiration_pool_action.triggered.connect(self.open_inspiration_pool)
            resource_menu.addAction(inspiration_pool_action)
        
        config_menu = menubar.addMenu('配置')
        
        resource_type_action = QAction('资源文件类型配置', self)
        resource_type_action.triggered.connect(self.config_resource_types)
        config_menu.addAction(resource_type_action)
        
        project_type_action = QAction('项目类型配置', self)
        project_type_action.triggered.connect(self.config_project_types)
        config_menu.addAction(project_type_action)
        
        config_menu.addSeparator()
        
        default_path_action = QAction('默认项目路径设置', self)
        default_path_action.triggered.connect(self.config_default_project_path)
        config_menu.addAction(default_path_action)
        
        auto_scan_action = QAction('自动扫描设置', self)
        auto_scan_action.triggered.connect(self.config_auto_scan)
        config_menu.addAction(auto_scan_action)
        
        config_menu.addSeparator()
        
        backup_action = QAction('创建数据备份', self)
        backup_action.triggered.connect(self.manual_backup_data)
        config_menu.addAction(backup_action)
        
        restore_action = QAction('从备份恢复', self)
        restore_action.triggered.connect(self.manual_restore_data)
        config_menu.addAction(restore_action)
        
        check_integrity_action = QAction('检查数据完整性', self)
        check_integrity_action.triggered.connect(self.check_data_integrity)
        config_menu.addAction(check_integrity_action)
        
        config_menu.addSeparator()
        
        open_config_folder_action = QAction('打开配置文件夹', self)
        open_config_folder_action.triggered.connect(self.open_config_folder)
        config_menu.addAction(open_config_folder_action)

        open_data_folder_action = QAction('打开数据文件夹', self)
        open_data_folder_action.triggered.connect(self.open_data_folder)
        config_menu.addAction(open_data_folder_action)
        
        help_menu = menubar.addMenu('帮助')
        
        about_action = QAction('关于', self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)
    
    def config_auto_scan(self):
        """配置自动扫描设置"""
        dialog = QDialog(self)
        dialog.setWindowTitle("自动扫描设置")
        dialog.setMinimumWidth(600)
        dialog.setWindowModality(Qt.ApplicationModal)
        
        layout = QVBoxLayout(dialog)
        layout.setSpacing(20)
        layout.setContentsMargins(24, 24, 24, 24)
        
        # 启用自动扫描
        enabled_group = QGroupBox("自动扫描设置")
        enabled_layout = QHBoxLayout(enabled_group)
        
        self.auto_scan_enabled_checkbox = QCheckBox("启用自动扫描")
        self.auto_scan_enabled_checkbox.setChecked(self.auto_scan_enabled)
        enabled_layout.addWidget(self.auto_scan_enabled_checkbox)
        
        layout.addWidget(enabled_group)
        
        # 扫描间隔设置
        interval_group = QGroupBox("扫描间隔")
        interval_layout = QHBoxLayout(interval_group)
        
        interval_layout.addWidget(QLabel("扫描间隔(秒):"))
        self.auto_scan_interval_spinbox = QSpinBox()
        self.auto_scan_interval_spinbox.setRange(10, 3600)
        self.auto_scan_interval_spinbox.setValue(self.auto_scan_interval)
        self.auto_scan_interval_spinbox.setSuffix(" 秒")
        interval_layout.addWidget(self.auto_scan_interval_spinbox)
        
        interval_layout.addStretch()
        layout.addWidget(interval_group)
        
        # 文件类型设置
        file_types_group = QGroupBox("扫描文件类型")
        file_types_layout = QVBoxLayout(file_types_group)
        
        file_types_help = QLabel("选择要自动扫描的文件类型:")
        file_types_help.setStyleSheet("color: #666; font-size: 12px;")
        file_types_layout.addWidget(file_types_help)
        
        # 创建文件类型复选框
        file_types_grid = QGridLayout()
        
        # 常见文件类型
        common_extensions = [
            ('.pdf', 'PDF文档'),
            ('.docx', 'Word文档'),
            ('.xlsx', 'Excel表格'),
            ('.pptx', 'PowerPoint演示文稿'),
            ('.txt', '文本文件'),
            ('.md', 'Markdown文件'),
            ('.jpg', 'JPEG图片'),
            ('.png', 'PNG图片'),
            ('.gif', 'GIF图片'),
            ('.mp4', 'MP4视频'),
            ('.mp3', 'MP3音频'),
            ('.zip', 'ZIP压缩包'),
            ('.rar', 'RAR压缩包'),
            ('.py', 'Python代码'),
            ('.html', 'HTML文件'),
            ('.css', 'CSS样式'),
            ('.js', 'JavaScript脚本')
        ]
        
        self.file_type_checkboxes = {}
        row, col = 0, 0
        for ext, desc in common_extensions:
            checkbox = QCheckBox(f"{desc} ({ext})")
            checkbox.setChecked(ext in self.auto_scan_file_types)
            self.file_type_checkboxes[ext] = checkbox
            file_types_grid.addWidget(checkbox, row, col)
            
            col += 1
            if col > 2:  # 每行3个
                col = 0
                row += 1
        
        file_types_layout.addLayout(file_types_grid)
        layout.addWidget(file_types_group)
        
        # 排除文件夹设置
        exclude_group = QGroupBox("排除文件夹")
        exclude_layout = QVBoxLayout(exclude_group)
        
        exclude_help = QLabel("包含以下名称的文件夹将被跳过:")
        exclude_help.setStyleSheet("color: #666; font-size: 12px;")
        exclude_layout.addWidget(exclude_help)
        
        self.exclude_folders_edit = QTextEdit()
        self.exclude_folders_edit.setMaximumHeight(100)
        self.exclude_folders_edit.setPlainText('\n'.join(self.auto_scan_exclude_folders))
        exclude_layout.addWidget(self.exclude_folders_edit)
        
        exclude_note = QLabel("每行一个文件夹名称，例如: .git, __pycache__, node_modules")
        exclude_note.setStyleSheet("color: #999; font-size: 11px;")
        exclude_layout.addWidget(exclude_note)
        
        layout.addWidget(exclude_group)
        
        # 按钮区域
        button_layout = QHBoxLayout()
        
        test_button = ModernButton("测试扫描", "secondary")
        test_button.clicked.connect(lambda: self.test_auto_scan_settings(dialog))
        button_layout.addWidget(test_button)
        
        button_layout.addStretch()
        
        save_button = ModernButton("保存设置", "primary")
        save_button.clicked.connect(lambda: self.save_auto_scan_settings(dialog))
        button_layout.addWidget(save_button)
        
        cancel_button = ModernButton("取消", "ghost")
        cancel_button.clicked.connect(dialog.reject)
        button_layout.addWidget(cancel_button)
        
        layout.addLayout(button_layout)
        
        # 显示对话框
        dialog.exec_()
    
    def save_auto_scan_settings(self, dialog):
        """保存自动扫描设置"""
        try:
            # 更新设置
            self.auto_scan_enabled = self.auto_scan_enabled_checkbox.isChecked()
            self.auto_scan_interval = self.auto_scan_interval_spinbox.value()
            
            # 更新文件类型
            self.auto_scan_file_types = []
            for ext, checkbox in self.file_type_checkboxes.items():
                if checkbox.isChecked():
                    self.auto_scan_file_types.append(ext)
            
            # 更新排除文件夹
            exclude_text = self.exclude_folders_edit.toPlainText().strip()
            if exclude_text:
                self.auto_scan_exclude_folders = [folder.strip() for folder in exclude_text.split('\n') if folder.strip()]
            else:
                self.auto_scan_exclude_folders = []
            
            # 保存到配置文件
            self.save_config()
            
            # 重新设置自动扫描
            self.setup_auto_scan()
            
            # 关闭对话框
            dialog.accept()
            
            # 显示成功消息
            self.show_status_message("自动扫描设置已保存")
            
        except Exception as e:
            QMessageBox.warning(self, "保存失败", f"保存自动扫描设置时出错: {str(e)}")
    
    def test_auto_scan_settings(self, parent_dialog):
        """测试自动扫描设置"""
        try:
            # 获取当前设置
            enabled = self.auto_scan_enabled_checkbox.isChecked()
            interval = self.auto_scan_interval_spinbox.value()
            
            file_types = []
            for ext, checkbox in self.file_type_checkboxes.items():
                if checkbox.isChecked():
                    file_types.append(ext)
            
            exclude_text = self.exclude_folders_edit.toPlainText().strip()
            if exclude_text:
                exclude_folders = [folder.strip() for folder in exclude_text.split('\n') if folder.strip()]
            else:
                exclude_folders = []
            
            # 创建测试结果对话框
            result_dialog = QDialog(parent_dialog)
            result_dialog.setWindowTitle("测试结果")
            result_dialog.setMinimumWidth(500)
            result_layout = QVBoxLayout(result_dialog)
            
            # 显示当前设置
            settings_text = QTextEdit()
            settings_text.setReadOnly(True)
            settings_text.setMaximumHeight(200)
            
            settings_content = f"""
自动扫描状态: {'启用' if enabled else '禁用'}
扫描间隔: {interval} 秒
扫描文件类型: {', '.join(file_types) if file_types else '无'}
排除文件夹: {', '.join(exclude_folders) if exclude_folders else '无'}
            """
            
            settings_text.setPlainText(settings_content)
            result_layout.addWidget(QLabel("当前设置:"))
            result_layout.addWidget(settings_text)
            
            # 测试扫描
            if enabled and file_types:
                result_layout.addWidget(QLabel("测试扫描结果:"))
                
                test_result = QTextEdit()
                test_result.setReadOnly(True)
                test_result.setMaximumHeight(150)
                
                # 获取第一个项目路径进行测试
                test_path = None
                for project in self.projects:
                    if 'path' in project and project['path'] and os.path.exists(project['path']):
                        test_path = project['path']
                        break
                
                if test_path:
                    # 临时应用设置进行测试
                    original_enabled = self.auto_scan_enabled
                    original_file_types = self.auto_scan_file_types
                    original_exclude_folders = self.auto_scan_exclude_folders
                    
                    self.auto_scan_enabled = enabled
                    self.auto_scan_file_types = file_types
                    self.auto_scan_exclude_folders = exclude_folders
                    
                    # 执行测试扫描
                    new_files = self.scan_directory_for_new_files(test_path)
                    
                    # 恢复原始设置
                    self.auto_scan_enabled = original_enabled
                    self.auto_scan_file_types = original_file_types
                    self.auto_scan_exclude_folders = original_exclude_folders
                    
                    if new_files:
                        test_result.setPlainText(f"在路径 {test_path} 中发现 {len(new_files)} 个新文件:\n\n")
                        for i, file_info in enumerate(new_files[:5]):  # 只显示前5个
                            test_result.append(f"{i+1}. {file_info['name']} ({file_info['extension']})")
                        
                        if len(new_files) > 5:
                            test_result.append(f"... 还有 {len(new_files) - 5} 个文件")
                    else:
                        test_result.setPlainText(f"在路径 {test_path} 中未发现新文件")
                else:
                    test_result.setPlainText("没有找到有效的项目路径进行测试")
                
                result_layout.addWidget(test_result)
            else:
                result_layout.addWidget(QLabel("自动扫描未启用或未选择文件类型，无法进行测试"))
            
            # 关闭按钮
            close_button = QPushButton("关闭")
            close_button.clicked.connect(result_dialog.accept)
            result_layout.addWidget(close_button)
            
            # 显示测试结果
            result_dialog.exec_()
            
        except Exception as e:
            QMessageBox.warning(self, "测试失败", f"测试自动扫描设置时出错: {str(e)}")
        
    def show_about(self):
        """显示关于对话框"""
        QMessageBox.about(self, "关于", 
                         f"个人知识管理工具\n\n"
                         f"版本: {self.TOOL_INFO['version']}\n"
                         f"描述: {self.TOOL_INFO['description']}\n\n"
                         f"现代化界面设计，支持项目和资源类型双维度管理")
        
    def create_project_management_panel(self):
        """创建项目管理面板"""
        panel = QWidget()
        layout = QVBoxLayout(panel)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(16)
        
        # 项目统计区域
        stats_card = ModernCard("")
        stats_main_layout = QVBoxLayout()
        
        # 标题和日期范围选择区域（同一行）
        header_layout = QHBoxLayout()
        header_layout.setSpacing(20)
        
        # 项目统计标题
        stats_title = QLabel("项目统计")
        c = DesignSystem.COLORS
        stats_title.setStyleSheet(f"""
            QLabel {{
                font-size: 20px;
                font-weight: 700;
                color: {c['text_primary']};
                margin-right: 20px;
                letter-spacing: -0.3px;
            }}
        """)
        
        # 日期范围选择区域
        date_range_layout = QHBoxLayout()
        date_range_layout.setSpacing(12)
        
        # 日期范围标题
        date_range_title = QLabel("📅 统计时间范围:")
        c = DesignSystem.COLORS
        date_range_title.setStyleSheet(f"""
            QLabel {{
                font-size: {DesignSystem.FONT_SIZES['lg']}px;
                font-weight: 600;
                color: {c['text_primary']};
                margin-right: 8px;
            }}
        """)
        
        # 开始日期
        start_date_label = QLabel("从")
        c = DesignSystem.COLORS
        start_date_label.setStyleSheet(f"""
            QLabel {{
                font-size: {DesignSystem.FONT_SIZES['lg']}px;
                color: {c['text_secondary']};
                font-weight: 500;
            }}
        """)
        self.start_date_edit = QDateEdit()
        # 设置为空日期，显示为"请选择"
        self.start_date_edit.setSpecialValueText("请选择")
        # 设置最小日期，当日期等于最小日期时会显示specialValueText
        min_date = QDate(2025, 1, 1)
        self.start_date_edit.setMinimumDate(min_date)
        # 设置日期为最小日期，触发显示specialValueText
        self.start_date_edit.setDate(min_date)
        self.start_date_edit.setCalendarPopup(True)
        self.start_date_edit.setFixedHeight(36)
        self.start_date_edit.setMinimumWidth(130)
        # 防止自动获得焦点
        self.start_date_edit.setFocusPolicy(Qt.NoFocus)
        self.start_date_edit.setStyleSheet(DesignSystem.dateedit_style())
        self.start_date_edit.dateChanged.connect(self.on_date_range_changed)
        
        # 到
        to_label = QLabel("到")
        to_label.setStyleSheet(DesignSystem.label_style('secondary'))
        
        # 结束日期
        self.end_date_edit = QDateEdit()
        # 设置为空日期，显示为"请选择"
        self.end_date_edit.setSpecialValueText("请选择")
        # 设置最小日期为2025年1月1日，允许选择2025年之后的任意日期
        end_min_date = QDate(2025, 1, 1)
        self.end_date_edit.setMinimumDate(end_min_date)
        # 设置最大日期为未来很远的日期，确保用户可以选择任意未来日期
        self.end_date_edit.setMaximumDate(QDate(2099, 12, 31))
        # 设置日期为最小日期，触发显示specialValueText
        self.end_date_edit.setDate(end_min_date)
        self.end_date_edit.setCalendarPopup(True)
        self.end_date_edit.setFixedHeight(36)
        self.end_date_edit.setMinimumWidth(130)
        # 防止自动获得焦点
        self.end_date_edit.setFocusPolicy(Qt.NoFocus)
        self.end_date_edit.setStyleSheet(DesignSystem.dateedit_style())
        self.end_date_edit.dateChanged.connect(self.on_date_range_changed)
        
        # 重置按钮
        reset_date_btn = ModernButton("🔄 重置", "secondary")
        reset_date_btn.setFixedHeight(36)
        reset_date_btn.setMinimumWidth(80)
        c = DesignSystem.COLORS
        reset_date_btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {c['surface']};
                color: {c['text_primary']};
                border: 1px solid {c['border']};
                border-radius: {DesignSystem.RADIUS['md']}px;
                font-weight: 500;
                font-size: {DesignSystem.FONT_SIZES['lg']}px;
                padding: 8px 16px;
            }}
            QPushButton:hover {{
                background-color: {c['surface_hover']};
                border-color: {c['border_hover']};
            }}
            QPushButton:pressed {{
                background-color: {c['surface_pressed']};
            }}
        """)
        reset_date_btn.clicked.connect(self.reset_date_range)
        
        date_range_layout.addWidget(date_range_title)
        date_range_layout.addWidget(start_date_label)
        date_range_layout.addWidget(self.start_date_edit)
        date_range_layout.addWidget(to_label)
        date_range_layout.addWidget(self.end_date_edit)
        date_range_layout.addWidget(reset_date_btn)
        date_range_layout.addStretch()
        
        # 将标题和日期选择控件添加到同一行
        header_layout.addWidget(stats_title)
        header_layout.addLayout(date_range_layout)
        
        stats_main_layout.addLayout(header_layout)
        
        # 统计数据区域
        stats_layout = QHBoxLayout()
        
        # 总项目数统计
        project_count_layout = QVBoxLayout()
        project_count_layout.setAlignment(Qt.AlignCenter)
        
        self.project_count_label = QLabel("0")
        c = DesignSystem.COLORS
        self.project_count_label.setStyleSheet(f"""
            QLabel {{
                font-size: 34px;
                font-weight: 700;
                color: {c['primary']};
                letter-spacing: -0.5px;
            }}
        """)
        self.project_count_label.setAlignment(Qt.AlignCenter)
        
        project_count_title = QLabel("总项目数")
        c = DesignSystem.COLORS
        project_count_title.setStyleSheet(f"""
            QLabel {{
                font-size: 15px;
                color: {c['text_secondary']};
                font-weight: 500;
            }}
        """)
        project_count_title.setAlignment(Qt.AlignCenter)
        
        project_count_layout.addWidget(self.project_count_label)
        project_count_layout.addWidget(project_count_title)
        
        # 删除总资源文件类型数统计相关代码
        
        # 总资源数统计
        resource_count_layout = QVBoxLayout()
        resource_count_layout.setAlignment(Qt.AlignCenter)
        
        self.resource_count_label = QLabel("0")
        c = DesignSystem.COLORS
        self.resource_count_label.setStyleSheet(f"""
            QLabel {{
                font-size: 34px;
                font-weight: 700;
                color: {c['warning']};
                letter-spacing: -0.5px;
            }}
        """)
        self.resource_count_label.setAlignment(Qt.AlignCenter)
        
        resource_count_title = QLabel("总资源数")
        c = DesignSystem.COLORS
        resource_count_title.setStyleSheet(f"""
            QLabel {{
                font-size: 15px;
                color: {c['text_secondary']};
                font-weight: 500;
            }}
        """)
        resource_count_title.setAlignment(Qt.AlignCenter)
        
        resource_count_layout.addWidget(self.resource_count_label)
        resource_count_layout.addWidget(resource_count_title)
        
        # 添加到布局
        stats_layout.addLayout(project_count_layout)
        stats_layout.addLayout(resource_count_layout)
        
        # 添加资源清单按钮
        stats_button_layout = QVBoxLayout()
        stats_button_layout.setAlignment(Qt.AlignCenter)
        
        self.resource_inventory_btn = ModernButton("资源清单", "primary")
        c = DesignSystem.COLORS
        self.resource_inventory_btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {c['primary']};
                color: white;
                border: none;
                border-radius: {DesignSystem.RADIUS['sm']}px;
                font-weight: 500;
                padding: 8px 16px;
            }}
            QPushButton:hover {{
                background-color: {c['primary_hover']};
            }}
            QPushButton:pressed {{
                background-color: {c['primary_pressed']};
            }}
        """)
        self.resource_inventory_btn.clicked.connect(self.show_resource_inventory)
        
        stats_button_layout.addWidget(self.resource_inventory_btn)
        stats_layout.addLayout(stats_button_layout)
        
        stats_main_layout.addLayout(stats_layout)
        stats_card.addLayout(stats_main_layout)
        layout.addWidget(stats_card)
        
        # 项目列表区域
        project_card = ModernCard("项目列表")
        
        # 顶部操作区域（搜索框、项目类型筛选和新建按钮）
        top_layout = QHBoxLayout()
        
        # 搜索框
        self.search_input = ModernSearchBox("搜索项目...")
        self.search_input.textChanged.connect(self.on_search)
        top_layout.addWidget(self.search_input, 1)
        
        # 状态筛选下拉框
        self.status_filter_combo = QComboBox()
        self.status_filter_combo.setFixedHeight(36)
        self.status_filter_combo.addItem("全部状态")
        self.status_filter_combo.addItems(["未开始", "进行中", "已暂停", "已完成", "已取消"])
        c = DesignSystem.COLORS
        self.status_filter_combo.setStyleSheet(f"""
            QComboBox {{
                border: 1px solid {c['border']};
                border-radius: {DesignSystem.RADIUS['sm']}px;
                padding: 5px 10px;
                background-color: {c['surface']};
                min-width: 120px;
            }}
            QComboBox:hover {{
                border: 1px solid {c['border_hover']};
            }}
            QComboBox:focus {{
                border: 1px solid {c['primary']};
            }}
            QComboBox::drop-down {{
                subcontrol-origin: padding;
                subcontrol-position: center right;
                width: 25px;
                border-left: none;
            }}
            QComboBox::down-arrow {{
                image: url(icons/dropdown_arrow.png);
                width: 12px;
                height: 12px;
            }}
            QComboBox QAbstractItemView {{
                border: 1px solid {c['border']};
                border-radius: 0px;
                background-color: {c['surface']};
                selection-background-color: {c['primary_light']};
            }}
        """)
        self.status_filter_combo.currentIndexChanged.connect(self.on_status_filter_changed)
        top_layout.addWidget(self.status_filter_combo)
        
        # 项目类型筛选下拉框
        self.type_filter_combo = QComboBox()
        self.type_filter_combo.setFixedHeight(36)
        self.type_filter_combo.addItem("全部类型")
        
        # 获取实际项目中的类型
        project_types = self.get_project_types()
        if project_types:
            self.type_filter_combo.addItems(project_types)
        c = DesignSystem.COLORS
        self.type_filter_combo.setStyleSheet(f"""
            QComboBox {{
                border: 1px solid {c['border']};
                border-radius: {DesignSystem.RADIUS['sm']}px;
                padding: 5px 10px;
                background-color: {c['surface']};
                min-width: 120px;
            }}
            QComboBox:hover {{
                border: 1px solid {c['border_hover']};
            }}
            QComboBox:focus {{
                border: 1px solid {c['primary']};
            }}
            QComboBox::drop-down {{
                subcontrol-origin: padding;
                subcontrol-position: center right;
                width: 25px;
                border-left: none;
            }}
            QComboBox::down-arrow {{
                image: url(icons/dropdown_arrow.png);
                width: 12px;
                height: 12px;
            }}
            QComboBox QAbstractItemView {{
                border: 1px solid {c['border']};
                border-radius: 0px;
                background-color: {c['surface']};
                selection-background-color: {c['primary_light']};
            }}
        """)
        self.type_filter_combo.currentIndexChanged.connect(self.on_type_filter_changed)
        top_layout.addWidget(self.type_filter_combo)
        
        # 刷新项目列表按钮
        self.refresh_project_btn = ModernButton("🔄 刷新列表", "secondary")
        self.refresh_project_btn.clicked.connect(self.reload_data_and_refresh)
        top_layout.addWidget(self.refresh_project_btn)
        
        # 新建项目按钮
        self.new_project_btn = ModernButton("+ 新建项目", "primary")
        self.new_project_btn.clicked.connect(self.new_project)
        top_layout.addWidget(self.new_project_btn)
        
        project_card.addLayout(top_layout)
        
        # 项目表格
        # 使用自定义的支持拖拽的表格类
        self.project_table = ProjectTableWidget(self)
        self.project_table.setColumnCount(9)
        self.project_table.setHorizontalHeaderLabels([
            "项目编号", "项目名称", "项目类型", "状态", "资源文件数", 
            "项目标签", "创建时间", "最近修改时间", "操作"
        ])
        
        # 启用拖拽功能
        self.project_table.setAcceptDrops(True)
        self.project_table.viewport().setAcceptDrops(True)
        self.project_table.setDragDropMode(QAbstractItemView.DropOnly)
        
        # 设置表格样式 - 使用设计系统
        self.project_table.setStyleSheet(DesignSystem.table_style())
        
        # 设置表格属性
        self.project_table.setSelectionBehavior(QTableWidget.SelectRows)
        self.project_table.setAlternatingRowColors(True)
        self.project_table.verticalHeader().setVisible(False)
        self.project_table.horizontalHeader().setStretchLastSection(False)
        
        # 启用自动换行，确保项目名称和标签可以自动换行
        self.project_table.setWordWrap(True)
        
        # 禁用列宽调整
        self.project_table.horizontalHeader().setSectionsMovable(False)
        self.project_table.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        
        # 禁用水平滚动条，确保表格完全适应可见区域
        self.project_table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        
        # 设置行高，增加行高以容纳多行文本
        self.project_table.verticalHeader().setDefaultSectionSize(60)
        
        # 连接窗口大小变化事件，自动调整列宽
        self.project_table.horizontalHeader().geometriesChanged.connect(self.adjust_project_table_columns)
        
        # 连接选择事件
        self.project_table.itemSelectionChanged.connect(self.on_project_table_selected)
        
        # 禁用双击编辑功能
        self.project_table.setEditTriggers(QTableWidget.NoEditTriggers)
        
        # 连接双击事件到查看项目详情
        self.project_table.cellDoubleClicked.connect(self.on_project_table_double_clicked)
        
        # 设置右键菜单
        self.project_table.setContextMenuPolicy(Qt.CustomContextMenu)
        self.project_table.customContextMenuRequested.connect(self.show_project_context_menu)
        
        # 表格自动适应布局，不设置固定最小高度
        self.project_table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        project_card.addWidget(self.project_table)
        
        # 空状态组件
        self.project_empty_state = EmptyStateWidget(
            icon_text="📭",
            title="暂无项目",
            description="您还没有创建任何项目，点击下方按钮开始创建您的第一个项目",
            action_text="创建项目"
        )
        self.project_empty_state.set_action_callback(self.new_project)
        self.project_empty_state.hide()
        project_card.addWidget(self.project_empty_state)
        
        layout.addWidget(project_card)
        
        return panel
        
    def create_resource_file_type_panel(self):
        """创建资源文件类型面板"""
        panel = QWidget()
        layout = QVBoxLayout(panel)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(16)
        
        # 资源概览
        overview_card = ModernCard("资源概览")
        
        # 刷新按钮
        refresh_btn_layout = QHBoxLayout()
        self.refresh_types_btn = ModernButton("刷新类型", "secondary")
        self.refresh_types_btn.clicked.connect(self.refresh_type_combo)
        self.config_types_btn = ModernButton("配置文件类型", "primary")
        self.config_types_btn.clicked.connect(self.config_resource_types)
        refresh_btn_layout.addWidget(self.refresh_types_btn)
        refresh_btn_layout.addWidget(self.config_types_btn)
        refresh_btn_layout.addStretch()
        overview_card.addLayout(refresh_btn_layout)
        
        # 资源文件类型表格
        self.type_table = QTableWidget()
        self.type_table.setColumnCount(4)
        self.type_table.setHorizontalHeaderLabels([
            "资源文件类型", "文件数量", "扩展名", "最近修改时间"
        ])
        
        # 设置表头
        self.type_table.setHorizontalHeaderLabels(["类型名称", "文件数量", "支持扩展名"])
        
        # 设置表格样式 - 使用设计系统
        self.type_table.setStyleSheet(DesignSystem.table_style())
        
        # 设置表格属性
        self.type_table.setSelectionBehavior(QTableWidget.SelectRows)
        self.type_table.setAlternatingRowColors(True)
        self.type_table.verticalHeader().setVisible(False)
        self.type_table.horizontalHeader().setStretchLastSection(True)
        
        # 设置列宽
        header = self.type_table.horizontalHeader()
        header.resizeSection(0, 100)  # 资源文件类型
        header.resizeSection(1, 80)   # 文件数量
        header.resizeSection(2, 200)  # 资源路径
        
        # 连接选择事件
        self.type_table.itemSelectionChanged.connect(self.on_type_table_selected)
        
        self.type_table.setMinimumHeight(300)
        overview_card.addWidget(self.type_table)
        
        layout.addWidget(overview_card)
        
        # 资源详情区域
        detail_card = ModernCard("资源详情")
        detail_layout = QVBoxLayout()
        
        # 类型信息显示
        type_info_layout = QHBoxLayout()
        type_info_layout.addWidget(QLabel("选中类型:"))
        self.selected_type_label = QLabel("未选择类型")
        self.selected_type_label.setStyleSheet(DesignSystem.label_style('tag'))
        type_info_layout.addWidget(self.selected_type_label)
        type_info_layout.addStretch()
        detail_layout.addLayout(type_info_layout)
        
        # 文件列表
      
        self.type_file_tree = ModernTreeWidget()
        self.type_file_tree.setHeaderLabels(["文件名", "大小", "所属项目", "修改时间"])
        self.type_file_tree.itemDoubleClicked.connect(self.open_type_resource)
        detail_layout.addWidget(self.type_file_tree)
        
        detail_card.addLayout(detail_layout)
        layout.addWidget(detail_card)
        
        return panel
        
    def create_modern_project_detail_tab(self):
        """创建现代化项目详情标签页"""
        tab = QWidget()
        layout = QVBoxLayout(tab)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(16)
        
        # 项目信息卡片
        info_card = ModernCard("项目信息")
        
        # 项目名称
        name_layout = QHBoxLayout()
        name_icon = QLabel("📝")
        name_icon.setFixedSize(24, 24)
        name_layout.addWidget(name_icon)
        name_layout.addWidget(QLabel("项目名称:"))
        self.project_name_label = QLabel("未选择项目")
        c = DesignSystem.COLORS
        self.project_name_label.setStyleSheet(f"""
            QLabel {{
                font-weight: 600;
                font-size: 16px;
                color: {c['primary']};
                padding: 4px 8px;
                background-color: {c['primary_light']};
                border-radius: {DesignSystem.RADIUS['sm']}px;
            }}
        """)
        name_layout.addWidget(self.project_name_label)
        name_layout.addStretch()
        info_card.addLayout(name_layout)
        
        # 项目描述
        desc_layout = QHBoxLayout()
        desc_icon = QLabel("📄")
        desc_icon.setFixedSize(24, 24)
        desc_layout.addWidget(desc_icon)
        desc_layout.addWidget(QLabel("描述:"))
        self.project_desc_label = QLabel("")
        c = DesignSystem.COLORS
        self.project_desc_label.setStyleSheet(f"color: {c['text_secondary']}; font-style: italic;")
        desc_layout.addWidget(self.project_desc_label)
        desc_layout.addStretch()
        info_card.addLayout(desc_layout)
        
        # 项目标签
        tags_layout = QHBoxLayout()
        tags_icon = QLabel("🏷️")
        tags_icon.setFixedSize(24, 24)
        tags_layout.addWidget(tags_icon)
        tags_layout.addWidget(QLabel("标签:"))
        self.project_tags_label = QLabel("")
        c = DesignSystem.COLORS
        self.project_tags_label.setStyleSheet(f"""
            QLabel {{
                color: {c['success']};
                background-color: {c['success_light']};
                padding: 2px 8px;
                border-radius: {DesignSystem.RADIUS['lg']}px;
                font-size: {DesignSystem.FONT_SIZES['sm']}px;
            }}
        """)
        tags_layout.addWidget(self.project_tags_label)
        tags_layout.addStretch()
        info_card.addLayout(tags_layout)
        
        # 项目时间信息
        time_layout = QHBoxLayout()
        time_icon = QLabel("⏰")
        time_icon.setFixedSize(24, 24)
        time_layout.addWidget(time_icon)
        time_layout.addWidget(QLabel("时间信息:"))
        self.project_time_label = QLabel("")
        c = DesignSystem.COLORS
        self.project_time_label.setStyleSheet(f"""
            QLabel {{
                color: {c['text_secondary']};
                font-size: {DesignSystem.FONT_SIZES['sm']}px;
                font-style: italic;
            }}
        """)
        time_layout.addWidget(self.project_time_label)
        time_layout.addStretch()
        info_card.addLayout(time_layout)
        
        layout.addWidget(info_card)
        
        # 资源管理卡片
        resource_card = ModernCard("项目资源")
        
        # 资源操作按钮
        resource_btn_layout = QHBoxLayout()
        self.add_resource_btn = ModernButton("+ 添加资源", "primary")
        self.add_resource_btn.clicked.connect(self.add_resource_to_project)
        self.remove_resource_btn = ModernButton("- 移除资源", "danger")
        self.remove_resource_btn.clicked.connect(self.remove_resource_from_project)
        self.refresh_resource_btn = ModernButton("🔄 刷新时间", "secondary")
        self.refresh_resource_btn.clicked.connect(self.refresh_resource_times)
        resource_btn_layout.addWidget(self.add_resource_btn)
        resource_btn_layout.addWidget(self.remove_resource_btn)
        resource_btn_layout.addWidget(self.refresh_resource_btn)
        resource_btn_layout.addStretch()
        resource_card.addLayout(resource_btn_layout)
        
        # 资源树形视图
        self.resource_tree = ModernTreeWidget()
        self.resource_tree.setHeaderLabels(["资源名称", "修改时间", "文件路径"])
        self.resource_tree.itemDoubleClicked.connect(self.open_resource_file)
        self.resource_tree.setColumnWidth(0, 300)
        self.resource_tree.setColumnWidth(1, 150)
        resource_card.addWidget(self.resource_tree)
        
        layout.addWidget(resource_card)
        
        return tab
        
    def create_modern_resource_type_tab(self):
        """创建现代化资源文件类型标签页"""
        tab = QWidget()
        layout = QVBoxLayout(tab)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(16)
        
        # 类型选择卡片
        type_card = ModernCard("资源文件类型")
        
        type_layout = QHBoxLayout()
        type_layout.addWidget(QLabel("选择类型:"))
        self.type_combo = QComboBox()
        c = DesignSystem.COLORS
        self.type_combo.setStyleSheet(f"""
            QComboBox {{
                background-color: {c['surface']};
                border: 2px solid {c['border']};
                border-radius: {DesignSystem.RADIUS['md']}px;
                padding: 8px 12px;
                font-size: {DesignSystem.FONT_SIZES['lg']}px;
                min-width: 200px;
            }}
            QComboBox:focus {{
                border-color: {c['primary']};
            }}
            QComboBox::drop-down {{
                border: none;
                width: 30px;
            }}
            QComboBox::down-arrow {{
                image: none;
                border: 2px solid {c['text_secondary']};
                border-top: none;
                border-right: none;
                width: 6px;
                height: 6px;
                margin-right: 8px;
                transform: rotate(-45deg);
            }}
        """)
        self.type_combo.currentTextChanged.connect(self.on_type_selected)
        type_layout.addWidget(self.type_combo)
        
        batch_btn = ModernButton("批量添加到项目", "secondary")
        batch_btn.clicked.connect(self.batch_add_to_project)
        type_layout.addWidget(batch_btn)
        type_layout.addStretch()
        type_card.addLayout(type_layout)
        
        layout.addWidget(type_card)
        
        # 资源列表卡片
        resource_list_card = ModernCard("资源列表")
        self.type_resource_list = ModernListWidget()
        self.type_resource_list.itemDoubleClicked.connect(self.open_type_resource)
        resource_list_card.addWidget(self.type_resource_list)
        
        layout.addWidget(resource_list_card)
        
        return tab
        
    def create_modern_status_bar(self):
        """创建状态栏 - 使用统一设计系统"""
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        
        self.status_bar.setStyleSheet(DesignSystem.status_bar_style())
        
        self.status_bar.showMessage("就绪 - 个人知识管理工具")
        
        version_label = QLabel(f"v{self.TOOL_INFO['version']}")
        version_label.setStyleSheet(f"color: {DesignSystem.COLORS['text_secondary']}; margin-right: 12px;")
        self.status_bar.addPermanentWidget(version_label)
    
    # 以下方法保持原有逻辑，只是界面组件已经现代化
    def new_project(self):
        """新建项目"""
        dialog = ProjectDialog(self, project_types=self.project_types)
        if dialog.exec_() == QDialog.Accepted:
            project_data = dialog.get_project_data()
            current_time = datetime.now().isoformat()
            
            # 生成唯一的项目ID
            existing_ids = {project.get('id', 0) for project in self.projects}
            new_id = 1
            while new_id in existing_ids:
                new_id += 1
            project_data['id'] = new_id
            
            project_data['created_time'] = current_time
            project_data['modified_time'] = current_time
            project_data['resources'] = []
            project_data['auto_scan_resources'] = False  # 添加自动扫描资源配置字段，默认为False
      
            
            # 确保项目状态存在，默认为"未开始"
            if 'status' not in project_data:
                project_data['status'] = '未开始'
            
            # 处理文件夹创建或指定
            folder_created = False
            project_folder_path = ''
            
            if project_data.get('create_folder', False):
                # 用户选择创建项目文件夹
                folder_created, project_folder_path = self.create_project_folder(
                    project_data['name'], 
                    project_data.get('folder_path', '')
                )
                if folder_created:
                    project_data['folder_path'] = project_folder_path
            else:
                # 用户选择不创建项目文件夹，需要手动指定一个现有的项目文件夹路径
                folder_path = QFileDialog.getExistingDirectory(
                    self, 
                    "请选择项目文件夹", 
                    self.default_project_path or os.path.expanduser("~/Documents")
                )
                if folder_path:
                    project_data['folder_path'] = folder_path
                    project_folder_path = folder_path
                else:
                    # 用户取消了文件夹选择，不创建项目
                    QMessageBox.warning(self, "警告", "必须指定项目文件夹才能创建项目！")
                    return
                
            # 将项目添加到列表
            self.projects.append(project_data)
            
            # 记录项目日志
            self.add_project_log(project_data['name'], "创建项目", 
                               f"新建项目，类型：{project_data.get('type', '其他')}", 
                               "操作")
            
            # 保存项目数据
            try:
                self.save_data(create_backup=True)  # 新建项目时创建备份
                self.refresh_project_list()
                
                # 显示创建结果
                if project_data.get('create_folder', False):
                    if folder_created:
                        self.status_bar.showMessage(
                            f"✅ 项目 '{project_data['name']}' 创建成功，文件夹已创建：{project_folder_path}"
                        )
                    else:
                        self.status_bar.showMessage(
                            f"⚠️ 项目 '{project_data['name']}' 创建成功，但文件夹创建失败"
                        )
                else:
                    self.status_bar.showMessage(
                        f"✅ 项目 '{project_data['name']}' 创建成功，项目文件夹：{project_folder_path}"
                    )
            except Exception as e:
                # 如果保存失败，从列表中移除项目并显示错误
                self.projects.pop()
                QMessageBox.critical(self, "错误", f"保存项目数据失败：{str(e)}")
                logging.error(f"保存项目数据失败: {e}")
    
    def delete_project(self):
        """删除项目"""
        current_row = self.project_table.currentRow()
        if current_row < 0:
            QMessageBox.warning(self, "警告", "请先选择要删除的项目")
            return
        
        # 从项目名称列获取项目名称
        name_item = self.project_table.item(current_row, 1)
        if not name_item:
            QMessageBox.warning(self, "错误", "无法获取项目名称")
            return
            
        project_name = name_item.text()
        # 移除可能的前缀图标
        if project_name.startswith("📌 "):
            project_name = project_name[2:]  # 移除"📌 "前缀
        elif project_name.startswith("🆕 "):
            project_name = project_name[2:]  # 移除"🆕 "前缀
        
        # 找到项目数据
        project_to_delete = None
        project_index = -1
        for i, project in enumerate(self.projects):
            if project['name'] == project_name:
                project_to_delete = project
                project_index = i
                break
        
        if not project_to_delete:
            QMessageBox.warning(self, "错误", "未找到项目数据")
            return
        
        # 检查项目是否有关联的文件夹
        project_folder = project_to_delete.get('folder_path', '')
        if project_folder and os.path.exists(project_folder):
            # 创建自定义对话框询问是否删除文件夹
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("确认删除")
            msg_box.setText(f"确定要删除项目 '{project_name}' 吗？")
            msg_box.setInformativeText(f"项目文件夹路径：\n{project_folder}\n\n是否同时删除项目文件夹？")
            msg_box.setIcon(QMessageBox.Question)
            
            # 添加自定义按钮
            delete_with_folder_btn = msg_box.addButton("删除项目和文件夹", QMessageBox.YesRole)
            delete_only_project_btn = msg_box.addButton("仅删除项目数据", QMessageBox.NoRole)
            cancel_btn = msg_box.addButton("取消", QMessageBox.RejectRole)
            
            msg_box.setDefaultButton(delete_only_project_btn)
            msg_box.exec_()
            
            clicked_button = msg_box.clickedButton()
            
            if clicked_button == cancel_btn:
                return
            
            # 记录项目日志（在删除前记录）
            self.add_project_log(project_name, "删除项目", 
                               f"项目已被删除，包含 {len(project_to_delete.get('resources', []))} 个资源", 
                               "操作")
            
            # 删除项目数据
            del self.projects[project_index]
            
            # 如果用户选择同时删除项目文件夹
            if clicked_button == delete_with_folder_btn:
                try:
                    shutil.rmtree(project_folder)
                    self.status_bar.showMessage(f"🗑️ 项目 '{project_name}' 及其文件夹已删除")
                except Exception as e:
                    QMessageBox.warning(self, "警告", f"删除项目文件夹失败: {str(e)}")
                    self.status_bar.showMessage(f"🗑️ 项目 '{project_name}' 已删除，但文件夹删除失败")
            else:
                self.status_bar.showMessage(f"🗑️ 项目 '{project_name}' 已删除，文件夹保留")
        else:
            # 项目没有关联文件夹，直接确认删除
            reply = QMessageBox.question(self, "确认删除", 
                                      f"确定要删除项目 '{project_name}' 吗？\n此操作不可撤销。",
                                      QMessageBox.Yes | QMessageBox.No)
            
            if reply == QMessageBox.Yes:
                # 删除项目数据
                del self.projects[project_index]
                self.status_bar.showMessage(f"🗑️ 项目 '{project_name}' 已删除")
            else:
                return
        
        self.save_data(create_backup=True)  # 删除项目时创建备份
        self.refresh_project_list()
        # 清除选中的项目
        self.selected_project_name = None
        self.project_table.clearSelection()
    

    
    def add_resource_to_project_by_row(self, row):
        """按行添加资源到项目"""
        if row < 0 or row >= self.project_table.rowCount():
            QMessageBox.warning(self, "错误", "无效的项目行")
            return
        
        # 获取项目名称
        name_item = self.project_table.item(row, 1)
        if not name_item:
            QMessageBox.warning(self, "错误", "无法获取项目名称")
            return
        
        project_name = name_item.text()
        # 移除置顶图标前缀（如果存在）
        if project_name.startswith("📌 "):
            project_name = project_name[2:]  # 移除"📌 "前缀
        # 移除最新项目标识前缀（如果存在）
        if project_name.startswith("🆕 "):
            project_name = project_name[2:]  # 移除"🆕 "前缀
        # 移除最新项目标识前缀（如果存在）
        if project_name.startswith("🆕 "):
            project_name = project_name[2:]  # 移除"🆕 "前缀
        # 移除最新项目标识前缀（如果存在）
        if project_name.startswith("🆕 "):
            project_name = project_name[2:]  # 移除"🆕 "前缀
        # 移除最新项目标识前缀（如果存在）
        elif project_name.startswith("🆕 "):
            project_name = project_name[2:]  # 移除"🆕 "前缀
        
        project = self.find_project_by_name(project_name)
        if not project:
            QMessageBox.warning(self, "错误", "未找到项目")
            return
        
        # 直接打开添加资源对话框
        dialog = AddResourceDialog(self, self.resource_categories, self.resource_types)
        if dialog.exec_() == QDialog.Accepted:
            if 'resources' not in project:
                project['resources'] = []
            
            # 检查是否是批量添加
            if hasattr(dialog, 'batch_resources_data') and dialog.batch_resources_data:
                # 批量添加资源
                added_count = 0
                duplicate_count = 0
                
                for resource_data in dialog.batch_resources_data:
                    resource_name = resource_data.get('name', '')
                    resource_path = resource_data.get('path', '')
                    
                    # 检查重复（通过名称或路径）
                    is_duplicate = False
                    normalized_resource_path = os.path.normpath(resource_path) if resource_path else ''
                    for existing_resource in project['resources']:
                        existing_path = os.path.normpath(existing_resource.get('path', ''))
                        if (existing_resource.get('name') == resource_name and resource_name) or \
                           (existing_path == normalized_resource_path and normalized_resource_path):
                            duplicate_count += 1
                            is_duplicate = True
                            break
                    
                    if not is_duplicate:
                        project['resources'].append(resource_data)
                        added_count += 1
                
                self.update_project_modified_time(project['name'], save_immediately=False)
                self.save_data(create_backup=True)  # 批量添加资源时创建备份
                self.refresh_project_list()  # 刷新项目列表以更新资源数量
                
                # 显示批量添加结果
                message = f"✅ 成功添加 {added_count} 个资源到项目 '{project_name}'"
                if duplicate_count > 0:
                    message += f"，跳过 {duplicate_count} 个重复资源"
                self.status_bar.showMessage(message)
                
                # 刷新项目详情页面（如果已打开）
                for dialog in self.findChildren(ProjectDetailDialog):
                    if dialog.project['name'] == project_name:
                        dialog.load_resources()
                        dialog.update_tab_counts()  # 更新tab标题中的统计数
                        break
            else:
                # 单个资源添加
                # 先获取基础资源数据（不包含ID）
                resource_data = dialog.get_resource_data()
                resource_name = resource_data.get('name', '')
                resource_path = resource_data.get('path', '')
                
                # 使用统一的重复检查机制
                check_result = self.check_resource_duplicate_and_get_id(project, resource_name, resource_path)
                
                if check_result['is_duplicate']:
                    QMessageBox.warning(self, "重复资源", 
                                      f"资源 '{resource_name}' 已存在于项目中，无法重复添加。")
                    return
                
              
                
                # 添加资源
                project['resources'].append(resource_data)
                self.update_project_modified_time(project['name'], save_immediately=False)
                self.save_data(create_backup=True)  # 添加资源时创建备份
                self.refresh_project_list()  # 刷新项目列表以更新资源数量
                self.status_bar.showMessage(f"✅ 资源 '{resource_data['name']}' 已添加到项目 '{project_name}'")
                
                # 刷新项目详情页面（如果已打开）
                for dialog in self.findChildren(ProjectDetailDialog):
                    if dialog.project['name'] == project_name:
                        dialog.load_resources()
                        dialog.update_tab_counts()  # 更新tab标题中的统计数
                        break
    
    def on_project_table_selected(self):
        """项目表格选择事件"""
        current_row = self.project_table.currentRow()
        if current_row >= 0:
            # 从项目名称列获取项目名称
            name_item = self.project_table.item(current_row, 1)
            if name_item:
                self.selected_project_name = name_item.text()
                self.status_bar.showMessage(f"已选择项目: {self.selected_project_name}")
        else:
            self.selected_project_name = None
            self.status_bar.showMessage("就绪")
            

                        
    def view_project_detail_by_row(self, row):
        """通过行号查看项目详情"""
        if row < 0 or row >= self.project_table.rowCount():
            QMessageBox.warning(self, "警告", "无效的项目行号！")
            return
            
        # 从项目名称列获取项目名称
        name_item = self.project_table.item(row, 1)
        if not name_item:
            QMessageBox.warning(self, "错误", "无法获取项目名称")
            return
            
        project_name = name_item.text()
        # 移除置顶图标前缀（如果存在）
        if project_name.startswith("📌 "):
            project_name = project_name[2:]  # 移除"📌 "前缀
        # 移除最新项目标识前缀（如果存在）
        if project_name.startswith("🆕 "):
            project_name = project_name[2:]  # 移除"🆕 "前缀
        
        # 查找项目数据
        project = None
        for p in self.projects:
            if p['name'] == project_name:
                project = p
                break
        
        if not project:
            QMessageBox.warning(self, "错误", "未找到项目数据！")
            return
        
        # 加载该项目的笔记数据（按需加载，避免启动时加载所有项目笔记）
        self.load_project_from_markdown(project)
        
        # 创建并显示项目详情对话框
        detail_dialog = ProjectDetailDialog(self, project)
        # 添加到跟踪列表
        self.open_project_dialogs.append(detail_dialog)
        # 连接对话框关闭信号，从列表中移除
        detail_dialog.finished.connect(lambda: self.remove_project_dialog(detail_dialog))
        detail_dialog.exec_()
    
    def view_project_detail(self):
        """查看项目详情"""
        if not self.selected_project_name:
            QMessageBox.warning(self, "警告", "请先选择一个项目！")
            return
        
        # 查找项目数据
        project = None
        for p in self.projects:
            if p['name'] == self.selected_project_name:
                project = p
                break
        
        if not project:
            QMessageBox.warning(self, "错误", "未找到项目数据！")
            return
        
        # 加载该项目的笔记数据（按需加载，避免启动时加载所有项目笔记）
        self.load_project_from_markdown(project)
        
        # 创建并显示项目详情对话框
        detail_dialog = ProjectDetailDialog(self, project)
        # 添加到跟踪列表
        self.open_project_dialogs.append(detail_dialog)
        # 连接对话框关闭信号，从列表中移除
        detail_dialog.finished.connect(lambda: self.remove_project_dialog(detail_dialog))
        detail_dialog.exec_()
    
    def edit_project(self):
        """编辑项目"""
        if not self.selected_project_name:
            QMessageBox.warning(self, "警告", "请先选择一个项目！")
            return
        
        # 查找项目数据
        project = None
        project_index = -1
        for i, p in enumerate(self.projects):
            if p['name'] == self.selected_project_name:
                project = p
                project_index = i
                break
        
        if not project:
            QMessageBox.warning(self, "错误", "未找到项目数据！")
            return
        
        # 创建编辑对话框
        dialog = ProjectDialog(self, self.project_types, project)
        if dialog.exec_() == QDialog.Accepted:
            # 获取编辑后的数据
            updated_data = dialog.get_project_data()
            
            # 确保项目状态存在，默认为"未开始"
            if 'status' not in updated_data:
                updated_data['status'] = project.get('status', '未开始')
            
            # 检查项目名称是否发生变化，如果是则重命名文件夹
            old_name = project.get('name')
            new_name = updated_data.get('name')
            folder_renamed = False
            
            if old_name and new_name and old_name != new_name:
                # 如果项目有文件夹，尝试重命名
                if project.get('folder_path') and os.path.exists(project.get('folder_path')):
                    new_folder_path = self.rename_project_folder(project, old_name, new_name)
                    if new_folder_path:
                        updated_data['folder_path'] = new_folder_path
                        folder_renamed = True
                    else:
                        # 如果重命名失败，保持原有的文件夹路径
                        updated_data['folder_path'] = project.get('folder_path')
                        logging.warning(f"项目文件夹重命名失败，保持原路径: {project.get('folder_path')}")
                elif project.get('folder_path'):
                    # 如果项目有文件夹路径但文件夹不存在，保持原路径记录
                    updated_data['folder_path'] = project.get('folder_path')
                    logging.warning(f"项目文件夹不存在，保持原路径记录: {project.get('folder_path')}")
                
            # 处理文件夹创建逻辑（针对历史项目）
            folder_created = False
            project_folder_path = ''
            notes_migrated = False
            
            # 检查是否需要创建项目文件夹
            if updated_data.get('create_folder', False):
                # 检查项目是否已经有文件夹路径
                existing_folder = project.get('folder_path', '')
                new_parent_path = updated_data.get('folder_path', '')
                
                if not existing_folder or not os.path.exists(existing_folder):
                    # 项目没有文件夹或文件夹不存在，需要创建新文件夹
                    if new_parent_path:
                        folder_created, project_folder_path = self.create_project_folder(
                            updated_data['name'], 
                            new_parent_path
                        )
                        if folder_created:
                            updated_data['folder_path'] = project_folder_path
                        else:
                            QMessageBox.warning(self, "警告", "项目文件夹创建失败！")
                    else:
                        QMessageBox.warning(self, "警告", "请指定项目文件夹的父目录！")
                else:
                    # 项目已有文件夹，检查是否需要迁移到新位置
                    if new_parent_path and new_parent_path != os.path.dirname(existing_folder):
                        # 用户指定了新的父目录，需要迁移项目文件夹
                        new_folder_path = self.migrate_project_notes(
                            project, updated_data['name'], existing_folder, new_parent_path
                        )
                        if new_folder_path:
                            # 更新项目文件夹路径为实际的新路径
                            project_folder_path = new_folder_path
                            updated_data['folder_path'] = new_folder_path
                            notes_migrated = True
                    else:
                        # 项目已有文件夹，保持原路径
                        updated_data['folder_path'] = existing_folder
            
            # 检查哪些字段发生了变化
            changes = []
            old_data = project
            folder_renamed = False
            
            # 检查项目名称是否发生变化，如果是则重命名文件夹
            if 'name' in updated_data and updated_data['name'] != old_data.get('name'):
                old_name = old_data.get('name')
                new_name = updated_data['name']
                
                # 如果项目有文件夹，尝试重命名
                if project.get('folder_path') and os.path.exists(project.get('folder_path')):
                    new_folder_path = self.rename_project_folder(project, old_name, new_name)
                    if new_folder_path:
                        updated_data['folder_path'] = new_folder_path
                        folder_renamed = True
                    else:
                        # 如果重命名失败，保持原有的文件夹路径
                        updated_data['folder_path'] = project.get('folder_path')
                        logging.warning(f"项目文件夹重命名失败，保持原路径: {project.get('folder_path')}")
                elif project.get('folder_path'):
                    # 如果项目有文件夹路径但文件夹不存在，保持原路径记录
                    updated_data['folder_path'] = project.get('folder_path')
                    logging.warning(f"项目文件夹不存在，保持原路径记录: {project.get('folder_path')}")
            
            for key, new_value in updated_data.items():
                old_value = old_data.get(key)
                if old_value != new_value:
                    if key == 'name':
                        if folder_renamed:
                            changes.append(f"项目名称：{old_value} → {new_value}（文件夹已同步重命名）")
                        else:
                            changes.append(f"项目名称：{old_value} → {new_value}")
                    elif key == 'description':
                        changes.append(f"项目描述已更新")
                    elif key == 'type':
                        changes.append(f"项目类型：{old_value} → {new_value}")
                    elif key == 'status':
                        changes.append(f"项目状态：{old_value} → {new_value}")
                    elif key == 'tags':
                        changes.append(f"项目标签已更新")
                    elif key == 'folder_path':
                        if folder_created:
                            changes.append(f"项目文件夹已创建：{new_value}")
                        elif notes_migrated:
                            changes.append(f"项目文件夹已迁移：{new_value}")
                        elif not folder_renamed:  # 避免重复记录文件夹变更
                            changes.append(f"项目文件夹路径已更新：{new_value}")
            
            # 更新项目数据
            self.projects[project_index].update(updated_data)
            self.projects[project_index]['modified_time'] = datetime.now().isoformat()
            
            # 如果文件夹路径发生了变化，重新加载markdown文件数据
            if 'folder_path' in updated_data and updated_data['folder_path'] != project.get('folder_path'):
                try:
                    # 重新加载项目的markdown数据
                    updated_project = self.projects[project_index]
                    folder_path = updated_project.get('folder_path', '')
                    if folder_path and os.path.exists(folder_path):
                        project_name = updated_project['name']
                        safe_name = "".join(c for c in project_name if c.isalnum() or c in (' ', '-', '_', '（', '）', '(', ')')).strip()
                        if not safe_name:
                            safe_name = "新项目"
                        notes_file = os.path.join(folder_path, f"{safe_name}_笔记.md")
                        
                        if os.path.exists(notes_file):
                            with open(notes_file, 'r', encoding='utf-8') as f:
                                content = f.read()
                            # 这里可以解析markdown内容并更新项目数据
                            # 但为了简化，我们只确保路径更新正确
                except Exception as e:
                    logging.error(f"重新加载markdown数据失败: {e}")
            
            # 记录项目日志
            if changes:
                change_details = "；".join(changes)
                self.add_project_log(updated_data['name'], "编辑项目", 
                                   f"项目信息已更新：{change_details}", 
                                   "操作")
            
            # 保存数据
            self.save_data()
            
            # 刷新界面
            self.refresh_project_list()
            
            # 更新状态栏
            if folder_created:
                self.status_bar.showMessage(f"项目 '{updated_data['name']}' 已更新，文件夹已创建：{project_folder_path}", 3000)
            elif notes_migrated:
                self.status_bar.showMessage(f"项目 '{updated_data['name']}' 已更新，文件夹已迁移：{project_folder_path}", 3000)
            else:
                self.status_bar.showMessage(f"项目 '{updated_data['name']}' 已更新", 3000)
            
            # 如果项目名称发生变化，更新选中状态
            if updated_data['name'] != self.selected_project_name:
                self.selected_project_name = updated_data['name']
                # 重新选中项目
                for row in range(self.project_table.rowCount()):
                    if self.project_table.item(row, 0).text() == self.selected_project_name:
                        self.project_table.selectRow(row)
                        break
    

    
    def get_file_icon(self, file_path):
        """根据文件扩展名获取图标"""
        if not os.path.exists(file_path):
            return "❌"
        
        _, ext = os.path.splitext(file_path.lower())
        icon_map = {
            '.pdf': '📄',
            '.doc': '📝', '.docx': '📝',
            '.txt': '📃', '.md': '📃',
            '.py': '🐍', '.js': '📜', '.html': '🌐', '.css': '🎨',
            '.mp4': '🎬', '.avi': '🎬', '.mkv': '🎬', '.mov': '🎬',
            '.jpg': '🖼️', '.png': '🖼️', '.gif': '🖼️',
            '.zip': '📦', '.rar': '📦',
            '.exe': '⚙️',
            '.url': '🔗'
        }
        return icon_map.get(ext, '📄')
    
    def get_file_time_info(self, file_path):
        """获取文件时间信息"""
        try:
            if os.path.exists(file_path):
                mtime = os.path.getmtime(file_path)
                return datetime.fromtimestamp(mtime).strftime('%Y-%m-%d %H:%M')
            else:
                return "文件不存在"
        except:
            return "未知时间"
    
    def get_file_modification_time(self, file_path):
        """获取文件修改时间戳"""
        try:
            if os.path.exists(file_path):
                return os.path.getmtime(file_path)
            else:
                return 0
        except:
            return 0
    
    def is_recently_modified(self, timestamp):
        """判断文件是否在24小时内修改过"""
        if timestamp == 0:
            return False
        current_time = datetime.now().timestamp()
        return (current_time - timestamp) < 86400  # 24小时 = 86400秒
    
    def open_resource_file(self, item, column):
        """双击打开资源文件"""
        file_path = item.data(0, Qt.UserRole)
        if file_path and os.path.exists(file_path):
            try:
                if sys.platform.startswith('win'):
                    os.startfile(file_path)
                elif sys.platform.startswith('darwin'):  # macOS
                    subprocess.run(['open', file_path])
                else:  # Linux
                    subprocess.run(['xdg-open', file_path])
                self.status_bar.showMessage(f"📂 已打开文件: {os.path.basename(file_path)}")
            except Exception as e:
                QMessageBox.warning(self, "打开失败", f"无法打开文件:\n{str(e)}")
        else:
            QMessageBox.warning(self, "文件不存在", "文件路径无效或文件不存在")
    
    def update_project_modified_time(self, project_name, save_immediately=False):
        """更新项目修改时间
        
        Args:
            project_name (str): 项目名称
            save_immediately (bool): 是否立即保存数据，默认为False
        """
        for project in self.projects:
            if project['name'] == project_name:
                project['modified_time'] = datetime.now().isoformat()
                if save_immediately:
                    self.save_data(create_backup=True)  # 更新项目修改时间时创建备份
                break
    
    def add_project_log(self, project_name, action, details="", log_type="操作"):
        """添加项目日志到项目的md笔记文件中"""
        project = self.find_project_by_name(project_name)
        if not project:
            return
        
        # 获取项目文件夹路径
        folder_path = project.get('folder_path', '')
        if not folder_path or not os.path.exists(folder_path):
            return
        
        # 构建笔记文件路径
        safe_name = "".join(c for c in project_name if c.isalnum() or c in (' ', '-', '_', '（', '）', '(', ')')).strip()
        if not safe_name:
            safe_name = "新项目"
        notes_file = os.path.join(folder_path, f"{safe_name}_笔记.md")
        
        # 如果笔记文件不存在，创建基础结构
        if not os.path.exists(notes_file):
            self.create_project_notes_file(project_name, notes_file)
        
        try:
            # 读取现有内容
            with open(notes_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 创建日志条目
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            log_entry = f"- **{timestamp}** [{log_type}] {action}"
            if details:
                log_entry += f" - {details}"
            log_entry += "\n"
            
            # 查找或创建项目日志部分
            log_section_marker = "## 项目日志\n"
            if log_section_marker in content:
                # 在现有日志部分的开头插入新日志
                parts = content.split(log_section_marker, 1)
                if len(parts) == 2:
                    before_log = parts[0] + log_section_marker
                    after_log = parts[1]
                    
                    # 在日志部分开头插入新条目
                    content = before_log + "\n" + log_entry + after_log
                else:
                    # 如果分割失败，在文件末尾添加
                    content += "\n" + log_section_marker + "\n" + log_entry
            else:
                # 在文件末尾添加日志部分
                content += "\n" + log_section_marker + "\n" + log_entry
            
            # 写回文件
            with open(notes_file, 'w', encoding='utf-8') as f:
                f.write(content)
                
        except Exception as e:
            logging.error(f"写入项目日志失败: {e}")
    
    def create_project_notes_file(self, project_name, notes_file):
        """创建项目笔记文件的基础结构"""
        try:
            content = f"# {project_name} 项目笔记\n\n"
            content += f"**创建时间：** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
            content += "## 项目概述\n\n"
            content += "在这里记录项目的基本信息和概述...\n\n"
            content += "## 项目笔记\n\n"
            content += "在这里记录项目相关的笔记内容...\n\n"
            content += "## 待办事项\n\n"
            content += "- [ ] 待办事项1\n"
            content += "- [ ] 待办事项2\n"
            content += "- [ ] 待办事项3\n\n"
            content += "## 项目进展\n\n"
            content += "在这里记录项目的进展情况...\n\n"
            content += "## 资源缓存信息\n\n"
            content += "<!-- 此部分由系统自动维护，请勿手动修改 -->\n"
            content += "```json\n"
            content += "{\n"
            content += '  "cache_version": "1.0",\n'
            content += f'  "last_updated": "{datetime.now().isoformat()}",\n'
            content += '  "resources_cache": {}\n'
            content += "}\n"
            content += "```\n\n"
            content += "## 项目日志\n\n"
            
            with open(notes_file, 'w', encoding='utf-8') as f:
                f.write(content)
        except Exception as e:
            logging.error(f"创建项目笔记文件失败: {e}")
    
    def read_resources_cache(self, notes_file):
        """从项目笔记中读取资源缓存信息"""
        try:
            if not os.path.exists(notes_file):
                return None
            
            with open(notes_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 查找资源缓存信息部分
            cache_start = content.find('## 资源缓存信息')
            if cache_start == -1:
                return None
            
            # 查找JSON代码块
            json_start = content.find('```json', cache_start)
            if json_start == -1:
                return None
            
            json_end = content.find('```', json_start + 7)
            if json_end == -1:
                return None
            
            json_content = content[json_start + 7:json_end].strip()
            cache_data = json.loads(json_content)
            
            return cache_data
        except Exception as e:
            logging.error(f"读取资源缓存失败: {e}")
            return None
    
    def update_resources_cache(self, notes_file, resources_cache):
        """更新项目笔记中的资源缓存信息"""
        try:
            if not os.path.exists(notes_file):
                return False
            
            with open(notes_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 查找资源缓存信息部分
            cache_start = content.find('## 资源缓存信息')
            if cache_start == -1:
                return False
            
            # 查找JSON代码块
            json_start = content.find('```json', cache_start)
            if json_start == -1:
                return False
            
            json_end = content.find('```', json_start + 7)
            if json_end == -1:
                return False
            
            # 构建新的缓存数据
            cache_data = {
                "cache_version": "1.0",
                "last_updated": datetime.now().isoformat(),
                "resources_cache": resources_cache
            }
            
            # 替换JSON内容
            new_json_content = json.dumps(cache_data, ensure_ascii=False, indent=2)
            new_content = content[:json_start + 7] + "\n" + new_json_content + "\n" + content[json_end:]
            
            with open(notes_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            return True
        except Exception as e:
            logging.error(f"更新资源缓存失败: {e}")
            return False
    
    def get_project_notes_file(self, project_name):
        """获取项目笔记文件路径"""
        try:
            if not project_name:
                return None
            
            # 构建项目笔记文件路径
            notes_filename = f"{project_name}_项目笔记.md"
            notes_file = os.path.join(self.notes_dir, notes_filename)
            
            return notes_file
        except Exception as e:
            logging.error(f"获取项目笔记文件路径失败: {e}")
            return None
    
    def rename_project_folder(self, project, old_name, new_name):
        """当项目名称变更时重命名项目文件夹"""
        try:
            folder_path = project.get('folder_path', '')
            if not folder_path or not os.path.exists(folder_path):
                return None
            
            # 生成新的安全文件夹名称
            new_safe_name = "".join(c for c in new_name if c.isalnum() or c in (' ', '-', '_', '（', '）', '(', ')')).strip()
            if not new_safe_name:
                new_safe_name = "新项目"
            
            # 获取父目录路径
            parent_path = os.path.dirname(folder_path)
            new_folder_path = os.path.join(parent_path, new_safe_name)
            
            # 如果新文件夹名称与当前相同，只需要更新笔记文件内容
            if new_folder_path == folder_path:
                # 即使文件夹名称相同，也需要检查并更新笔记文件内容
                old_safe_name = "".join(c for c in old_name if c.isalnum() or c in (' ', '-', '_', '（', '）', '(', ')')).strip()
                if not old_safe_name:
                    old_safe_name = "新项目"
                
                notes_file = os.path.join(folder_path, f"{old_safe_name}_笔记.md")
                new_notes_file = os.path.join(folder_path, f"{new_safe_name}_笔记.md")
                
                if os.path.exists(notes_file):
                    try:
                        # 如果笔记文件名需要更改，先直接移动文件
                        if notes_file != new_notes_file:
                            import shutil
                            shutil.move(notes_file, new_notes_file)
                            logging.info(f"成功移动笔记文件: {notes_file} -> {new_notes_file}")
                        
                        # 移动成功后，如果需要更新项目名称或添加重命名日志，再打开文件修改
                        need_update = False
                        
                        # 读取文件内容（使用新文件路径或原路径，取决于是否移动了文件）
                        file_to_read = new_notes_file if notes_file != new_notes_file else notes_file
                        with open(file_to_read, 'r', encoding='utf-8') as f:
                            content = f.read()
                        
                        # 更新标题
                        if content:
                            new_content = content.replace(f"# {old_name} 项目笔记", f"# {new_name} 项目笔记", 1)
                            if new_content != content:
                                content = new_content
                                need_update = True
                        
                        # 添加重命名日志
                        if content:  # 确保文件有内容
                            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                            rename_log = f"- **{timestamp}** [系统] 项目重命名 - 从 '{old_name}' 重命名为 '{new_name}'\n"
                            
                            # 查找项目日志部分并添加重命名记录
                            log_section_marker = "## 项目日志\n"
                            if log_section_marker in content:
                                parts = content.split(log_section_marker, 1)
                                if len(parts) == 2:
                                    before_log = parts[0] + log_section_marker
                                    after_log = parts[1]
                                    new_content = before_log + "\n" + rename_log + after_log
                                else:
                                    new_content = content + "\n" + log_section_marker + "\n" + rename_log
                            else:
                                new_content = content + "\n" + log_section_marker + "\n" + rename_log
                            
                            if new_content != content:
                                content = new_content
                                need_update = True
                        
                        # 如果需要更新文件内容，写入文件
                        if need_update and content:
                            file_to_write = new_notes_file if notes_file != new_notes_file else notes_file
                            with open(file_to_write, 'w', encoding='utf-8') as f:
                                f.write(content)
                            logging.info(f"更新了笔记文件的内容: {file_to_write}")
                                
                    except Exception as e:
                        logging.error(f"更新笔记文件内容失败: {e}")
                        
                return folder_path
            
            # 如果新文件夹已存在，添加数字后缀
            counter = 1
            original_new_folder = new_folder_path
            while os.path.exists(new_folder_path):
                new_folder_path = f"{original_new_folder}_{counter}"
                counter += 1
            
            # 重命名文件夹
            import shutil
            shutil.move(folder_path, new_folder_path)
            
            # 更新笔记文件中的项目名称
            old_safe_name = "".join(c for c in old_name if c.isalnum() or c in (' ', '-', '_', '（', '）', '(', ')')).strip()
            if not old_safe_name:
                old_safe_name = "新项目"
            
            old_notes_file = os.path.join(new_folder_path, f"{old_safe_name}_笔记.md")
            new_notes_file = os.path.join(new_folder_path, f"{new_safe_name}_笔记.md")
            
            # 重命名笔记文件并更新内容
            if os.path.exists(old_notes_file):
                try:
                    # 如果文件名不同，先直接移动文件
                    if old_notes_file != new_notes_file:
                        shutil.move(old_notes_file, new_notes_file)
                        logging.info(f"成功移动笔记文件: {old_notes_file} -> {new_notes_file}")
                    
                    # 移动成功后，如果需要更新项目名称或添加重命名日志，再打开文件修改
                    need_update = False
                    
                    # 读取文件内容
                    with open(new_notes_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # 更新标题
                    if content:
                        new_content = content.replace(f"# {old_name} 项目笔记", f"# {new_name} 项目笔记", 1)
                        if new_content != content:
                            content = new_content
                            need_update = True
                    
                    # 添加重命名日志
                    if content:  # 确保文件有内容
                        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        rename_log = f"- **{timestamp}** [系统] 项目重命名 - 从 '{old_name}' 重命名为 '{new_name}'\n"
                        
                        # 查找项目日志部分并添加重命名记录
                        log_section_marker = "## 项目日志\n"
                        if log_section_marker in content:
                            parts = content.split(log_section_marker, 1)
                            if len(parts) == 2:
                                before_log = parts[0] + log_section_marker
                                after_log = parts[1]
                                new_content = before_log + "\n" + rename_log + after_log
                            else:
                                new_content = content + "\n" + log_section_marker + "\n" + rename_log
                        else:
                            new_content = content + "\n" + log_section_marker + "\n" + rename_log
                        
                        if new_content != content:
                            content = new_content
                            need_update = True
                    
                    # 如果需要更新文件内容，写入文件
                    if need_update and content:
                        with open(new_notes_file, 'w', encoding='utf-8') as f:
                            f.write(content)
                        logging.info(f"更新了笔记文件的内容: {new_notes_file}")
                        
                except Exception as e:
                    logging.error(f"更新笔记文件失败: {e}")
                    # 如果更新失败，尝试直接移动文件
                    if old_notes_file != new_notes_file:
                        try:
                            shutil.move(old_notes_file, new_notes_file)
                            logging.info(f"使用移动方式重命名笔记文件: {old_notes_file} -> {new_notes_file}")
                        except Exception as e2:
                            logging.error(f"移动笔记文件失败: {e2}")
                            # 如果移动失败，尝试复制
                            try:
                                shutil.copy2(old_notes_file, new_notes_file)
                                logging.info(f"使用复制方式重命名笔记文件: {old_notes_file} -> {new_notes_file}")
                                # 复制成功后尝试删除原文件
                                if os.path.exists(new_notes_file):
                                    try:
                                        os.remove(old_notes_file)
                                        logging.info(f"复制后删除原笔记文件: {old_notes_file}")
                                    except Exception as e3:
                                        logging.error(f"删除原笔记文件失败: {e3}")
                            except Exception as e3:
                                logging.error(f"复制笔记文件也失败: {e3}")
            
            return new_folder_path
            
        except Exception as e:
            logging.error(f"重命名项目文件夹失败: {e}")
            return None
    
    def migrate_project_notes(self, project, new_project_name, old_folder_path, new_parent_path):
        """迁移项目笔记到新的文件夹位置"""
        try:
            # 生成安全的项目名称
            safe_name = "".join(c for c in new_project_name if c.isalnum() or c in (' ', '-', '_', '（', '）', '(', ')')).strip()
            if not safe_name:
                safe_name = "新项目"
            
            # 创建新的项目文件夹
            new_folder_path = os.path.join(new_parent_path, safe_name)
            
            # 如果新文件夹已存在，添加数字后缀
            counter = 1
            original_new_folder = new_folder_path
            while os.path.exists(new_folder_path):
                new_folder_path = f"{original_new_folder}_{counter}"
                counter += 1
            
            # 创建新文件夹
            os.makedirs(new_folder_path, exist_ok=True)
            
            # 查找原有的笔记文件
            old_project_name = project.get('name', new_project_name)
            old_safe_name = "".join(c for c in old_project_name if c.isalnum() or c in (' ', '-', '_', '（', '）', '(', ')')).strip()
            if not old_safe_name:
                old_safe_name = "新项目"
            
            old_notes_file = os.path.join(old_folder_path, f"{old_safe_name}_笔记.md")
            new_notes_file = os.path.join(new_folder_path, f"{safe_name}_笔记.md")
            
            # 迁移笔记文件
            if os.path.exists(old_notes_file):
                try:
                    # 直接使用shutil.move移动笔记文件
                    import shutil
                    shutil.move(old_notes_file, new_notes_file)
                    logging.info(f"成功移动笔记文件: {old_notes_file} -> {new_notes_file}")
                    
                    # 移动成功后，如果需要更新项目名称或添加迁移日志，再打开文件修改
                    need_update = False
                    
                    # 读取移动后的文件内容
                    try:
                        with open(new_notes_file, 'r', encoding='utf-8') as f:
                            content = f.read()
                        
                        # 如果项目名称发生变化，更新笔记文件中的标题
                        if old_project_name != new_project_name and content:
                            new_content = content.replace(f"# {old_project_name} 项目笔记", f"# {new_project_name} 项目笔记", 1)
                            if new_content != content:
                                content = new_content
                                need_update = True
                        
                        # 添加迁移日志
                        if content:  # 确保文件有内容
                            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                            migration_log = f"- **{timestamp}** [系统] 项目文件夹迁移 - 从 {old_folder_path} 迁移到 {new_folder_path}\n"
                            
                            # 查找项目日志部分并添加迁移记录
                            log_section_marker = "## 项目日志\n"
                            if log_section_marker in content:
                                parts = content.split(log_section_marker, 1)
                                if len(parts) == 2:
                                    before_log = parts[0] + log_section_marker
                                    after_log = parts[1]
                                    new_content = before_log + migration_log + after_log
                                else:
                                    new_content = content + "\n" + log_section_marker + "\n" + migration_log
                            else:
                                new_content = content + "\n" + log_section_marker + "\n" + migration_log
                            
                            if new_content != content:
                                content = new_content
                                need_update = True
                        
                        # 如果需要更新文件内容，写入文件
                        if need_update and content:
                            # 先备份原始内容
                            original_content = content
                            
                            # 写入更新后的内容
                            with open(new_notes_file, 'w', encoding='utf-8') as f:
                                f.write(content)
                            
                            # 验证写入是否成功
                            if os.path.exists(new_notes_file):
                                with open(new_notes_file, 'r', encoding='utf-8') as f:
                                    new_file_content = f.read()
                                
                                # 检查新文件内容是否完整
                                if not new_file_content or len(new_file_content) < len(original_content) * 0.9:
                                    logging.error(f"写入的笔记文件内容不完整: {new_notes_file}")
                                    # 恢复原始内容
                                    with open(new_notes_file, 'w', encoding='utf-8') as f:
                                        f.write(original_content)
                                else:
                                    logging.info(f"成功更新了笔记文件的内容: {new_notes_file}")
                            else:
                                logging.error(f"更新后的笔记文件不存在: {new_notes_file}")
                    except Exception as e:
                        logging.error(f"读取或更新笔记文件内容失败: {e}")
                        # 如果读取或更新失败，至少文件已经被移动了，不需要额外处理
                    
                except Exception as e:
                    logging.error(f"移动笔记文件失败: {e}")
                    # 如果移动失败，尝试复制
                    try:
                        import shutil
                        shutil.copy2(old_notes_file, new_notes_file)
                        logging.info(f"使用复制方式迁移笔记文件: {old_notes_file} -> {new_notes_file}")
                        # 复制成功后尝试删除原文件
                        if os.path.exists(new_notes_file):
                            try:
                                os.remove(old_notes_file)
                                logging.info(f"复制后删除原笔记文件: {old_notes_file}")
                            except Exception as e3:
                                logging.error(f"删除原笔记文件失败: {e3}")
                    except Exception as e2:
                        logging.error(f"复制笔记文件也失败: {e2}")
            else:
                # 如果原来没有笔记文件，创建新的
                self.create_project_notes_file(new_project_name, new_notes_file)
            
            # 迁移其他文件（如果有的话）
            try:
                if os.path.exists(old_folder_path):
                    import shutil
                    for item in os.listdir(old_folder_path):
                        if item.endswith('_笔记.md'):
                            continue  # 笔记文件已经处理过了
                        
                        old_item_path = os.path.join(old_folder_path, item)
                        new_item_path = os.path.join(new_folder_path, item)
                        
                        if os.path.isfile(old_item_path):
                            # 使用move而不是copy2，确保文件被移动而不是复制
                            shutil.move(old_item_path, new_item_path)
                            logging.info(f"移动文件: {old_item_path} -> {new_item_path}")
                        elif os.path.isdir(old_item_path):
                            # 对于目录，先复制再删除，以确保数据安全
                            shutil.copytree(old_item_path, new_item_path)
                            # 确认目录复制成功后删除原目录
                            if os.path.exists(new_item_path):
                                shutil.rmtree(old_item_path)
                                logging.info(f"移动目录: {old_item_path} -> {new_item_path}")
                            else:
                                logging.error(f"目录复制失败，保留原目录: {old_item_path}")
            except Exception as e:
                logging.error(f"迁移其他文件失败: {e}")
            
            # 尝试删除原有的文件夹（确保所有文件都已成功迁移）
            try:
                if os.path.exists(old_folder_path):
                    # 检查是否还有未迁移的重要文件
                    remaining_files = []
                    for root, dirs, files in os.walk(old_folder_path):
                        for file in files:
                            if not file.startswith('.'):  # 忽略隐藏文件
                                # 检查是否是笔记文件（已经处理过的）
                                if file.endswith('_笔记.md'):
                                    # 如果笔记文件还存在，说明迁移可能失败了
                                    old_notes_path = os.path.join(root, file)
                                    # 检查新位置是否已有对应的笔记文件
                                    if os.path.exists(new_notes_file):
                                        # 如果新笔记文件存在，尝试再次删除旧笔记文件
                                        try:
                                            os.remove(old_notes_path)
                                            logging.info(f"删除残留的旧笔记文件: {old_notes_path}")
                                            continue  # 跳过添加到remaining_files
                                        except Exception as e:
                                            logging.error(f"删除残留的旧笔记文件失败: {e}")
                                remaining_files.append(os.path.join(root, file))
                    
                    if not remaining_files:
                        # 如果没有剩余文件，删除整个文件夹
                        import shutil
                        shutil.rmtree(old_folder_path)
                        logging.info(f"成功删除原文件夹: {old_folder_path}")
                    else:
                        logging.warning(f"原文件夹中还有未迁移的文件，保留文件夹: {old_folder_path}")
                        logging.warning(f"剩余文件数量: {len(remaining_files)}")
                        # 记录前5个剩余文件作为示例
                        for i, file in enumerate(remaining_files[:5]):
                            logging.warning(f"剩余文件 {i+1}: {file}")
                        
                        # 尝试将剩余文件移动到新位置
                        import shutil
                        moved_count = 0
                        for file_path in remaining_files:
                            try:
                                # 计算相对路径，以保持目录结构
                                rel_path = os.path.relpath(file_path, old_folder_path)
                                new_file_path = os.path.join(new_folder_path, rel_path)
                                
                                # 确保目标目录存在
                                os.makedirs(os.path.dirname(new_file_path), exist_ok=True)
                                
                                # 移动文件
                                shutil.move(file_path, new_file_path)
                                moved_count += 1
                            except Exception as e:
                                logging.error(f"移动剩余文件失败: {file_path} -> {e}")
                        
                        if moved_count == len(remaining_files):
                            logging.info(f"成功移动所有剩余文件({moved_count}个)，尝试删除原文件夹")
                            try:
                                shutil.rmtree(old_folder_path)
                                logging.info(f"成功删除原文件夹: {old_folder_path}")
                            except Exception as e:
                                logging.error(f"删除原文件夹失败: {e}")
                        else:
                            logging.warning(f"只移动了部分剩余文件({moved_count}/{len(remaining_files)})，保留原文件夹")
            except Exception as e:
                logging.error(f"处理原文件夹失败: {e}")
            
            # 返回新的文件夹路径（规范化处理）
            return os.path.normpath(new_folder_path)
            
        except Exception as e:
            logging.error(f"迁移项目笔记失败: {e}")
            QMessageBox.warning(self, "迁移失败", f"项目笔记迁移失败：{str(e)}")
            return None
    

    
    def on_project_table_double_clicked(self, row, column):
        """处理项目表格双击事件，打开项目详情页"""
        # 调用已有的查看项目详情函数
        self.view_project_detail_by_row(row)
    
    def show_project_context_menu(self, position):
        """显示项目表格右键菜单"""
        # 获取点击的行
        item = self.project_table.itemAt(position)
        if item is None:
            return
        
        row = item.row()
        if row < 0:
            return
        
        # 获取项目信息
        name_item = self.project_table.item(row, 1)
        if not name_item:
            return
        
        project_name = name_item.text()
        # 移除置顶图标前缀（如果存在）
        if project_name.startswith("📌 "):
            project_name = project_name[2:]  # 移除"📌 "前缀
        # 移除最新项目标识前缀（如果存在）
        if project_name.startswith("🆕 "):
            project_name = project_name[2:]  # 移除"🆕 "前缀
        
        project = self.find_project_by_name(project_name)
        if not project:
            return
        
        # 创建右键菜单
        context_menu = QMenu(self)
        
        # 置顶/取消置顶项目
        is_pinned = project.get('pinned', False)
        if is_pinned:
            pin_action = context_menu.addAction("📌 取消置顶")
            pin_action.triggered.connect(lambda: self.toggle_project_pin(project_name, False))
        else:
            pin_action = context_menu.addAction("📌 置顶项目")
            pin_action.triggered.connect(lambda: self.toggle_project_pin(project_name, True))
        
        context_menu.addSeparator()
        
        # 查看项目详情
        detail_action = context_menu.addAction("📋 查看详情")
        detail_action.triggered.connect(lambda: self.view_project_detail_by_row(row))
        
        # 编辑项目
        edit_action = context_menu.addAction("✏️ 编辑项目")
        edit_action.triggered.connect(lambda: self.edit_project_by_row(row))
        
        # 添加资源
        add_resource_action = context_menu.addAction("➕ 添加资源")
        add_resource_action.triggered.connect(lambda: self.add_resource_to_project_by_row(row))
        
        context_menu.addSeparator()
        
        # 打开项目文件夹
        open_folder_action = context_menu.addAction("📁 打开项目文件夹")
        open_folder_action.triggered.connect(lambda: self.open_project_folder(project_name))
        
        context_menu.addSeparator()
        
        # 删除项目
        delete_action = context_menu.addAction("🗑️ 删除项目")
        delete_action.triggered.connect(lambda: self.delete_project_by_row(row))
        
        # 显示菜单
        context_menu.exec_(self.project_table.mapToGlobal(position))
    
    def toggle_project_pin(self, project_name, pin_status):
        """切换项目置顶状态"""
        try:
            # 验证输入参数
            if not project_name or not isinstance(project_name, str):
                QMessageBox.warning(self, "错误", "项目名称无效")
                return False
            
            if not isinstance(pin_status, bool):
                QMessageBox.warning(self, "错误", "置顶状态参数无效")
                return False
            
            # 查找项目
            project = self.find_project_by_name(project_name)
            if not project:
                QMessageBox.warning(self, "错误", f"未找到项目 '{project_name}'")
                return False
            
            # 更新置顶状态
            project['pinned'] = pin_status
            
            # 记录项目日志
            status_text = "置顶" if pin_status else "取消置顶"
            self.add_project_log(project_name, f"{status_text}项目", 
                               f"项目已{status_text}", 
                               "操作")
            
            # 更新修改时间
            self.update_project_modified_time(project_name, save_immediately=False)
            
            # 保存数据
            self.save_data()
            
            # 刷新项目列表
            self.refresh_project_list()
            
            # 显示成功消息
            status_text = "置顶" if pin_status else "取消置顶"
            self.status_bar.showMessage(f"📌 项目 '{project_name}' 已{status_text}")
            
            return True
            
        except Exception as e:
            error_msg = f"切换项目置顶状态时发生错误: {str(e)}"
            logging.error(error_msg)
            QMessageBox.critical(self, "错误", error_msg)
            return False
    
    def open_project_folder(self, project_name):
        """打开项目文件夹"""
        try:
            # 查找项目
            project = self.find_project_by_name(project_name)
            if not project:
                QMessageBox.warning(self, "错误", f"未找到项目 '{project_name}'")
                return
            
            # 获取项目文件夹路径
            folder_path = project.get('folder_path', '')
            if not folder_path:
                QMessageBox.warning(self, "错误", f"项目 '{project_name}' 没有设置文件夹路径")
                return
            
            # 检查文件夹是否存在
            if not os.path.exists(folder_path):
                QMessageBox.warning(self, "错误", f"项目文件夹不存在：{folder_path}")
                return
            
            # 根据操作系统打开文件夹
            import subprocess
            if sys.platform == 'win32':
                os.startfile(folder_path)
            elif sys.platform == 'darwin':  # macOS
                subprocess.run(['open', folder_path])
            else:  # Linux
                subprocess.run(['xdg-open', folder_path])
            
            # 记录项目日志
            self.add_project_log(project_name, "打开文件夹", 
                               f"打开项目文件夹: {folder_path}", 
                               "操作")
            
            # 显示成功消息
            self.status_bar.showMessage(f"📁 已打开项目 '{project_name}' 的文件夹")
            
        except Exception as e:
            error_msg = f"打开项目文件夹时发生错误: {str(e)}"
            logging.error(error_msg)
            QMessageBox.critical(self, "错误", error_msg)
    
    def edit_project_by_row(self, row):
        """根据行号编辑项目"""
        name_item = self.project_table.item(row, 1)
        if not name_item:
            return
        
        project_name = name_item.text()
        # 移除置顶图标前缀（如果存在）
        if project_name.startswith("📌 "):
            project_name = project_name[2:]  # 移除"📌 "前缀
        # 移除最新项目标识前缀（如果存在）
        if project_name.startswith("🆕 "):
            project_name = project_name[2:]  # 移除"🆕 "前缀
        
        # 查找项目数据
        project = None
        project_index = -1
        for i, p in enumerate(self.projects):
            if p['name'] == project_name:
                project = p
                project_index = i
                break
        
        if not project:
            QMessageBox.warning(self, "错误", "未找到项目数据！")
            return
        
        # 创建编辑对话框
        dialog = ProjectDialog(self, self.project_types, project)
        if dialog.exec_() == QDialog.Accepted:
            # 获取编辑后的数据
            updated_data = dialog.get_project_data()
            
            # 确保项目状态存在，默认为"未开始"
            if 'status' not in updated_data:
                updated_data['status'] = project.get('status', '未开始')
            
            # 检查项目名称是否发生变化，如果是则重命名文件夹
            old_name = project.get('name')
            new_name = updated_data.get('name')
            folder_renamed = False
            
            if old_name and new_name and old_name != new_name:
                # 如果项目有文件夹，尝试重命名
                if project.get('folder_path') and os.path.exists(project.get('folder_path')):
                    new_folder_path = self.rename_project_folder(project, old_name, new_name)
                    if new_folder_path:
                        updated_data['folder_path'] = new_folder_path
                        folder_renamed = True
                    else:
                        # 如果重命名失败，保持原有的文件夹路径
                        updated_data['folder_path'] = project.get('folder_path')
                        logging.warning(f"项目文件夹重命名失败，保持原路径: {project.get('folder_path')}")
                elif project.get('folder_path'):
                    # 如果项目有文件夹路径但文件夹不存在，保持原路径记录
                    updated_data['folder_path'] = project.get('folder_path')
                    logging.warning(f"项目文件夹不存在，保持原路径记录: {project.get('folder_path')}")
                
            # 处理文件夹创建逻辑（针对历史项目）
            folder_created = False
            if updated_data.get('create_folder', False) and not updated_data.get('folder_path'):
                # 创建项目文件夹
                folder_path = self.create_project_folder(updated_data['name'])
                if folder_path:
                    updated_data['folder_path'] = folder_path
                    folder_created = True
                    
                    # 如果项目有笔记数据，迁移到新文件夹
                    if project.get('notes'):
                        try:
                            self.migrate_project_notes(project, updated_data['name'], 
                                                     project.get('folder_path', ''), 
                                                     os.path.dirname(folder_path))
                        except Exception as e:
                            logging.error(f"迁移项目笔记失败: {e}")
            
            # 更新项目数据，保留重要字段
            # 保留原始的created_time、resources、id等重要字段
            updated_data['created_time'] = project.get('created_time')
            updated_data['resources'] = project.get('resources', [])
            updated_data['id'] = project.get('id')
            updated_data['modified_time'] = project.get('modified_time')
            
            self.projects[project_index] = updated_data
            
            # 记录项目日志
            if folder_renamed:
                self.add_project_log(updated_data['name'], "文件夹重命名", 
                                   f"项目文件夹从 '{old_name}' 重命名为 '{new_name}'", "系统")
            elif folder_created:
                self.add_project_log(updated_data['name'], "创建文件夹", 
                                   f"为项目创建文件夹: {updated_data['folder_path']}", "系统")
            
            self.add_project_log(updated_data['name'], "编辑项目", 
                               f"更新项目信息", "编辑")
            
            # 更新修改时间
            self.update_project_modified_time(updated_data['name'], save_immediately=False)
            
            # 保存数据
            self.save_data()
            
            # 刷新界面
            self.refresh_project_list()
            
            # 显示成功消息
            message = f"✅ 项目 '{updated_data['name']}' 已更新"
            if folder_renamed:
                message += "，文件夹已同步重命名"
            elif folder_created:
                message += "，已创建项目文件夹"
            
            self.status_bar.showMessage(message)
    
    def add_resource_to_project_by_row(self, row):
        """根据行号为项目添加资源"""
        name_item = self.project_table.item(row, 1)
        if not name_item:
            return
        
        project_name = name_item.text()
        # 移除置顶图标前缀（如果存在）
        if project_name.startswith("📌 "):
            project_name = project_name[2:]  # 移除"📌 "前缀
        
        # 直接调用添加资源对话框，不依赖表格选中状态
        dialog = AddResourceDialog(self, self.resource_categories, self.resource_types)
        if dialog.exec_() == QDialog.Accepted:
            resource_data = dialog.get_resource_data()
            
            project = self.find_project_by_name(project_name)
            if project:
                if 'resources' not in project:
                    project['resources'] = []
                
                # 检查是否存在重复资源
                resource_name = resource_data.get('name', '')
                resource_path = resource_data.get('path', '')
                
                # 检查重复（通过名称或路径）
                normalized_resource_path = os.path.normpath(resource_path) if resource_path else ''
                for existing_resource in project['resources']:
                    existing_path = os.path.normpath(existing_resource.get('path', ''))
                    if (existing_resource.get('name') == resource_name and resource_name) or \
                       (existing_path == normalized_resource_path and normalized_resource_path):
                        QMessageBox.warning(self, "重复资源", 
                                          f"资源 '{resource_name}' 已存在于项目中，无法重复添加。")
                        return
                
                # 添加资源
                project['resources'].append(resource_data)
                self.update_project_modified_time(project['name'], save_immediately=False)
                
                # 记录项目日志
                self.add_project_log(project['name'], "添加资源", 
                                    f"添加了资源：{resource_data['name']} ({resource_data.get('type', '未知类型')})", 
                                    "资源")
                
                self.save_data()
                self.refresh_project_list()  # 刷新项目列表以更新资源数量
                
                # 刷新项目详情页面（如果已打开）
                for dialog in self.findChildren(ProjectDetailDialog):
                    if dialog.project['name'] == project['name']:
                        dialog.load_resources()
                        dialog.update_tab_counts()  # 更新tab标题中的统计数
                        break
                
                self.status_bar.showMessage(f"✅ 资源 '{resource_data['name']}' 已添加")
    
    def delete_project_by_row(self, row):
        """根据行号删除项目"""
        name_item = self.project_table.item(row, 1)
        if not name_item:
            return
        
        project_name = name_item.text()
        # 移除置顶图标前缀（如果存在）
        if project_name.startswith("📌 "):
            project_name = project_name[2:]  # 移除"📌 "前缀
        # 移除最新项目标识前缀（如果存在）
        elif project_name.startswith("🆕 "):
            project_name = project_name[2:]  # 移除"🆕 "前缀
        
        # 找到项目数据
        project_to_delete = None
        project_index = -1
        for i, project in enumerate(self.projects):
            if project['name'] == project_name:
                project_to_delete = project
                project_index = i
                break
        
        if not project_to_delete:
            QMessageBox.warning(self, "错误", "未找到项目数据")
            return
        
        # 检查项目是否有关联的文件夹
        project_folder = project_to_delete.get('folder_path', '')
        if project_folder and os.path.exists(project_folder):
            # 创建自定义对话框询问是否删除文件夹
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("确认删除")
            msg_box.setText(f"确定要删除项目 '{project_name}' 吗？")
            msg_box.setInformativeText(f"项目文件夹路径：\n{project_folder}\n\n是否同时删除项目文件夹？")
            msg_box.setIcon(QMessageBox.Question)
            
            # 添加自定义按钮
            delete_with_folder_btn = msg_box.addButton("删除项目和文件夹", QMessageBox.YesRole)
            delete_only_project_btn = msg_box.addButton("仅删除项目数据", QMessageBox.NoRole)
            cancel_btn = msg_box.addButton("取消", QMessageBox.RejectRole)
            
            msg_box.setDefaultButton(delete_only_project_btn)
            msg_box.exec_()
            
            clicked_button = msg_box.clickedButton()
            
            if clicked_button == cancel_btn:
                return
            
            # 记录项目日志（在删除前记录）
            self.add_project_log(project_name, "删除项目", 
                               f"项目已被删除，包含 {len(project_to_delete.get('resources', []))} 个资源", 
                               "操作")
            
            # 删除项目数据
            del self.projects[project_index]
            
            # 如果用户选择同时删除项目文件夹
            if clicked_button == delete_with_folder_btn:
                try:
                    shutil.rmtree(project_folder)
                    self.status_bar.showMessage(f"🗑️ 项目 '{project_name}' 及其文件夹已删除")
                except Exception as e:
                    QMessageBox.warning(self, "警告", f"删除项目文件夹失败: {str(e)}")
                    self.status_bar.showMessage(f"🗑️ 项目 '{project_name}' 已删除，但文件夹删除失败")
            else:
                self.status_bar.showMessage(f"🗑️ 项目 '{project_name}' 已删除，文件夹保留")
        else:
            # 项目没有关联文件夹，直接确认删除
            reply = QMessageBox.question(self, "确认删除", 
                                      f"确定要删除项目 '{project_name}' 吗？\n此操作不可撤销。",
                                      QMessageBox.Yes | QMessageBox.No)
            
            if reply == QMessageBox.Yes:
                # 删除项目数据
                del self.projects[project_index]
                self.status_bar.showMessage(f"🗑️ 项目 '{project_name}' 已删除")
            else:
                return
        
        self.save_data(create_backup=True)  # 删除项目时创建备份
        self.refresh_project_list()
        # 清除选中的项目
        self.selected_project_name = None
        self.project_table.clearSelection()
    
    def refresh_resource_times(self):
        """刷新当前项目的资源文件时间信息"""
        current_row = self.project_table.currentRow()
        if current_row < 0:
            QMessageBox.information(self, "提示", "请先选择一个项目")
            return
        
        # 从项目名称列获取项目名称
        name_item = self.project_table.item(current_row, 1)
        if not name_item:
            QMessageBox.warning(self, "错误", "无法获取项目名称")
            return
            
        project_name = name_item.text()
        # 移除置顶图标前缀（如果存在）
        if project_name.startswith("📌 "):
            project_name = project_name[2:]  # 移除"📌 "前缀
        
        project = self.find_project_by_name(project_name)
        if project:
            # 重新显示项目详情以刷新时间信息
            self.status_bar.showMessage("🔄 资源时间信息已刷新")
        else:
            QMessageBox.warning(self, "错误", "未找到选中的项目")
    

    
    def add_resource_to_project(self):
        """添加资源到项目"""
        current_row = self.project_table.currentRow()
        if current_row < 0:
            QMessageBox.warning(self, "警告", "请先选择一个项目")
            return
        
        # 调用按行添加资源的方法
        self.add_resource_to_project_by_row(current_row)
    
    def check_resource_duplicate_and_get_id(self, project, resource_name, resource_path):
        """检查资源是否重复，如果存在则返回已有ID，否则返回新ID"""
        if 'resources' not in project:
            project['resources'] = []
        
        # 标准化路径用于比较
        normalized_resource_path = os.path.normpath(resource_path) if resource_path else ''
        
        # 检查是否存在重复资源
        for existing_resource in project['resources']:
            existing_path = os.path.normpath(existing_resource.get('path', ''))
            # 通过名称或路径检查重复
            if (existing_resource.get('name') == resource_name and resource_name) or \
               (existing_path == normalized_resource_path and normalized_resource_path):
                # 返回已存在的资源信息
                return {
                    'is_duplicate': True,
                    'existing_resource': existing_resource
                }
        

        return {
            'is_duplicate': False,
            'new_id': None,
            'existing_resource': None
        }
    
    def add_resource_to_project_by_id(self, project_id, resource_data):
        """根据项目ID添加资源到项目"""
        # 查找项目
        project = None
        for p in self.projects:
            if str(p.get('id', '')) == str(project_id):
                project = p
                break
        
        if not project:
            QMessageBox.warning(self, "错误", f"未找到ID为 {project_id} 的项目")
            return False
        
        # 使用统一的重复检查机制
        resource_name = resource_data.get('name', '')
        resource_path = resource_data.get('path', '')
        check_result = self.check_resource_duplicate_and_get_id(project, resource_name, resource_path)
        
        if check_result['is_duplicate']:
            QMessageBox.warning(self, "重复资源", 
                              f"资源 '{resource_name}' 已存在于项目 '{project['name']}' 中，无法重复添加。")
            return False
  
        
        # 添加资源
        project['resources'].append(resource_data)
        # 更新资源总数字段
        project['resource_count'] = len(project['resources'])
        self.update_project_modified_time(project['name'], save_immediately=False)
        self.save_data()
        self.refresh_project_list()  # 刷新项目列表以更新资源数量
        
        # 刷新项目详情页面（如果已打开）
        for dialog in self.findChildren(ProjectDetailDialog):
            if dialog.project['name'] == project['name']:
                dialog.load_resources()
                dialog.update_tab_counts()  # 更新tab标题中的统计数
                break
        
        self.status_bar.showMessage(f"✅ 资源 '{resource_data['name']}' 已添加到项目 '{project['name']}'")
        return True
    
    def add_resources_to_project_by_id(self, project_id, resources_data):
        """根据项目ID批量添加资源到项目"""
        # 查找项目
        project = None
        for p in self.projects:
            if str(p.get('id', '')) == str(project_id):
                project = p
                break
        
        if not project:
            QMessageBox.warning(self, "错误", f"未找到ID为 {project_id} 的项目")
            return False
        
        # 批量添加资源
        added_count = 0
        duplicate_count = 0
        
        for resource_data in resources_data:
            resource_name = resource_data.get('name', '')
            resource_path = resource_data.get('path', '')
            
            # 使用统一的重复检查机制
            check_result = self.check_resource_duplicate_and_get_id(project, resource_name, resource_path)
            
            if check_result['is_duplicate']:
                duplicate_count += 1
            else:
                project['resources'].append(resource_data)
                added_count += 1
        
        # 更新资源总数字段
        project['resource_count'] = len(project['resources'])
        self.update_project_modified_time(project['name'], save_immediately=False)
        self.save_data()
        
        # 显示批量添加结果
        message = f"✅ 成功添加 {added_count} 个资源到项目 '{project['name']}'"  
        if duplicate_count > 0:
            message += f"，跳过 {duplicate_count} 个重复资源"
        
        # 使用异步方式显示消息，避免阻塞UI
        QTimer.singleShot(0, lambda: self.status_bar.showMessage(message))
        
        # 延迟刷新项目列表，避免阻塞批量添加操作
        QTimer.singleShot(100, self.refresh_project_list)
        
        # 刷新项目详情页面（如果已打开）
        for dialog in self.findChildren(ProjectDetailDialog):
            if dialog.project['name'] == project['name']:
                dialog.load_resources()
                break
        
        return True
    
    def remove_resource_from_project(self):
        """从项目中移除资源"""
        if not hasattr(self, 'selected_project_name') or not self.selected_project_name:
            QMessageBox.warning(self, "警告", "请先选择一个项目")
            return
        
        project = self.find_project_by_name(self.selected_project_name)
        if not project or 'resources' not in project or not project['resources']:
            QMessageBox.warning(self, "警告", "当前项目没有资源")
            return
        
        # 显示资源选择对话框
        resource_names = [res['name'] for res in project['resources']]
        resource_name, ok = QInputDialog.getItem(self, "选择资源", "请选择要移除的资源:", resource_names, 0, False)
        if not ok:
            return
        
        reply = QMessageBox.question(self, "确认移除", 
                                   f"确定要移除资源 '{resource_name}' 吗？",
                                   QMessageBox.Yes | QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            current_row = self.project_table.currentRow()
            if current_row >= 0:
                # 从项目名称列获取项目名称
                name_item = self.project_table.item(current_row, 1)
                if name_item:
                    project_name = name_item.text()
                    # 移除置顶图标前缀（如果存在）
                    if project_name.startswith("📌 "):
                        project_name = project_name[2:]  # 移除"📌 "前缀
                    # 移除最新项目标识前缀（如果存在）
                    elif project_name.startswith("🆕 "):
                        project_name = project_name[2:]  # 移除"🆕 "前缀
                    
                    project = self.find_project_by_name(project_name)
                    if project and 'resources' in project:
                        # 找到并移除资源
                        removed_resource = None
                        for i, resource in enumerate(project['resources']):
                            if resource['name'] == resource_name:
                                removed_resource = resource
                                del project['resources'][i]
                                break
                        
                        # 更新资源总数字段
                        project['resource_count'] = len(project['resources'])
                        self.update_project_modified_time(project['name'], save_immediately=False)
                        
                        # 记录项目日志
                        if removed_resource:
                            self.add_project_log(project['name'], "移除资源", 
                                               f"移除了资源：{removed_resource['name']} ({removed_resource.get('type', '未知类型')})", 
                                               "资源")
                        
                        self.save_data(create_backup=True)  # 移除资源时创建备份
                        self.show_project_detail(project)
                        self.refresh_project_list()  # 刷新项目列表以更新资源数量
                        self.status_bar.showMessage(f"🗑️ 资源 '{resource_name}' 已移除")
    
    def open_resource(self, item, column):
        """打开资源"""
        resource_path = item.text(2)
        if os.path.exists(resource_path):
            try:
                if sys.platform.startswith('win'):
                    os.startfile(resource_path)
                elif sys.platform.startswith('darwin'):
                    subprocess.run(['open', resource_path])
                else:
                    subprocess.run(['xdg-open', resource_path])
                self.status_bar.showMessage(f"🚀 已打开: {resource_path}")
            except Exception as e:
                QMessageBox.warning(self, "错误", f"无法打开文件: {str(e)}")
        else:
            QMessageBox.warning(self, "错误", "文件不存在")
    
    def config_resource_types(self):
        """配置资源文件类型"""
        dialog = ResourceTypeConfigDialog(self, self.resource_types)
        if dialog.exec_() == QDialog.Accepted:
            self.resource_types = dialog.get_resource_types()
            self.save_config()
            self.refresh_type_combo()
            self.status_bar.showMessage("⚙️ 资源文件类型配置已更新")
    
    def refresh_type_combo(self):
        """刷新类型下拉框"""
        # 新UI中不再使用type_combo，改为刷新资源文件类型表格
        if hasattr(self, 'type_table'):
            self.refresh_resource_type_table()
        
        # 更新项目类型筛选下拉框
        if hasattr(self, 'type_filter_combo'):
            # 保存当前选中的项目类型
            current_type = self.type_filter_combo.currentText()
            
            # 暂时断开信号连接，避免触发 on_type_filter_changed
            try:
                self.type_filter_combo.currentIndexChanged.disconnect(self.on_type_filter_changed)
            except:
                pass
                
            # 清空并重新填充项目类型
            self.type_filter_combo.clear()
            self.type_filter_combo.addItem("全部类型")
            
            # 获取所有项目类型
            project_types = self.get_project_types()
            if project_types:
                self.type_filter_combo.addItems(project_types)
            
            # 恢复之前选中的项目类型
            index = self.type_filter_combo.findText(current_type)
            if index >= 0:
                self.type_filter_combo.setCurrentIndex(index)
            else:
                self.type_filter_combo.setCurrentIndex(0)  # 默认选择"全部类型"
            
            # 重新连接信号
            try:
                self.type_filter_combo.currentIndexChanged.connect(self.on_type_filter_changed)
            except:
                pass
    
    def on_type_selected(self, type_name):
        """类型选中事件"""
        if not type_name:
            self.type_resource_list.clear()
            return
            
        # 加载指定类型的资源
        self.load_type_resources(type_name)
    
    def load_type_resources(self, type_name, type_path=None):
        """加载指定类型的资源"""
        self.type_resource_list.clear()
        
        # 处理未归类资源的特殊情况
        if type_name == '未归类':
            self.load_uncategorized_resources()
            return
        
        # 遍历所有项目资源，找出指定类型的资源
        resource_count = 0
        for project in self.projects:
            for resource in project.get('resources', []):
                resource_path = resource.get('path', '')
                if not resource_path:
                    continue
                
                # 使用is_resource_of_type方法判断资源类型
                if self.is_resource_of_type(resource_path, type_name):
                    file_name = os.path.basename(resource_path)
                    item = QListWidgetItem(file_name)
                    item.setToolTip(resource_path)  # 设置完整路径为提示信息
                    self.type_resource_list.addItem(item)
                    resource_count += 1
        
        self.status_bar.showMessage(f"📁 已加载 {resource_count} 个 {type_name} 资源")
    
    def load_uncategorized_resources(self):
        """加载未归类的资源"""
        self.type_resource_list.clear()
        
        # 遍历所有项目资源，找出未归类的资源
        uncategorized_count = 0
        for project in self.projects:
            for resource in project.get('resources', []):
                resource_path = resource.get('path', '')
                if not resource_path:
                    continue
                
                # 使用is_resource_of_type方法判断是否为未归类资源
                if self.is_resource_of_type(resource_path, '未归类'):
                    file_name = os.path.basename(resource_path)
                    item = QListWidgetItem(file_name)
                    item.setToolTip(resource_path)  # 设置完整路径为提示信息
                    self.type_resource_list.addItem(item)
                    uncategorized_count += 1
        
        self.status_bar.showMessage(f"📁 已加载 {uncategorized_count} 个未归类资源")
    
    def open_type_resource(self, item):
        """打开类型资源"""
        # 从工具提示获取完整路径
        file_path = item.toolTip(0)
        
        if not file_path:
            QMessageBox.warning(self, "错误", "无法获取文件路径")
            return
        
        if os.path.exists(file_path):
            try:
                if sys.platform.startswith('win'):
                    os.startfile(file_path)
                elif sys.platform.startswith('darwin'):
                    subprocess.run(['open', file_path])
                else:
                    subprocess.run(['xdg-open', file_path])
                self.status_bar.showMessage(f"🚀 已打开: {file_path}")
            except Exception as e:
                QMessageBox.warning(self, "错误", f"无法打开文件: {str(e)}")
        else:
            QMessageBox.warning(self, "错误", "文件不存在")
    
    def batch_add_to_project(self):
        """批量添加到项目"""
        current_row = self.project_table.currentRow()
        if current_row < 0:
            QMessageBox.warning(self, "警告", "请先选择一个项目")
            return
        
        selected_items = self.type_resource_list.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "警告", "请先选择要添加的资源")
            return
        
        type_name = self.type_combo.currentText()
        type_path = self.resource_types[type_name]['path']
        
        # 从项目名称列获取项目名称
        name_item = self.project_table.item(current_row, 1)
        if not name_item:
            QMessageBox.warning(self, "错误", "无法获取项目名称")
            return
            
        project_name = name_item.text()
        project = self.find_project_by_name(project_name)
        
        if project:
            if 'resources' not in project:
                project['resources'] = []
            
            added_count = 0
            for item in selected_items:
                file_name = item.text()
                file_path = os.path.join(type_path, file_name)
                
                # 检查是否已存在
                exists = any(r['path'] == file_path for r in project['resources'])
                if not exists:
                    resource_data = {
                        'name': file_name,
                        'type': type_name,
                        'path': file_path,
                        'added_time': datetime.now().isoformat()
                    }
                    project['resources'].append(resource_data)
                    added_count += 1
            
            if added_count > 0:
                self.update_project_modified_time(project['name'])
                self.show_project_detail(project)
                self.status_bar.showMessage(f"✅ 已批量添加 {added_count} 个资源")
            else:
                self.status_bar.showMessage("ℹ️ 所选资源已存在于项目中")
    
    def on_type_filter_changed(self, index):
        """项目类型筛选变化时的处理"""
        self.filter_projects()
    
    def _populate_project_table(self, projects):
        """填充项目表格"""
        # 找出最新修改的项目（排除置顶项目）
        latest_project = None
        if projects:
            # 过滤掉置顶项目，只在非置顶项目中找最新的
            non_pinned_projects = [p for p in projects if not p.get('pinned', False)]
            if non_pinned_projects:
                def get_time_key(project):
                    """获取项目时间键值，确保返回可比较的值"""
                    modified_time = project.get('modified_time', project.get('created_time', ''))
                    if not modified_time:
                        return 0.0  # 默认值
                    
                    # 如果是字符串，尝试解析为datetime对象
                    if isinstance(modified_time, str):
                        try:
                            dt = datetime.fromisoformat(modified_time)
                            return dt.timestamp()
                        except:
                            return 0.0
                    
                    # 如果是数字，直接返回
                    try:
                        return float(modified_time)
                    except:
                        return 0.0
                
                latest_project = max(non_pinned_projects, key=get_time_key)
        
        for row, project in enumerate(projects):
            # 项目编号
            id_item = QTableWidgetItem(str(project.get('id', row + 1)))
            id_item.setTextAlignment(Qt.AlignCenter)
            self.project_table.setItem(row, 0, id_item)
            
            # 项目名称（如果是置顶项目，添加置顶图标；如果是最新项目，添加最新标识）
            project_name = project['name']
            is_latest = latest_project and project == latest_project
            
            if project.get('pinned', False):
                project_name = f"📌 {project_name}"
            elif is_latest:
                project_name = f"🆕 {project_name}"
                
            name_item = QTableWidgetItem(project_name)
            name_item.setTextAlignment(Qt.AlignCenter)
            
            # 为置顶项目设置特殊样式
            if project.get('pinned', False):
                name_item.setBackground(QColor('#fff3cd'))  # 浅黄色背景
                name_item.setForeground(QColor('#856404'))  # 深黄色文字
            # 为最新项目设置特殊样式
            elif is_latest:
                name_item.setBackground(QColor('#e8f5e9'))  # 浅绿色背景
                name_item.setForeground(QColor('#1b5e20'))  # 深绿色文字
                name_item.setToolTip('这是最近修改的项目')
                
            self.project_table.setItem(row, 1, name_item)
            
            # 项目类型
            project_type = project.get('type', '其他')
            type_item = QTableWidgetItem(project_type)
            type_item.setTextAlignment(Qt.AlignCenter)
            self.project_table.setItem(row, 2, type_item)
            
            # 项目状态
            project_status = project.get('status', '未开始')
            status_item = QTableWidgetItem(project_status)
            status_item.setTextAlignment(Qt.AlignCenter)
            
            # 根据状态设置不同的背景色
            if project_status == '已完成':
                status_item.setBackground(QColor('#e8f5e9'))  # 浅绿色
                status_item.setForeground(QColor('#2e7d32'))  # 深绿色文字
            elif project_status == '进行中':
                status_item.setBackground(QColor('#e3f2fd'))  # 浅蓝色
                status_item.setForeground(QColor('#1565c0'))  # 深蓝色文字
            elif project_status == '已暂停':
                status_item.setBackground(QColor('#fff8e1'))  # 浅黄色
                status_item.setForeground(QColor('#f57f17'))  # 橙色文字
            elif project_status == '已取消':
                status_item.setBackground(QColor('#ffebee'))  # 浅红色
                status_item.setForeground(QColor('#c62828'))  # 深红色文字
            else:  # 未开始
                status_item.setBackground(QColor('#f5f5f5'))  # 浅灰色
                status_item.setForeground(QColor('#616161'))  # 深灰色文字
                
            self.project_table.setItem(row, 3, status_item)
            
            # 资源文件数（优先从resource_count字段读取，如果没有则动态计算）
            resource_count = project.get('resource_count', len(project.get('resources', [])))
            count_item = QTableWidgetItem(str(resource_count))
            count_item.setTextAlignment(Qt.AlignCenter)
            self.project_table.setItem(row, 4, count_item)
            
            # 项目标签
            tags_str = ', '.join(project.get('tags', []))
            if not tags_str:
                tags_str = '无标签'
            tags_item = QTableWidgetItem(tags_str)
            self.project_table.setItem(row, 5, tags_item)
            
            # 创建时间
            created_time = project.get('created_time', '')
            if created_time:
                try:
                    dt = datetime.fromisoformat(created_time)
                    created_str = dt.strftime('%Y-%m-%d %H:%M')
                except:
                    created_str = '未知时间'
            else:
                created_str = '未知时间'

            created_item = QTableWidgetItem(created_str)
            created_item.setTextAlignment(Qt.AlignCenter)
            self.project_table.setItem(row, 6, created_item)
            
            # 最近修改时间
            modified_time = project.get('modified_time', created_time)
            if modified_time:
                try:
                    dt = datetime.fromisoformat(modified_time)
                    modified_str = dt.strftime('%Y-%m-%d %H:%M')
                except:
                    modified_str = '未知时间'
            else:
                modified_str = '未知时间'
            modified_item = QTableWidgetItem(modified_str)
            modified_item.setTextAlignment(Qt.AlignCenter)
            
            # 为最新项目的修改时间列添加特殊样式
            if is_latest:
                modified_item.setBackground(QColor('#e8f5e9'))  # 浅绿色背景
                modified_item.setForeground(QColor('#1b5e20'))  # 深绿色文字
                modified_item.setToolTip('最近修改的项目')
                
            self.project_table.setItem(row, 7, modified_item)
            
            # 创建操作按钮容器
            operation_widget = QWidget()
            operation_layout = QHBoxLayout(operation_widget)
            operation_layout.setContentsMargins(2, 2, 2, 2)
            operation_layout.setSpacing(8)
            
            # 添加资源按钮
            add_resource_btn = QPushButton("+ 资源")
            add_resource_btn.setStyleSheet(DesignSystem.table_action_button_style('default'))
            add_resource_btn.setToolTip("添加资源到项目")
            add_resource_btn.clicked.connect(lambda checked, r=row: self.add_resource_to_project_by_row(r))
            operation_layout.addWidget(add_resource_btn)
            
            # 编辑项目按钮
            edit_btn = QPushButton("编辑")
            edit_btn.setStyleSheet(DesignSystem.table_action_button_style('primary'))
            edit_btn.setToolTip("编辑项目")
            edit_btn.clicked.connect(lambda checked, r=row: self.edit_project_by_row(r))
            operation_layout.addWidget(edit_btn)
            
            # 删除按钮
            delete_btn = QPushButton("删除")
            delete_btn.setStyleSheet(DesignSystem.table_action_button_style('danger'))
            delete_btn.setToolTip("删除项目")
            delete_btn.clicked.connect(lambda checked, r=row: self.delete_project_by_row(r))
            operation_layout.addWidget(delete_btn)
            
            self.project_table.setCellWidget(row, 8, operation_widget)
    
    def filter_projects(self):
        """根据搜索文本、项目类型和状态筛选项目"""
        search_text = self.search_input.text().strip()
        selected_type = self.type_filter_combo.currentText()
        selected_status = self.status_filter_combo.currentText()
        
        # 如果没有筛选条件，显示所有项目
        if not search_text and selected_type == "全部类型" and selected_status == "全部状态":
            # 不要调用 refresh_project_list() 避免循环调用
            # 对项目进行排序：置顶项目在前
            sorted_projects = sorted(self.projects, key=lambda p: (
                not p.get('pinned', False),  # 置顶项目在前（False < True）
                p.get('created_time', '')  # 然后按创建时间排序
            ), reverse=False)
            
            # 更新空状态显示
            if len(sorted_projects) == 0:
                self.project_table.hide()
                self.project_empty_state.show()
            else:
                self.project_empty_state.hide()
                self.project_table.show()
                self.project_table.setRowCount(len(sorted_projects))
                self._populate_project_table(sorted_projects)
            return
        
        # 过滤项目表格
        filtered_projects = []
        for project in self.projects:
            # 检查项目类型筛选
            if selected_type != "全部类型" and project.get('type', '其他') != selected_type:
                continue
                
            # 检查项目状态筛选
            if selected_status != "全部状态" and project.get('status', '未开始') != selected_status:
                continue
                
            # 检查搜索文本
            if search_text and not (
                search_text.lower() in project['name'].lower() or 
                search_text.lower() in project.get('description', '').lower() or
                search_text.lower() in str(project.get('tags', '')).lower()
            ):
                continue
                
            filtered_projects.append(project)
        
        # 对筛选后的项目进行排序：置顶项目在前
        sorted_filtered_projects = sorted(filtered_projects, key=lambda p: (
            not p.get('pinned', False),  # 置顶项目在前（False < True）
            p.get('created_time', '')  # 然后按创建时间排序
        ), reverse=False)
        
        # 更新空状态显示
        if len(sorted_filtered_projects) == 0:
            self.project_table.hide()
            self.project_empty_state.show()
            # 更新空状态描述
            if search_text or selected_type != "全部类型" or selected_status != "全部状态":
                self.project_empty_state.set_content(
                    title="未找到匹配的项目",
                    description="没有找到符合筛选条件的项目，请尝试调整筛选条件"
                )
            else:
                self.project_empty_state.set_content(
                    title="暂无项目",
                    description="您还没有创建任何项目，点击下方按钮开始创建您的第一个项目"
                )
        else:
            self.project_empty_state.hide()
            self.project_table.show()
            # 更新项目表格显示过滤后的项目
            self.project_table.setRowCount(len(sorted_filtered_projects))
            self._populate_project_table(sorted_filtered_projects)
        
        # 搜索资源
        found_resources = []
        for project in self.projects:
            for resource in project.get('resources', []):
                if search_text and (search_text.lower() in resource['name'].lower() or
                                   search_text.lower() in resource['type'].lower()):
                    found_resources.append(f"{project['name']} - {resource['name']}")
        
        # 更新状态栏消息
        filter_conditions = []
        if selected_type != "全部类型":
            filter_conditions.append(f"类型: {selected_type}")
        if selected_status != "全部状态":
            filter_conditions.append(f"状态: {selected_status}")
        if search_text:
            filter_conditions.append(f"搜索: '{search_text}'")
        
        if filter_conditions:
            filter_msg = ", ".join(filter_conditions)
            if search_text:
                msg = f"🔍 {filter_msg} - 找到 {len(filtered_projects)} 个项目, {len(found_resources)} 个资源"
            else:
                msg = f"🔍 {filter_msg} - 找到 {len(filtered_projects)} 个项目"
        else:
            msg = f"共 {len(filtered_projects)} 个项目"
            
        self.status_bar.showMessage(msg)
    
    def on_search(self, text):
        """搜索功能"""
        self.filter_projects()
    
    def on_status_filter_changed(self, index):
        """状态筛选变化事件"""
        self.filter_projects()
    
    def on_type_filter_changed(self, index):
        """类型筛选变化事件"""
        self.filter_projects()
    
    def find_project_by_name(self, name):
        """根据名称查找项目"""
        for project in self.projects:
            if project['name'] == name:
                return project
        return None
        
    def get_project_types(self):
        """获取所有项目类型列表"""
        # 从所有项目中提取不重复的类型
        types = set()
        for project in self.projects:
            project_type = project.get('type', '其他')
            if project_type:
                types.add(project_type)
        return sorted(list(types))
    
    def remove_project_dialog(self, dialog):
        """从跟踪列表中移除项目详情对话框"""
        try:
            if dialog in self.open_project_dialogs:
                self.open_project_dialogs.remove(dialog)
        except Exception as e:
            print(f"移除项目对话框时出错：{str(e)}")
    
    def notify_project_dialogs_refresh(self):
        """通知所有打开的项目详情对话框刷新数据"""
        try:
            # 遍历所有打开的项目详情对话框
            for dialog in self.open_project_dialogs[:]:
                try:
                    # 检查对话框是否仍然有效
                    if hasattr(dialog, 'project') and dialog.project:
                        # 使用新的refresh_from_parent方法来刷新对话框
                        if hasattr(dialog, 'refresh_from_parent'):
                            dialog.refresh_from_parent()
                        else:
                            # 兼容旧版本，使用原有的刷新逻辑
                            project_name = dialog.project.get('name')
                            if project_name:
                                # 查找最新的项目数据
                                updated_project = None
                                for p in self.projects:
                                    if p['name'] == project_name:
                                        updated_project = p
                                        break
                                
                                # 如果找到了最新的项目数据，更新对话框
                                if updated_project:
                                    dialog.project = updated_project
                                    # 如果对话框有刷新方法，调用它
                                    if hasattr(dialog, 'load_resources'):
                                        dialog.load_resources()
                except Exception as e:
                    print(f"刷新项目对话框时出错：{str(e)}")
        except Exception as e:
            print(f"通知项目对话框刷新时出错：{str(e)}")
    
    def reload_data_and_refresh(self):
        """重新加载数据文件并刷新项目列表"""
        try:
            # 清空所有筛选和搜索条件，恢复到初始状态
            self.clear_all_filters_and_search()
            
            # 重新加载数据文件
            self.load_data()
            # 刷新项目列表显示
            self.refresh_project_list()
            
            # 通知所有打开的项目详情对话框刷新数据
            self.notify_project_dialogs_refresh()
            
            # 更新状态栏消息
            if hasattr(self, 'status_bar'):
                self.status_bar.showMessage("项目列表已刷新，筛选条件已重置", 2000)
        except Exception as e:
            QMessageBox.warning(self, "刷新失败", f"重新加载数据时出错：{str(e)}")
    
    def clear_all_filters_and_search(self):
        """清空所有筛选条件和搜索词，恢复到初始状态"""
        try:
            # 清空搜索框
            if hasattr(self, 'search_input'):
                # 暂时断开信号连接，避免触发搜索事件
                try:
                    self.search_input.textChanged.disconnect(self.on_search)
                except:
                    pass
                self.search_input.clear()
                # 重新连接信号
                try:
                    self.search_input.textChanged.connect(self.on_search)
                except:
                    pass
            
            # 重置项目类型筛选为"全部类型"
            if hasattr(self, 'type_filter_combo'):
                # 暂时断开信号连接，避免触发筛选事件
                try:
                    self.type_filter_combo.currentIndexChanged.disconnect(self.on_type_filter_changed)
                except:
                    pass
                index = self.type_filter_combo.findText("全部类型")
                if index >= 0:
                    self.type_filter_combo.setCurrentIndex(index)
                # 重新连接信号
                try:
                    self.type_filter_combo.currentIndexChanged.connect(self.on_type_filter_changed)
                except:
                    pass
            
            # 重置项目状态筛选为"全部状态"
            if hasattr(self, 'status_filter_combo'):
                # 暂时断开信号连接，避免触发筛选事件
                try:
                    self.status_filter_combo.currentIndexChanged.disconnect(self.on_status_filter_changed)
                except:
                    pass
                index = self.status_filter_combo.findText("全部状态")
                if index >= 0:
                    self.status_filter_combo.setCurrentIndex(index)
                # 重新连接信号
                try:
                    self.status_filter_combo.currentIndexChanged.connect(self.on_status_filter_changed)
                except:
                    pass
            
            # 清空笔记搜索框（如果存在）
            if hasattr(self, 'notes_search_input'):
                try:
                    self.notes_search_input.textChanged.disconnect(self.filter_notes)
                except:
                    pass
                self.notes_search_input.clear()
                try:
                    self.notes_search_input.textChanged.connect(self.filter_notes)
                except:
                    pass
            
            # 清空清单搜索框（如果存在）
            if hasattr(self, 'checklist_search_input'):
                try:
                    self.checklist_search_input.textChanged.disconnect(self.filter_checklist)
                except:
                    pass
                self.checklist_search_input.clear()
                try:
                    self.checklist_search_input.textChanged.connect(self.filter_checklist)
                except:
                    pass
                    
        except Exception as e:
            print(f"清空筛选条件时出错：{str(e)}")
    
    def refresh_project_list(self):
        """刷新项目表格"""
        # 保存当前的筛选条件
        current_type = self.type_filter_combo.currentText() if hasattr(self, 'type_filter_combo') else "全部类型"
        current_status = self.status_filter_combo.currentText() if hasattr(self, 'status_filter_combo') else "全部状态"
        current_search = self.search_input.text() if hasattr(self, 'search_input') else ""
        
        # 对项目进行排序：置顶项目在前，然后按创建时间倒序
        def get_sort_key(p):
            """获取排序键，确保类型一致"""
            pinned = not p.get('pinned', False)
            created_time = p.get('created_time', 0)
            # 统一转换为字符串进行比较，避免类型不一致
            if isinstance(created_time, (int, float)):
                return (pinned, str(created_time))
            return (pinned, str(created_time) if created_time else '0')
        
        sorted_projects = sorted(self.projects, key=get_sort_key, reverse=False)
        
        # 首先显示所有项目
        self.project_table.setRowCount(len(sorted_projects))
        self._populate_project_table(sorted_projects)
        
        # 如果有筛选条件，则暂时清除筛选条件，以便在 filter_projects 中重新应用
        if (current_type != "全部类型" or current_status != "全部状态" or current_search.strip()) and hasattr(self, 'filter_projects'):
            if hasattr(self, 'type_filter_combo'):
                index = self.type_filter_combo.findText("全部类型")
                if index >= 0:
                    self.type_filter_combo.setCurrentIndex(index)
            
            if hasattr(self, 'status_filter_combo'):
                index = self.status_filter_combo.findText("全部状态")
                if index >= 0:
                    self.status_filter_combo.setCurrentIndex(index)
            
            if hasattr(self, 'search_input') and current_search.strip():
                # 暂时断开信号连接，避免触发 on_search
                try:
                    self.search_input.textChanged.disconnect(self.on_search)
                except:
                    pass
                self.search_input.setText("")
                self.search_input.textChanged.connect(self.on_search)
        
        # 刷新类型下拉框
        self.refresh_type_combo()
        
        # 刷新资源类型表格
        self.refresh_resource_type_table()
        
        # 更新项目统计信息
        self.update_project_statistics()
        
        # 恢复筛选条件
        if (current_type != "全部类型" or current_status != "全部状态" or current_search.strip()) and hasattr(self, 'filter_projects'):
            # 恢复类型筛选
            if hasattr(self, 'type_filter_combo') and current_type != "全部类型":
                index = self.type_filter_combo.findText(current_type)
                if index >= 0:
                    # 暂时断开信号连接，避免触发 on_type_filter_changed
                    try:
                        self.type_filter_combo.currentIndexChanged.disconnect(self.on_type_filter_changed)
                    except:
                        pass
                    self.type_filter_combo.setCurrentIndex(index)
                    try:
                        self.type_filter_combo.currentIndexChanged.connect(self.on_type_filter_changed)
                    except:
                        pass
            
            # 恢复状态筛选
            if hasattr(self, 'status_filter_combo') and current_status != "全部状态":
                index = self.status_filter_combo.findText(current_status)
                if index >= 0:
                    # 暂时断开信号连接，避免触发 on_status_filter_changed
                    try:
                        self.status_filter_combo.currentIndexChanged.disconnect(self.on_status_filter_changed)
                    except:
                        pass
                    self.status_filter_combo.setCurrentIndex(index)
                    try:
                        self.status_filter_combo.currentIndexChanged.connect(self.on_status_filter_changed)
                    except:
                        pass
            
            # 恢复搜索文本
            if hasattr(self, 'search_input') and current_search.strip():
                # 暂时断开信号连接，避免触发 on_search
                try:
                    self.search_input.textChanged.disconnect(self.on_search)
                except:
                    pass
                self.search_input.setText(current_search)
                try:
                    self.search_input.textChanged.connect(self.on_search)
                except:
                    pass
            
            # 应用筛选
            self.filter_projects()
        
        # 动态调整列宽
        self.adjust_project_table_columns()
    
    def adjust_project_table_columns(self):
        """动态调整项目表格列宽
        
        根据表格可见区域宽度，按比例分配列宽：
        - 项目名称列：平均宽度的2倍
        - 操作列：平均宽度
        - 其他列：根据内容自动分配
        确保所有列都在可见范围内，不出现水平滚动条
        """
        if not hasattr(self, 'project_table'):
            return
        
        # 获取表格可见区域宽度
        table_width = self.project_table.viewport().width()
        
        # 获取列数
        column_count = self.project_table.columnCount()
        
        if column_count == 0:
            return
        
        # 定义各列的宽度比例
        # 列索引：0=项目编号, 1=项目名称, 2=项目类型, 3=状态, 4=资源文件数, 5=项目标签, 6=创建时间, 7=最近修改时间, 8=操作
        column_ratios = {
            0: 0.8,    # 项目编号：0.8倍
            1: 1.4,    # 项目名称：1.4倍（重要，较宽）
            2: 1.0,    # 项目类型：1.0倍
            3: 0.8,    # 状态：0.8倍
            4: 0.8,    # 资源文件数：0.8倍
            5: 1.0,    # 项目标签：1.0倍
            6: 1.0,    # 创建时间：1.0倍
            7: 1.0,    # 最近修改时间：1.0倍
            8: 1.3,    # 操作：1.3倍
        }
        
        # 计算比例总和
        total_ratio = sum(column_ratios.values())
        
        # 计算各列宽度，确保总宽度不超过可见区域
        header = self.project_table.horizontalHeader()
        for col in range(column_count):
            ratio = column_ratios.get(col, 1.0)
            # 使用比例占总和的比例来分配宽度
            width = int(table_width * (ratio / total_ratio))
            header.resizeSection(col, width)
    
    def refresh_resource_type_table(self):
        """刷新资源文件类型表格"""
        if not hasattr(self, 'type_table'):
            return
            
        # 初始化资源文件类型统计信息
        type_stats = {}
        
        # 初始化所有已配置的资源文件类型
        for type_name, type_info in self.resource_types.items():
            type_stats[type_name] = {
                'count': 0,
                'paths': set(),
                'latest_modified': None,
                'extensions': type_info['extensions']
            }
        
        # 添加未归类类型
        type_stats['未归类'] = {
            'count': 0,
            'paths': set(),
            'latest_modified': None,
            'extensions': []
        }
        
        # 遍历所有项目资源
        for project in self.projects:
            for resource in project.get('resources', []):
                resource_path = resource.get('path', '')
                if not resource_path or not os.path.exists(resource_path):
                    continue
                
                # 获取文件扩展名
                _, ext = os.path.splitext(resource_path)
                ext = ext.lower()
                
                # 根据扩展名确定资源文件类型
                resource_type = '未归类'
                for type_name, stats in type_stats.items():
                    if type_name != '未归类' and ext in stats['extensions']:
                        resource_type = type_name
                        break
                
                # 更新统计信息
                type_stats[resource_type]['count'] += 1
                type_stats[resource_type]['paths'].add(os.path.dirname(resource_path))
                
                # 获取文件修改时间
                try:
                    mtime = os.path.getmtime(resource_path)
                    if (type_stats[resource_type]['latest_modified'] is None or 
                        mtime > type_stats[resource_type]['latest_modified']):
                        type_stats[resource_type]['latest_modified'] = mtime
                except:
                    pass
        
        # 填充表格
        self.type_table.setRowCount(len(type_stats))
        
        for row, (type_name, stats) in enumerate(type_stats.items()):
            # 资源文件类型
            type_item = QTableWidgetItem(type_name)
            self.type_table.setItem(row, 0, type_item)
            
            # 文件数量
            count_item = QTableWidgetItem(str(stats['count']))
            count_item.setTextAlignment(Qt.AlignCenter)
            self.type_table.setItem(row, 1, count_item)
            
            # 资源扩展名
            if type_name == '未归类':
                ext_text = "其他扩展名"
            else:
                extensions = stats['extensions']
                ext_text = ", ".join(extensions) if extensions else "无扩展名"
            ext_item = QTableWidgetItem(ext_text)
            self.type_table.setItem(row, 2, ext_item)
            
            # 最近修改时间
            if stats['latest_modified']:
                try:
                    dt = datetime.fromtimestamp(stats['latest_modified'])
                    time_str = dt.strftime('%Y-%m-%d %H:%M')
                except:
                    time_str = '未知时间'
            else:
                time_str = '未知时间'
            time_item = QTableWidgetItem(time_str)
            time_item.setTextAlignment(Qt.AlignCenter)
            self.type_table.setItem(row, 3, time_item)
    
    def on_type_table_selected(self):
        """资源文件类型表格选择事件"""
        current_row = self.type_table.currentRow()
        if current_row >= 0:
            type_name = self.type_table.item(current_row, 0).text()
            self.selected_type_label.setText(type_name)
            
            # 处理未归类资源的特殊情况
            if type_name == '未归类':
                self.load_uncategorized_files()
            else:
                self.load_type_files(type_name)
        else:
            self.selected_type_label.setText("未选择类型")
            self.type_file_tree.clear()
    
    def load_type_files(self, type_name):
        """加载指定类型的文件列表"""
        if not hasattr(self, 'type_file_tree'):
            return
            
        self.type_file_tree.clear()
        
        # 获取该类型的所有资源
        resources_count = 0
        
        for project in self.projects:
            for resource in project.get('resources', []):
                # 根据扩展名确定资源文件类型
                resource_path = resource.get('path', '')
                if not resource_path:
                    continue
                    
                # 如果是指定类型的资源，或者根据扩展名匹配
                if self.is_resource_of_type(resource_path, type_name):
                    resources_count += 1
                    item = QTreeWidgetItem()
                    
                    # 文件名
                    file_name = os.path.basename(resource_path)
                    item.setText(0, file_name)
                    
                    # 大小
                    if os.path.exists(resource_path):
                        try:
                            size = os.path.getsize(resource_path)
                            if size < 1024:
                                size_str = f"{size} B"
                            elif size < 1024 * 1024:
                                size_str = f"{size/1024:.1f} KB"
                            else:
                                size_str = f"{size/(1024*1024):.1f} MB"
                        except:
                            size_str = "未知"
                    else:
                        size_str = "未知"
                    item.setText(1, size_str)
                    
                    # 所属项目
                    item.setText(2, project.get('name', ''))
                    
                    # 修改时间
                    if os.path.exists(resource_path):
                        try:
                            mtime = os.path.getmtime(resource_path)
                            dt = datetime.fromtimestamp(mtime)
                            time_str = dt.strftime('%Y-%m-%d %H:%M')
                        except:
                            time_str = "未知"
                    else:
                        time_str = "未知"
                    item.setText(3, time_str)
                    
                    # 设置完整路径为工具提示
                    item.setToolTip(0, resource_path)
                    
                    # 添加到树形控件
                    self.type_file_tree.addTopLevelItem(item)
        
        # 更新状态栏显示资源数量
        self.status_bar.showMessage(f"📁 已加载 {resources_count} 个 {type_name} 资源")
        
    def is_resource_of_type(self, resource_path, type_name):
        """判断资源是否属于指定类型"""
        # 处理未归类资源的特殊情况
        if type_name == '未归类':
            # 获取所有已配置资源文件类型的扩展名
            all_extensions = set()
            for type_info in self.resource_types.values():
                all_extensions.update(type_info['extensions'])
            
            # 获取文件扩展名
            _, ext = os.path.splitext(resource_path)
            ext = ext.lower()
            
            # 如果扩展名不在任何已配置的资源文件类型中，则为未归类
            return ext not in all_extensions
        
        # 处理普通资源文件类型
        elif type_name in self.resource_types:
            # 获取文件扩展名
            _, ext = os.path.splitext(resource_path)
            ext = ext.lower()
            
            # 检查扩展名是否在该类型的扩展名列表中
            return ext in self.resource_types[type_name]['extensions']
        
        return False
    
    def load_uncategorized_files(self):
        """加载未归类的文件列表"""
        # 直接使用is_resource_of_type方法判断资源文件类型
        self.load_type_files('未归类')
    
    def load_config(self):
        """加载配置"""
        try:
            if os.path.exists(self.config_path):
                with open(self.config_path, 'r', encoding='utf-8') as f:
                    config = json.load(f)
                    
                    # 检查是否为新格式配置文件
                    if 'appSpecific' in config:
                        # 新格式配置文件
                        app_config = config['appSpecific']
                        
                        # 加载项目类型（从"分类键-属性对象模式"中提取键名）
                        project_types_config = app_config.get('projectTypes', {})
                        if isinstance(project_types_config, dict):
                            # 新格式：提取启用的项目类型
                            self.project_types = [key for key, value in project_types_config.items() 
                                                 if isinstance(value, dict) and value.get('enabled', True)]
                        else:
                            # 兼容旧格式（数组）
                            self.project_types = project_types_config if isinstance(project_types_config, list) else self.project_types
                        
                        # 动态加载所有资源类型（直接从配置文件读取，无需硬编码映射）
                        if 'resourceTypes' in app_config:
                            self.resource_types.update(app_config['resourceTypes'])
                        
                        # 加载资源分类（从"分类键-属性对象模式"中提取键名）
                        resource_categories_config = app_config.get('resourceCategories', {})
                        if isinstance(resource_categories_config, dict):
                            # 新格式：提取启用的资源分类
                            self.resource_categories = [key for key, value in resource_categories_config.items() 
                                                       if isinstance(value, dict) and value.get('enabled', True)]
                        else:
                            # 兼容旧格式（数组）
                            self.resource_categories = resource_categories_config if isinstance(resource_categories_config, list) else self.resource_categories
                        
                        # 加载默认项目路径（从"分类键-属性对象模式"中提取值）
                        default_path_config = app_config.get('defaultProjectPath', {})
                        if isinstance(default_path_config, dict):
                            # 新格式：提取value属性
                            self.default_project_path = default_path_config.get('value', '')
                        else:
                            # 兼容旧格式（字符串）
                            self.default_project_path = default_path_config if isinstance(default_path_config, str) else ''
                        
                        # 加载自动扫描设置（从"分类键-属性对象模式"中提取值）
                        auto_scan_config = app_config.get('autoScanSettings', {})
                        if isinstance(auto_scan_config, dict):
                            # 加载自动扫描启用状态
                            enabled_config = auto_scan_config.get('enabled', {})
                            self.auto_scan_enabled = enabled_config.get('value', True) if isinstance(enabled_config, dict) else enabled_config
                            
                            # 加载扫描间隔
                            scan_interval_config = auto_scan_config.get('scanInterval', {})
                            self.auto_scan_interval = scan_interval_config.get('value', 30) if isinstance(scan_interval_config, dict) else scan_interval_config
                            
                            # 加载文件类型
                            file_types_config = auto_scan_config.get('fileTypes', {})
                            self.auto_scan_file_types = file_types_config.get('items', ['.pdf', '.docx', '.txt', '.md', '.jpg', '.png', '.mp4', '.mp3', '.ppt', '.pptx', '.xls', '.xlsx', '.bmp']) if isinstance(file_types_config, dict) else file_types_config
                            
                            # 加载排除文件夹
                            exclude_folders_config = auto_scan_config.get('excludeFolders', {})
                            self.auto_scan_exclude_folders = exclude_folders_config.get('items', ['.git', '__pycache__', 'node_modules', '.vscode']) if isinstance(exclude_folders_config, dict) else exclude_folders_config
                        else:
                            # 设置默认值（使用初始化时设置的默认值）
                            # 不再覆盖初始化时设置的self.auto_scan_enabled = False
                            self.auto_scan_interval = 30
                            self.auto_scan_file_types = ['.pdf', '.docx', '.txt', '.md', '.jpg', '.png', '.mp4', '.mp3', '.ppt', '.pptx', '.xls', '.xlsx', '.bmp']
                            self.auto_scan_exclude_folders = ['.git', '__pycache__', 'node_modules', '.vscode']
                        
                        # 更新配置文件的最后修改时间
                        if 'meta' in config:
                            config['meta']['lastModified'] = datetime.now().isoformat()
                            with open(self.config_path, 'w', encoding='utf-8') as f:
                                json.dump(config, f, ensure_ascii=False, indent=2)
                    else:
                        # 旧格式配置文件兼容性处理
                        self.resource_types.update(config.get('resource_types', {}))
                        self.project_types = config.get('project_types', self.project_types)
                        self.resource_categories = config.get('resource_categories', self.resource_categories)
                        self.default_project_path = config.get('default_project_path', '')
            else:
                # 如果配置文件不存在，设置默认值
                self.default_project_path = ''
        except Exception as e:
            logging.error(f"加载配置失败: {e}")
            self.default_project_path = ''
    
    def save_config(self):
        """保存配置"""
        try:
            current_time = datetime.now().isoformat()
            
            # 构建新格式的配置文件
            config = {
                "meta": {
                    "configIdentifier": "km-config-001",
                    "relatedTool": "com.iassistant.knowledge_manager",
                    "configVersion": "2.0.0",
                    "sourceFile": "knowledge_manager_tool.py",
                    "sourceCodePath": "d:/cursorcode/iassistant/code",
                    "name": "知识管理工具配置文件",
                    "description": "个人知识管理工具的配置文件，包含项目类型、资源类型、资源分类等配置信息",
                    "createdAt": "2024-01-01T00:00:00.000Z",
                    "lastModified": current_time
                },
                "system": {
                    "logLevel": "INFO",
                    "logPath": "/logs/knowledge_manager.log",
                    "maxLogFiles": 7,
                    "backupStrategy": {
                        "enabled": False,
                        "interval": "daily",
                        "retention": 30
                    }
                },
                "appSpecific": {
                    "projectTypes": {
                        project_type: {"enabled": True} for project_type in self.project_types
                    },
                    "resourceCategories": {
                        category: {"enabled": True} for category in self.resource_categories
                    },
                    "defaultProjectPath": {
                        "value": getattr(self, 'default_project_path', '')
                    },
                    "resourceTypes": self.resource_types,
                    "autoScanSettings": {
                        "enabled": {
                            "value": getattr(self, 'auto_scan_enabled', False)  # 默认为False
                        },
                        "scanInterval": {
                            "value": getattr(self, 'auto_scan_interval', 30)
                        },
                        "fileTypes": {
                            "items": getattr(self, 'auto_scan_file_types', ['.pdf', '.docx', '.txt', '.md', '.jpg', '.png', '.mp4', '.mp3', '.ppt', '.pptx', '.xls', '.xlsx', '.bmp'])
                        },
                        "excludeFolders": {
                            "items": getattr(self, 'auto_scan_exclude_folders', ['.git', '__pycache__', 'node_modules', '.vscode'])
                        }
                    }
                }
            }
            
            with open(self.config_path, 'w', encoding='utf-8') as f:
                json.dump(config, f, ensure_ascii=False, indent=2)
        except Exception as e:
            logging.error(f"保存配置失败: {e}")
    
    def load_data(self):
        """加载数据，增强鲁棒性处理"""
        # 初始化为空列表，确保数据结构正确
        self.projects = []
        
        try:
            if os.path.exists(self.data_path):
                # 尝试加载主数据文件
                with open(self.data_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    
                # 验证数据结构 - 支持新旧格式
                if isinstance(data, dict):
                    # 检查是否为新格式（包含meta、content等字段）
                    if 'content' in data and 'projects' in data['content']:
                        # 新格式
                        projects_data = data['content'].get('projects', [])
                        if isinstance(projects_data, list):
                            self.projects = projects_data
                            logging.info(f"成功加载 {len(self.projects)} 个项目（新格式）")
                        else:
                            logging.warning("新格式数据文件中的projects字段不是列表格式，使用空列表")
                            self.projects = []
                    elif 'projects' in data:
                        # 旧格式兼容
                        projects_data = data.get('projects', [])
                        if isinstance(projects_data, list):
                            self.projects = projects_data
                            logging.info(f"成功加载 {len(self.projects)} 个项目（旧格式）")
                        else:
                            logging.warning("旧格式数据文件中的projects字段不是列表格式，使用空列表")
                            self.projects = []
                    else:
                        logging.warning("数据文件格式不正确，缺少projects字段，使用空列表")
                        self.projects = []
                else:
                    logging.warning("数据文件格式不正确，不是有效的JSON对象，使用空列表")
                    self.projects = []
                    
                # 为没有resource_count字段的项目自动计算并添加该字段
                # 为没有folder_descriptions字段的项目添加该字段
                # 为没有project_logs字段的项目添加该字段
                for project in self.projects:
                    if 'resource_count' not in project:
                        project['resource_count'] = len(project.get('resources', []))
                    if 'folder_descriptions' not in project:
                        project['folder_descriptions'] = {}
                    if 'project_logs' not in project:
                        project['project_logs'] = []
                    
                # 为每个项目从markdown文件加载笔记和清单数据
                # 注意：此操作较耗时，延迟到UI显示后执行
                # self.load_projects_from_markdown()  # 移到延迟任务中
                
            else:
                # 数据文件不存在，尝试从备份恢复
                logging.warning(f"数据文件 {self.data_path} 不存在")
                if self.try_restore_from_backup():
                    logging.info("成功从备份文件恢复数据")
                    # 递归调用自己重新加载
                    self.load_data()
                    return
                else:
                    logging.info("没有可用的备份文件，创建新的空数据文件")
                    self.create_empty_data_file()
                    
        except json.JSONDecodeError as e:
            logging.error(f"JSON文件格式错误: {e}")
            # JSON格式错误，尝试从备份恢复
            if self.try_restore_from_backup():
                logging.info("JSON格式错误，已从备份恢复")
                self.load_data()
                return
            else:
                logging.error("无法从备份恢复，重置为空数据")
                self.projects = []
                self.create_empty_data_file()
                
        except FileNotFoundError as e:
            logging.error(f"文件未找到: {e}")
            self.projects = []
            self.create_empty_data_file()
            
        except PermissionError as e:
            logging.error(f"文件权限错误: {e}")
            self.projects = []
            
        except Exception as e:
            logging.error(f"加载数据时发生未知错误: {e}")
            self.projects = []
            # 尝试从备份恢复
            if self.try_restore_from_backup():
                logging.info("发生错误，已从备份恢复")
                self.load_data()
            else:
                self.create_empty_data_file()
    
    def try_restore_from_backup(self):
        """尝试从备份文件恢复数据"""
        try:
            # 查找最新的备份文件
            data_dir = os.path.dirname(os.path.abspath(self.data_path))
            backup_files = []
            
            for file in os.listdir(data_dir):
                if file.startswith('knowledge_manager_data_backup_') and file.endswith('.json'):
                    backup_path = os.path.join(data_dir, file)
                    if os.path.isfile(backup_path):
                        # 获取文件修改时间
                        mtime = os.path.getmtime(backup_path)
                        backup_files.append((mtime, backup_path))
            
            if not backup_files:
                return False
            
            # 按修改时间排序，获取最新的备份
            backup_files.sort(reverse=True)
            latest_backup = backup_files[0][1]
            
            # 验证备份文件是否有效
            with open(latest_backup, 'r', encoding='utf-8') as f:
                backup_data = json.load(f)
            
            # 检查是否为有效的数据格式（支持新旧格式）
            is_valid = False
            if isinstance(backup_data, dict):
                # 检查新格式
                if ('meta' in backup_data and 'content' in backup_data and 
                    'dataSchema' in backup_data and 'stats' in backup_data and
                    'projects' in backup_data.get('content', {})):
                    is_valid = True
                # 检查旧格式
                elif 'projects' in backup_data:
                    is_valid = True
            
            if is_valid:
                # 备份文件有效，复制到主数据文件
                import shutil
                shutil.copy2(latest_backup, self.data_path)
                logging.info(f"从备份文件 {latest_backup} 恢复数据")
                return True
            else:
                logging.warning(f"备份文件 {latest_backup} 格式不正确")
                return False
                
        except Exception as e:
            logging.error(f"从备份恢复数据失败: {e}")
            return False
    
    def create_empty_data_file(self):
        """创建空的数据文件"""
        try:
            current_time = datetime.now().isoformat()
            empty_data = {
                "meta": {
                    "dataIdentifier": "km-projects-001",
                    "relatedTool": "com.iassistant.knowledge_manager",
                    "sourceFile": "knowledge_manager_tool.py",
                    "sourceCodePath": "d:/cursorcode/iassistant/code",
                    "name": "知识管理项目数据",
                    "version": "2.0.0",
                    "createdAt": current_time,
                    "dataFilePath": self.data_path.replace('\\', '/'),
                    "lastModified": current_time,
                    "description": "存储知识管理工具的项目数据，包括项目信息、资源文件、笔记和清单等"
                },
                "dataSchema": {
                    "project": {
                        "fields": [
                            {"name": "id", "type": "integer", "required": True, "description": "项目唯一标识符"},
                            {"name": "name", "type": "string", "required": True, "description": "项目名称"},
                            {"name": "description", "type": "string", "required": False, "description": "项目描述"},
                            {"name": "type", "type": "string", "required": True, "description": "项目类型"},
                            {"name": "status", "type": "string", "required": True, "description": "项目状态"},
                            {"name": "tags", "type": "array", "required": False, "description": "项目标签列表"},
                            {"name": "create_folder", "type": "boolean", "required": True, "description": "是否创建项目文件夹"},
                            {"name": "folder_path", "type": "string", "required": False, "description": "项目文件夹路径"},
                            {"name": "created_time", "type": "string", "required": True, "description": "创建时间"},
                            {"name": "modified_time", "type": "string", "required": True, "description": "修改时间"},
                            {"name": "resources", "type": "array", "required": False, "description": "项目资源列表"},
                            {"name": "resource_count", "type": "integer", "required": False, "description": "资源数量"},
                            {"name": "last_modified", "type": "string", "required": False, "description": "最后修改时间"},
                            {"name": "folder_descriptions", "type": "object", "required": False, "description": "文件夹描述"},
                            {"name": "project_logs", "type": "array", "required": False, "description": "项目日志"}
                        ]
                    }
                },
                "content": {
                    "projects": []
                },
                "stats": {
                    "totalProjects": 0,
                    "totalResources": 0,
                    "lastAccessTime": current_time,
                    "dataVersion": "2.0.0"
                }
            }
            
            with open(self.data_path, 'w', encoding='utf-8') as f:
                json.dump(empty_data, f, ensure_ascii=False, indent=2)
            
            logging.info(f"创建空数据文件: {self.data_path}")
            
        except Exception as e:
            logging.error(f"创建空数据文件失败: {e}")
    
    def create_data_backup(self):
        """创建数据文件备份"""
        try:
            if not os.path.exists(self.data_path):
                return False
            
            # 生成备份文件名
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            backup_filename = f'knowledge_manager_data_backup_{timestamp}.json'
            backup_path = os.path.join(os.path.dirname(os.path.abspath(self.data_path)), backup_filename)
            
            # 复制文件（将保留上次创建时间）
            import shutil
            shutil.copy2(self.data_path, backup_path)
            
            logging.info(f"创建数据备份: {backup_path}")
            
            # 清理旧备份（保留最近10个）
            self.cleanup_old_backups()
            
            return True
            
        except Exception as e:
            logging.error(f"创建数据备份失败: {e}")
            return False
    
    def cleanup_old_backups(self, keep_count=1):
        """清理旧的备份文件，保留指定数量的最新备份"""
        try:
            data_dir = os.path.dirname(self.data_path)
            backup_files = []
            
            for file in os.listdir(data_dir):
                if file.startswith('knowledge_manager_data_backup_') and file.endswith('.json'):
                    backup_path = os.path.join(data_dir, file)
                    if os.path.isfile(backup_path):
                        mtime = os.path.getmtime(backup_path)
                        backup_files.append((mtime, backup_path))
            
            # 按修改时间排序
            backup_files.sort(reverse=True)
            
            # 删除超出保留数量的备份
            for _, backup_path in backup_files[keep_count:]:
                try:
                    os.remove(backup_path)
                    logging.info(f"删除旧备份: {backup_path}")
                except Exception as e:
                    logging.warning(f"删除备份文件失败: {e}")
                    
        except Exception as e:
            logging.error(f"清理备份文件失败: {e}")
    
    def manual_backup_data(self):
        """手动创建数据备份"""
        try:
            if not os.path.exists(self.data_path):
                QMessageBox.warning(self, "备份失败", "数据文件不存在，无法创建备份")
                return
            
            if self.create_data_backup():
                QMessageBox.information(self, "备份成功", "数据备份已创建成功")
            else:
                QMessageBox.warning(self, "备份失败", "创建数据备份时发生错误")
                
        except Exception as e:
            QMessageBox.critical(self, "备份失败", f"创建备份时发生错误：\n{str(e)}")
    
    def manual_restore_data(self):
        """手动从备份恢复数据"""
        try:
            # 查找可用的备份文件
            # 使用绝对路径避免路径拼接问题
            data_dir = os.path.dirname(os.path.abspath(self.data_path))
            backup_files = []
            
            print(f"Debug: data_dir = {data_dir}")
            for file in os.listdir(data_dir):
                if file.startswith('knowledge_manager_data_backup_') and file.endswith('.json'):
                    backup_path = os.path.join(data_dir, file)
                    print(f"Debug: backup_path = {backup_path}")
                    if os.path.isfile(backup_path):
                        mtime = os.path.getmtime(backup_path)
                        backup_files.append((mtime, backup_path, file))
                        print(f"Debug: added backup_files item: ({mtime}, {backup_path}, {file})")
            
            if not backup_files:
                QMessageBox.information(self, "恢复失败", "没有找到可用的备份文件")
                return
            
            # 按修改时间排序
            backup_files.sort(reverse=True)
            
            # 让用户选择要恢复的备份
            backup_names = []
            for mtime, path, filename in backup_files[:10]:  # 最多显示10个备份
                backup_time = datetime.fromtimestamp(mtime).strftime('%Y-%m-%d %H:%M:%S')
                backup_names.append(f"{backup_time} - {filename}")
            
            backup_name, ok = QInputDialog.getItem(
                self, "选择备份", "请选择要恢复的备份文件：", backup_names, 0, False
            )
            
            if not ok:
                return
            
            # 获取选中的备份文件路径
            selected_index = backup_names.index(backup_name)
            selected_backup = backup_files[selected_index][1]
            
            # 调试信息：打印路径
            print(f"Debug: selected_backup = {selected_backup}")
            print(f"Debug: os.path.exists(selected_backup) = {os.path.exists(selected_backup)}")
            
            # 确保路径正确
            if not os.path.exists(selected_backup):
                QMessageBox.warning(self, "恢复失败", f"备份文件不存在：\n{selected_backup}")
                return
            
            # 确认恢复操作
            reply = QMessageBox.question(
                self, "确认恢复", 
                f"确定要从以下备份恢复数据吗？\n\n{backup_name}\n\n注意：当前数据将被覆盖！",
                QMessageBox.Yes | QMessageBox.No
            )
            
            if reply != QMessageBox.Yes:
                return
            
            # 验证备份文件
            with open(selected_backup, 'r', encoding='utf-8') as f:
                backup_data = json.load(f)
            
            # 检查是否为有效的数据格式（支持新旧格式）
            is_valid = False
            if isinstance(backup_data, dict):
                # 检查新格式
                if ('meta' in backup_data and 'content' in backup_data and 
                    'dataSchema' in backup_data and 'stats' in backup_data and
                    'projects' in backup_data.get('content', {})):
                    is_valid = True
                # 检查旧格式
                elif 'projects' in backup_data:
                    is_valid = True
            
            if not is_valid:
                QMessageBox.warning(self, "恢复失败", "选择的备份文件格式不正确")
                return
            
            # 创建当前数据的备份
            if os.path.exists(self.data_path):
                self.create_data_backup()
            
            # 复制备份文件到主数据文件
            import shutil
            shutil.copy2(selected_backup, self.data_path)
            
            # 重新加载数据
            self.load_data()
            self.refresh_project_list()
            
            QMessageBox.information(self, "恢复成功", "数据已成功从备份恢复")
            
        except Exception as e:
            error_msg = str(e).replace('\\', '/')
            QMessageBox.critical(self, "恢复失败", f"从备份恢复数据时发生错误:\n{error_msg}")
    
    def startup_integrity_check(self):
        """启动时的数据完整性检查"""
        try:
            # 检查主数据文件
            if not os.path.exists(self.data_path):
                # 尝试从备份恢复
                data_dir = os.path.dirname(os.path.abspath(self.data_path))
                backup_files = []
                
                for file in os.listdir(data_dir):
                    if file.startswith('knowledge_manager_data_backup_') and file.endswith('.json'):
                        backup_path = os.path.join(data_dir, file)
                        if os.path.isfile(backup_path):
                            mtime = os.path.getmtime(backup_path)
                            backup_files.append((mtime, backup_path))
                
                if backup_files:
                    try:
                        # 按修改时间排序，获取最新的备份
                        backup_files.sort(reverse=True)
                        latest_backup = backup_files[0][1]
                        shutil.copy2(latest_backup, self.data_path)
                        print(f"已从备份恢复主数据文件: {os.path.basename(latest_backup)}")
                    except Exception as e:
                        print(f"从备份恢复失败: {str(e)}")
                        self.create_empty_data_file()
                else:
                    self.create_empty_data_file()
            else:
                # 验证主数据文件格式
                try:
                    with open(self.data_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                    
                    # 检查是否为有效的数据格式（支持新旧格式）
                    is_valid = False
                    if isinstance(data, dict):
                        # 检查新格式
                        if ('meta' in data and 'content' in data and 
                            'dataSchema' in data and 'stats' in data and
                            'projects' in data.get('content', {})):
                            is_valid = True
                        # 检查旧格式
                        elif 'projects' in data:
                            is_valid = True
                    
                    if not is_valid:
                        raise ValueError("数据格式不正确")
                        
                except (json.JSONDecodeError, ValueError) as e:
                    print(f"主数据文件格式错误: {str(e)}，尝试从备份恢复")
                    if not self.try_restore_from_backup():
                        self.create_empty_data_file()
            
            # 清理多余的备份文件，只保留一个最新的
            self.cleanup_old_backups(keep_count=1)
            
            # 检查并执行自动扫描资源功能
            self.check_and_auto_scan_resources()
            
        except Exception as e:
            print(f"启动完整性检查失败: {str(e)}")
    
    def check_and_auto_scan_resources(self):
        """检查并执行自动扫描资源功能"""
        try:
            # 检查是否启用了自动扫描功能
            if not self.auto_scan_enabled:
                return
                
            # 确保self.projects是最新的数据
            if not self.projects:
                self.load_data()
            
            # 检查每个项目的自动扫描设置
            auto_scan_count = 0
            new_resources_total = 0
            for project in self.projects:
                # 检查项目是否启用了自动扫描
                if project.get('auto_scan_resources', False):
                    folder_path = project.get('folder_path', '')
                    if folder_path and os.path.exists(folder_path):
                        # 执行扫描，检查是否有新资源添加
                        has_new_resources = self.scan_project_folder_for_auto_scan(project)
                        if has_new_resources:
                            auto_scan_count += 1
                            new_resources_total += 1
            
            if auto_scan_count > 0:
                print(f"已自动扫描 {auto_scan_count} 个项目的资源文件夹，共添加 {new_resources_total} 个新资源")
                # 刷新UI以显示最新的资源数量
                self.refresh_project_list()
                # 注意：save_data已在scan_project_folder_for_auto_scan中调用，这里不需要重复调用
                
        except Exception as e:
            print(f"自动扫描资源失败: {str(e)}")
    
    def scan_project_folder_for_auto_scan(self, project):
        """为指定项目扫描文件夹并添加新资源"""
        try:
            folder_path = project.get('folder_path', '')
            if not folder_path or not os.path.exists(folder_path):
                return False  # 返回False表示没有进行扫描
            
            # 获取项目现有资源
            existing_resources = project.get('resources', [])
            existing_paths = set()
            
            # 构建现有资源路径集合
            for resource in existing_resources:
                resource_path = resource.get('path', '')
                if resource_path:
                    existing_paths.add(os.path.normpath(resource_path))
            
            # 扫描文件夹中的文件
            new_resources_added = 0
            for root, dirs, files in os.walk(folder_path):
                # 跳过排除的文件夹
                dirs[:] = [d for d in dirs if d not in self.auto_scan_exclude_folders]
                
                for file in files:
                    # 跳过隐藏文件
                    if file.startswith('.'):
                        continue
                    
                    file_path = os.path.join(root, file)
                    normalized_path = os.path.normpath(file_path)
                    
                    # 检查是否已存在
                    if normalized_path in existing_paths:
                        continue
                    
                    # 获取文件类型
                    file_ext = os.path.splitext(file)[1].lower()
                    
                    # 检查文件类型是否在扫描范围内
                    if file_ext not in self.auto_scan_file_types:
                        continue
                    
                    file_type = self.get_file_type_by_extension(file_ext)
                    
                    if file_type:
                        # 创建新资源
                        new_resource = {
                            'name': file,
                            'path': file_path,
                            'type': file_type,
                            'category': '参考资料',  # 默认分类
                            'description': '',
                            'tags': [],
                            'added_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                            'last_modified': datetime.fromtimestamp(os.path.getmtime(file_path)).strftime('%Y-%m-%d %H:%M:%S'),
                            'size': self.format_file_size(os.path.getsize(file_path))
                        }
                        
                        # 添加到项目资源列表
                        existing_resources.append(new_resource)
                        new_resources_added += 1
                        existing_paths.add(normalized_path)
            
            # 更新项目资源列表
            project['resources'] = existing_resources
            
            # 更新资源计数
            project['resource_count'] = len(existing_resources)
            
            # 如果添加了新资源，记录日志
            if new_resources_added > 0:
                # 确保有项目日志列表
                if 'project_logs' not in project:
                    project['project_logs'] = []
                
                # 添加自动扫描日志
                log_entry = {
                    'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    'type': '系统',
                    'message': f'自动扫描完成，新增 {new_resources_added} 个资源文件'
                }
                project['project_logs'].append(log_entry)
                
                # 限制日志数量
                if len(project['project_logs']) > 100:
                    project['project_logs'] = project['project_logs'][-100:]
                
                # 立即保存数据，确保新资源被持久化
                self.save_data()
                return True  # 返回True表示有新资源添加
            
            return False  # 返回False表示没有新资源添加
        
        except Exception as e:
            print(f"扫描项目文件夹失败: {str(e)}")
            return False
    
    def get_file_type_by_extension(self, extension):
        """根据文件扩展名获取文件类型"""
        if not extension:
            return None
            
        # 检查各种资源类型
        for resource_type, config in self.resource_types.items():
            if extension in config.get('extensions', []):
                return resource_type
        
        # 未识别的文件类型
        return None
    
    def check_data_integrity(self):
        """检查数据完整性"""
        try:
            issues = []
            
            # 检查主数据文件
            if not os.path.exists(self.data_path):
                issues.append("❌ 主数据文件不存在")
            else:
                try:
                    with open(self.data_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                    
                    if not isinstance(data, dict):
                        issues.append("❌ 数据文件格式错误：不是有效的JSON对象")
                    else:
                        # 检查是否为新格式
                        if 'meta' in data and 'content' in data and 'dataSchema' in data and 'stats' in data:
                            # 新格式验证
                            if 'projects' not in data.get('content', {}):
                                issues.append("❌ 新格式数据文件缺少content.projects字段")
                            elif not isinstance(data['content']['projects'], list):
                                issues.append("❌ content.projects字段不是列表格式")
                            else:
                                projects_count = len(data['content']['projects'])
                                issues.append(f"✅ 主数据文件正常（新格式），包含 {projects_count} 个项目")
                                
                                # 检查项目数据完整性
                                for i, project in enumerate(data['content']['projects']):
                                    if not isinstance(project, dict):
                                        issues.append(f"❌ 项目 {i+1} 数据格式错误")
                                        continue
                                    
                                    required_fields = ['name', 'id']
                                    for field in required_fields:
                                        if field not in project:
                                            issues.append(f"❌ 项目 '{project.get('name', f'项目{i+1}')}' 缺少必需字段: {field}")
                                    
                                    # 检查项目文件夹
                                    folder_path = project.get('folder_path')
                                    if folder_path and not os.path.exists(folder_path):
                                        issues.append(f"⚠️ 项目 '{project.get('name')}' 的文件夹不存在: {folder_path}")
                        elif 'projects' in data:
                            # 旧格式兼容验证
                            if not isinstance(data['projects'], list):
                                issues.append("❌ projects字段不是列表格式")
                            else:
                                issues.append(f"✅ 主数据文件正常（旧格式），包含 {len(data['projects'])} 个项目")
                                
                                # 检查项目数据完整性
                                for i, project in enumerate(data['projects']):
                                    if not isinstance(project, dict):
                                        issues.append(f"❌ 项目 {i+1} 数据格式错误")
                                        continue
                                    
                                    required_fields = ['name', 'id']
                                    for field in required_fields:
                                        if field not in project:
                                            issues.append(f"❌ 项目 '{project.get('name', f'项目{i+1}')}' 缺少必需字段: {field}")
                                    
                                    # 检查项目文件夹
                                    folder_path = project.get('folder_path')
                                    if folder_path and not os.path.exists(folder_path):
                                        issues.append(f"⚠️ 项目 '{project.get('name')}' 的文件夹不存在: {folder_path}")
                        else:
                            issues.append("❌ 数据文件格式不正确，缺少必要字段")
                        
                except json.JSONDecodeError as e:
                    issues.append(f"❌ 数据文件JSON格式错误: {e}")
                except Exception as e:
                    issues.append(f"❌ 读取数据文件时发生错误: {e}")
            
            # 检查备份文件
            data_dir = os.path.dirname(os.path.abspath(self.data_path))
            backup_count = 0
            
            for file in os.listdir(data_dir):
                if file.startswith('knowledge_manager_data_backup_') and file.endswith('.json'):
                    backup_count += 1
            
            if backup_count == 0:
                issues.append("⚠️ 没有找到备份文件")
            else:
                issues.append(f"✅ 找到 {backup_count} 个备份文件")
            
            # 检查配置文件
            if not os.path.exists(self.config_path):
                issues.append("⚠️ 配置文件不存在")
            else:
                try:
                    with open(self.config_path, 'r', encoding='utf-8') as f:
                        json.load(f)
                    issues.append("✅ 配置文件正常")
                except:
                    issues.append("❌ 配置文件格式错误")
            
            # 显示检查结果
            result_text = "\n".join(issues)
            
            # 统计问题数量
            error_count = len([issue for issue in issues if issue.startswith("❌")])
            warning_count = len([issue for issue in issues if issue.startswith("⚠️")])
            
            if error_count == 0 and warning_count == 0:
                title = "数据完整性检查 - 全部正常"
                icon = QMessageBox.Information
            elif error_count == 0:
                title = f"数据完整性检查 - 发现 {warning_count} 个警告"
                icon = QMessageBox.Warning
            else:
                title = f"数据完整性检查 - 发现 {error_count} 个错误，{warning_count} 个警告"
                icon = QMessageBox.Critical
            
            msg = QMessageBox(icon, title, result_text)
            msg.setDetailedText("\n".join(issues))
            msg.exec_()
            
        except Exception as e:
            QMessageBox.critical(self, "检查失败", f"检查数据完整性时发生错误：\n{str(e)}")
    
    def load_projects_from_markdown(self):
        """为所有项目从markdown文件加载数据"""
        for project in self.projects:
            self.load_project_from_markdown(project)
    
    def load_project_from_markdown(self, project):
        """从markdown文件加载单个项目的数据"""
        try:
            folder_path = project.get('folder_path', '')
            if not folder_path or not os.path.exists(folder_path):
                # 如果没有文件夹路径或文件夹不存在，初始化空的数据结构
                project['notes_timeline'] = project.get('notes_timeline', [])
                project['checklist_items'] = project.get('checklist_items', [])
                return
            
            project_name = project['name']
            safe_name = "".join(c for c in project_name if c.isalnum() or c in (' ', '-', '_', '（', '）', '(', ')')).strip()
            if not safe_name:
                safe_name = "新项目"
            
            notes_file = os.path.join(folder_path, f"{safe_name}_笔记.md")
            
            if not os.path.exists(notes_file):
                # 如果markdown文件不存在，保持现有数据或初始化空的数据结构
                project['notes_timeline'] = project.get('notes_timeline', [])
                project['checklist_items'] = project.get('checklist_items', [])
                return
            
            # 读取markdown文件
            with open(notes_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 解析markdown内容
            notes_timeline, checklist_items = self.parse_markdown_content(content)
            
            # 更新项目数据（只有当markdown文件存在且有内容时才覆盖）
            if notes_timeline or checklist_items:
                project['notes_timeline'] = notes_timeline
                project['checklist_items'] = checklist_items
            else:
                # 保持现有数据
                project['notes_timeline'] = project.get('notes_timeline', [])
                project['checklist_items'] = project.get('checklist_items', [])
                
        except Exception as e:
            logging.error(f"从markdown文件加载项目数据失败: {e}")
            # 保持现有数据或初始化空的数据结构
            project['notes_timeline'] = project.get('notes_timeline', [])
            project['checklist_items'] = project.get('checklist_items', [])
    
    def parse_markdown_content(self, content):
        """解析markdown内容，提取笔记和清单"""
        notes_timeline = []
        checklist_items = []
        
        lines = content.split('\n')
        current_section = None
        current_note = None
        current_note_content = []
        
        for line in lines:
            line = line.strip()
            
            # 检测章节
            if line.startswith('## 项目清单'):
                current_section = 'checklist'
                continue
            elif line.startswith('## 笔记时间轴'):
                current_section = 'notes'
                continue
            elif line.startswith('## '):
                current_section = None
                continue
            
            # 解析清单项
            if current_section == 'checklist' and (line.startswith('- [x]') or line.startswith('- [ ]')):
                completed = line.startswith('- [x]')
                text_part = line[5:].strip()  # 移除 "- [x] " 或 "- [ ] "
                
                # 提取时间信息
                import re
                time_pattern = r'\(创建: ([^,)]+)(?:, 完成: ([^)]+))?\)'
                match = re.search(time_pattern, text_part)
                
                if match:
                    text = text_part[:match.start()].strip()
                    created_time = match.group(1)
                    completed_time = match.group(2) if completed else None
                    
                    checklist_item = {
                        'id': f"checklist_{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}",
                        'text': text,
                        'completed': completed,
                        'timestamp': self.parse_time_string(created_time),
                    }
                    
                    if completed_time:
                        checklist_item['completed_time'] = self.parse_time_string(completed_time)
                    
                    checklist_items.append(checklist_item)
            
            # 解析笔记
            elif current_section == 'notes':
                if line.startswith('### '):
                    # 保存上一个笔记
                    if current_note:
                        current_note['content'] = '\n'.join(current_note_content).strip()
                        notes_timeline.append(current_note)
                    
                    # 开始新笔记
                    title = line[4:].strip()  # 移除 "### "
                    current_note = {
                        'id': f"note_{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}",
                        'title': title,
                        'content': '',
                        'timestamp': datetime.now().isoformat()
                    }
                    current_note_content = []
                    
                elif line.startswith('**时间：**'):
                    if current_note:
                        time_str = line.replace('**时间：**', '').strip()
                        current_note['timestamp'] = self.parse_time_string(time_str)
                        
                elif line == '---':
                    # 笔记结束
                    if current_note:
                        current_note['content'] = '\n'.join(current_note_content).strip()
                        notes_timeline.append(current_note)
                        current_note = None
                        current_note_content = []
                        
                elif current_note and line and not line.startswith('**时间：**'):
                    current_note_content.append(line)
        
        # 保存最后一个笔记
        if current_note:
            current_note['content'] = '\n'.join(current_note_content).strip()
            notes_timeline.append(current_note)
        
        return notes_timeline, checklist_items
    
    def parse_time_string(self, time_str):
        """解析时间字符串为ISO格式"""
        try:
            # 尝试解析 YYYY-MM-DD HH:MM:SS 格式
            dt = datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')
            return dt.isoformat()
        except:
            try:
                # 尝试解析其他格式
                dt = datetime.fromisoformat(time_str)
                return dt.isoformat()
            except:
                # 如果都失败，返回当前时间
                return datetime.now().isoformat()
    
    def parse_project_logs_from_markdown(self, content):
        """从markdown内容中解析项目日志"""
        logs = []
        
        try:
            lines = content.split('\n')
            in_log_section = False
            
            for line in lines:
                line = line.strip()
                
                # 检测项目日志部分
                if line == '## 项目日志':
                    in_log_section = True
                    continue
                elif line.startswith('## ') and in_log_section:
                    # 遇到其他章节，结束日志解析
                    break
                
                # 解析日志条目
                if in_log_section and line.startswith('- **'):
                    # 格式: - **2024-01-01 12:00:00** [操作] 动作 - 详情
                    import re
                    pattern = r'^- \*\*([^*]+)\*\* \[([^\]]+)\] (.+?)(?:\s-\s(.+))?$'
                    match = re.match(pattern, line)
                    
                    if match:
                        timestamp_str = match.group(1)
                        log_type = match.group(2)
                        action = match.group(3)
                        details = match.group(4) if match.group(4) else ""
                        
                        log_entry = {
                            'id': f"log_{len(logs) + 1}",
                            'timestamp': self.parse_time_string(timestamp_str),
                            'type': log_type,
                            'action': action,
                            'details': details
                        }
                        
                        logs.append(log_entry)
        
        except Exception as e:
            print(f"解析项目日志失败: {e}")
        
        return logs
    
    def save_data(self, create_backup=False):
        """保存数据，增强鲁棒性处理
        
        Args:
            create_backup (bool): 是否在保存前创建备份，默认为False
        """
        try:
            # 根据参数决定是否创建备份
            if create_backup and os.path.exists(self.data_path):
                self.create_data_backup()
            
            # 创建项目数据的副本，排除笔记和清单数据
            projects_to_save = []
            for project in self.projects:
                if not isinstance(project, dict):
                    logging.warning(f"跳过无效的项目数据: {project}")
                    continue
                    
                project_copy = project.copy()
                # 移除笔记和清单数据，这些数据应该保存在markdown文件中
                # 保留项目日志，因为自动扫描功能会添加日志
                project_copy.pop('notes_timeline', None)
                project_copy.pop('checklist_items', None)
                # 添加资源总数字段
                project_copy['resource_count'] = len(project.get('resources', []))
                # 添加最后修改时间
                project_copy['last_modified'] = datetime.now().isoformat()
                # 确保保留folder_descriptions字段
                if 'folder_descriptions' not in project_copy:
                    project_copy['folder_descriptions'] = {}
                projects_to_save.append(project_copy)
            
            # 获取当前时间
            current_time = datetime.now().isoformat()
            
            # 构建符合新规范的数据结构
            data = {
                "meta": {
                    # 必填字段
                    "dataIdentifier": "km-projects-001",
                    "relatedTool": "com.iassistant.knowledge_manager",
                    "sourceFile": "knowledge_manager_tool.py",
                    "sourceCodePath": os.path.abspath(os.path.dirname(__file__)).replace('\\', '/'),
                    "name": "个人知识管理工具数据文件",
                    "version": self.TOOL_INFO['version'],
                    "createdAt": current_time,
                    
                    # 自动更新字段
                    "dataFilePath": os.path.abspath(self.data_path).replace('\\', '/'),
                    "lastModified": current_time,
                    
                    # 可选字段
                    "description": "存储个人知识管理工具的项目数据，包括项目信息、资源文件等"
                },
                
                "dataSchema": {
                    "project": {
                        "fields": [
                            {"name": "id", "type": "string", "required": True},
                            {"name": "name", "type": "string", "required": True},
                            {"name": "description", "type": "string", "required": False},
                            {"name": "type", "type": "string", "required": True},
                            {"name": "status", "type": "string", "required": True},
                            {"name": "tags", "type": "array", "required": False},
                            {"name": "create_folder", "type": "boolean", "required": True},
                            {"name": "folder_path", "type": "string", "required": False},
                            {"name": "created_time", "type": "string", "required": True},
                            {"name": "modified_time", "type": "string", "required": True},
                            {"name": "resources", "type": "array", "required": False},
                            {"name": "resource_count", "type": "number", "required": True},
                            {"name": "last_modified", "type": "string", "required": True},
                            {"name": "folder_descriptions", "type": "object", "required": False},
                            {"name": "project_logs", "type": "array", "required": False}
                        ]
                    }
                },
                
                "content": {
                    "projects": projects_to_save
                },
                
                "stats": {
                    "totalRecords": len(projects_to_save),
                    "lastAccessTime": current_time,
                    "totalProjects": len(projects_to_save),
                    "totalResources": sum(len(project.get('resources', [])) for project in projects_to_save)
                }
            }
            
            # 先写入临时文件，确保写入成功后再替换原文件
            temp_path = self.data_path + '.tmp'
            
            with open(temp_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            
            # 验证临时文件是否写入成功
            if os.path.exists(temp_path) and os.path.getsize(temp_path) > 0:
                # 验证JSON格式是否正确
                with open(temp_path, 'r', encoding='utf-8') as f:
                    json.load(f)  # 尝试解析JSON，如果格式错误会抛出异常
                
                # 替换原文件
                if os.path.exists(self.data_path):
                    os.replace(temp_path, self.data_path)
                else:
                    os.rename(temp_path, self.data_path)
                    
                # 如果创建了备份，清理旧备份，只保留一个最新的备份
                if create_backup:
                    self.cleanup_old_backups(keep_count=1)
                    
                logging.info(f"成功保存数据文件到 {self.data_path}（共 {len(projects_to_save)} 个项目）")
            else:
                raise Exception("临时文件写入失败或文件为空")
                
        except json.JSONEncodeError as e:
            logging.error(f"JSON编码错误: {e}")
            # 清理临时文件
            temp_path = self.data_path + '.tmp'
            if os.path.exists(temp_path):
                os.remove(temp_path)
                
        except PermissionError as e:
            logging.error(f"文件权限错误，无法保存数据: {e}")
            
        except OSError as e:
            logging.error(f"文件系统错误: {e}")
            
        except Exception as e:
            logging.error(f"保存数据时发生未知错误: {e}")
            # 清理临时文件
            temp_path = self.data_path + '.tmp'
            if os.path.exists(temp_path):
                try:
                    os.remove(temp_path)
                except:
                    pass
    
    def import_projects(self):
        """导入项目数据"""
        file_path, _ = QFileDialog.getOpenFileName(
            self, "导入项目数据", "", "JSON文件 (*.json);;所有文件 (*)"
        )
        
        if not file_path:
            return
            
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                imported_data = json.load(f)
                
            # 验证导入的数据格式
            if not isinstance(imported_data, dict):
                QMessageBox.warning(self, "导入失败", "导入的文件格式不正确，不是有效的JSON对象")
                return
            
            # 检查是否为新格式
            if 'meta' in imported_data and 'content' in imported_data and 'dataSchema' in imported_data and 'stats' in imported_data:
                # 新格式数据
                if 'projects' not in imported_data.get('content', {}):
                    QMessageBox.warning(self, "导入失败", "导入的文件格式不正确，缺少content.projects字段")
                    return
                imported_projects = imported_data['content'].get('projects', [])
            elif 'projects' in imported_data:
                # 旧格式数据
                imported_projects = imported_data.get('projects', [])
            else:
                QMessageBox.warning(self, "导入失败", "导入的文件格式不正确，缺少projects字段")
                return
            
            if not imported_projects:
                QMessageBox.information(self, "导入结果", "导入的文件中没有项目数据")
                return
                
            # 处理导入选项
            options = QMessageBox.question(
                self, 
                "导入选项", 
                f"发现{len(imported_projects)}个项目，请选择导入方式：\n\n点击'是'合并到现有项目\n点击'否'替换现有项目",
                QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel
            )
            
            if options == QMessageBox.Cancel:
                return
                
            if options == QMessageBox.Yes:  # 合并项目
                # 检查重复项目
                existing_names = {p['name'] for p in self.projects}
                new_projects = []
                duplicates = []
                
                for project in imported_projects:
                    if project['name'] in existing_names:
                        duplicates.append(project['name'])
                    else:
                        new_projects.append(project)
                        
                # 添加非重复项目
                if new_projects:
                    self.projects.extend(new_projects)
                    
                # 记录导入日志
                if new_projects:
                    for project in new_projects:
                        self.add_project_log(project['name'], "导入项目", 
                                           f"从文件 '{os.path.basename(file_path)}' 导入项目", 
                                           "操作")
                    
                # 显示结果
                if duplicates:
                    QMessageBox.information(
                        self, 
                        "导入结果", 
                        f"成功导入{len(new_projects)}个项目，{len(duplicates)}个重复项目被忽略"
                    )
                else:
                    QMessageBox.information(
                        self, 
                        "导入成功", 
                        f"成功导入{len(new_projects)}个项目"
                    )
            else:  # 替换项目
                # 记录替换操作日志
                for project in imported_projects:
                    self.add_project_log(project['name'], "导入项目（替换模式）", 
                                       f"从文件 '{os.path.basename(file_path)}' 导入项目（替换现有项目）", 
                                       "操作")
                    
                self.projects = imported_projects
                QMessageBox.information(
                    self, 
                    "导入成功", 
                    f"已替换为导入的{len(imported_projects)}个项目"
                )
                
            # 保存数据并刷新界面
            self.save_data()
            self.refresh_project_list()
            self.update_project_statistics()
            
        except Exception as e:
            QMessageBox.critical(self, "导入失败", f"导入项目时发生错误：\n{str(e)}")
    
    def export_projects(self):
        """导出项目数据"""
        if not self.projects:
            QMessageBox.warning(self, "导出失败", "当前没有项目数据可供导出")
            return
        
        # 生成默认文件名：当前日期+项目导出.json
        default_filename = f"{datetime.now().strftime('%Y%m%d')}项目导出.json"
        
        file_path, _ = QFileDialog.getSaveFileName(
            self, "导出项目数据", default_filename, "JSON文件 (*.json);;所有文件 (*)"
        )
        
        if not file_path:
            return
            
        # 如果没有.json后缀，添加后缀
        if not file_path.lower().endswith('.json'):
            file_path += '.json'
            
        try:
            # 准备导出数据（按新格式）
            current_time = datetime.now().isoformat()
            export_data = {
                "meta": {
                    "dataIdentifier": "km-export-001",
                    "relatedTool": "com.iassistant.knowledge_manager",
                    "sourceFile": "knowledge_manager_tool.py",
                    "sourceCodePath": "d:/cursorcode/iassistant/code",
                    "name": "知识管理项目导出数据",
                    "version": self.TOOL_INFO['version'],
                    "createdAt": current_time,
                    "dataFilePath": file_path.replace('\\', '/'),
                    "lastModified": current_time,
                    "description": "从知识管理工具导出的项目数据"
                },
                "dataSchema": {
                    "project": {
                        "fields": [
                            {"name": "id", "type": "integer", "required": True, "description": "项目唯一标识符"},
                            {"name": "name", "type": "string", "required": True, "description": "项目名称"},
                            {"name": "description", "type": "string", "required": False, "description": "项目描述"},
                            {"name": "type", "type": "string", "required": True, "description": "项目类型"},
                            {"name": "status", "type": "string", "required": True, "description": "项目状态"},
                            {"name": "tags", "type": "array", "required": False, "description": "项目标签列表"},
                            {"name": "create_folder", "type": "boolean", "required": True, "description": "是否创建项目文件夹"},
                            {"name": "folder_path", "type": "string", "required": False, "description": "项目文件夹路径"},
                            {"name": "created_time", "type": "string", "required": True, "description": "创建时间"},
                            {"name": "modified_time", "type": "string", "required": True, "description": "修改时间"},
                            {"name": "resources", "type": "array", "required": False, "description": "项目资源列表"}
                        ]
                    }
                },
                "content": {
                    "projects": self.projects
                },
                "stats": {
                    "totalProjects": len(self.projects),
                    "totalResources": sum(len(project.get('resources', [])) for project in self.projects),
                    "exportTime": current_time,
                    "dataVersion": "2.0.0"
                }
            }
            
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(export_data, f, ensure_ascii=False, indent=2)
                
            # 记录导出日志（为所有项目添加导出日志）
            for project in self.projects:
                self.add_project_log(project['name'], "导出项目", 
                                   f"项目已导出到文件 '{os.path.basename(file_path)}'", 
                                   "操作")
                
            QMessageBox.information(
                self, 
                "导出成功", 
                f"已成功导出{len(self.projects)}个项目到：\n{file_path}"
            )
            
        except Exception as e:
            QMessageBox.critical(self, "导出失败", f"导出项目时发生错误：\n{str(e)}")
    
    def update_project_statistics(self):
        """更新项目统计信息"""
        try:
            # 获取日期范围
            start_date = None
            end_date = None
            
            if hasattr(self, 'start_date_edit') and hasattr(self, 'end_date_edit'):
                # 获取日期值
                start_date_value = self.start_date_edit.date()
                end_date_value = self.end_date_edit.date()
                
                # 检查是否为默认日期（即"请选择"状态）
                # 在 QDateEdit 中，当日期等于最小日期时，会显示 specialValueText
                is_default_start = start_date_value == self.start_date_edit.minimumDate()
                is_default_end = end_date_value == self.end_date_edit.minimumDate()
                
                # 如果是默认日期，则不进行日期筛选
                if is_default_start and is_default_end:
                    # 设置为None，表示不进行日期筛选
                    start_date = None
                    end_date = None
                else:
                    # 否则使用选择的日期范围
                    start_date = start_date_value.toPyDate()
                    end_date = end_date_value.toPyDate()
            
            # 根据日期范围筛选项目
            filtered_projects = self.filter_projects_by_date_range(self.projects, start_date, end_date)
            
            # 计算总项目数
            total_projects = len(filtered_projects)
            
            # 计算总资源数
            total_resources = 0
            
            for project in filtered_projects:
                for resource in project.get('resources', []):
                    # 检查资源的创建时间是否在日期范围内
                    if self.is_resource_in_date_range(resource, start_date, end_date):
                        total_resources += 1
            
            # 安全更新统计标签（检查控件是否存在）
            if hasattr(self, 'project_count_label') and self.project_count_label:
                self.project_count_label.setText(str(total_projects))
            
            if hasattr(self, 'resource_count_label') and self.resource_count_label:
                self.resource_count_label.setText(str(total_resources))
                
        except Exception as e:
            # 记录错误但不中断程序
            print(f"[ERROR] 更新项目统计时出错: {e}")
            import traceback
            traceback.print_exc()
    

    
    def on_date_range_changed(self):
        """日期范围变更处理"""
        try:
            # 更新项目统计信息
            self.update_project_statistics()
            
            # 显示状态信息
            if hasattr(self, 'start_date_edit') and hasattr(self, 'end_date_edit'):
                # 检查是否为默认日期（即"请选择"状态）
                start_date_value = self.start_date_edit.date()
                end_date_value = self.end_date_edit.date()
                
                # 检查是否为默认日期（等于最小日期，显示为"请选择"）
                is_default_start = start_date_value == self.start_date_edit.minimumDate()
                is_default_end = end_date_value == self.end_date_edit.minimumDate()
                
                if is_default_start and is_default_end:
                    # 如果都是默认日期，显示为"全部范围"
                    if hasattr(self, 'status_bar') and self.status_bar:
                        self.status_bar.showMessage(f"📅 显示全部项目")
                else:
                    # 否则显示具体日期范围
                    start_date = start_date_value.toString('yyyy-MM-dd')
                    end_date = end_date_value.toString('yyyy-MM-dd')
                    if hasattr(self, 'status_bar') and self.status_bar:
                        self.status_bar.showMessage(f"📅 已更新统计范围: {start_date} 至 {end_date}")
        except Exception as e:
            print(f"[ERROR] 日期范围变更处理时出错: {e}")
            import traceback
            traceback.print_exc()
    
    def reset_date_range(self):
        """重置日期范围"""
        try:
            # 重置为默认状态（显示为"请选择"）
            if hasattr(self, 'start_date_edit') and self.start_date_edit:
                # 暂时断开信号连接，避免触发多次更新
                try:
                    self.start_date_edit.dateChanged.disconnect(self.on_date_range_changed)
                except:
                    pass
                    
                # 设置为最小日期，触发显示specialValueText
                min_date = QDate(2025, 1, 1)
                self.start_date_edit.setMinimumDate(min_date)
                self.start_date_edit.setDate(min_date)
                
                # 重新连接信号
                try:
                    self.start_date_edit.dateChanged.connect(self.on_date_range_changed)
                except:
                    pass
            
            if hasattr(self, 'end_date_edit') and self.end_date_edit:
                # 暂时断开信号连接，避免触发多次更新
                try:
                    self.end_date_edit.dateChanged.disconnect(self.on_date_range_changed)
                except:
                    pass
                    
                # 设置为最小日期，触发显示specialValueText
                end_min_date = QDate(2025, 1, 1)
                self.end_date_edit.setMinimumDate(end_min_date)
                # 设置最大日期为未来很远的日期，确保用户可以选择任意未来日期
                self.end_date_edit.setMaximumDate(QDate(2099, 12, 31))
                self.end_date_edit.setDate(end_min_date)
                
                # 重新连接信号
                try:
                    self.end_date_edit.dateChanged.connect(self.on_date_range_changed)
                except:
                    pass
            
            # 更新统计信息
            self.update_project_statistics()
            
            # 显示状态信息
            if hasattr(self, 'status_bar') and self.status_bar:
                self.status_bar.showMessage("📅 已重置日期范围为全部范围")
        except Exception as e:
            print(f"重置日期范围时出错: {e}")
            import traceback
            traceback.print_exc()
    
    def filter_projects_by_date_range(self, projects, start_date, end_date):
        """根据日期范围筛选项目"""
        if not start_date or not end_date:
            return projects
        
        # 检查是否为默认日期（即"请选择"状态）
        # 在 QDateEdit 中，当日期等于最小日期时，会显示 specialValueText
        # 这里我们需要检查传入的 datetime.date 对象是否对应于最小日期
        is_default_start = start_date == datetime(2025, 1, 1).date()
        is_default_end = end_date == datetime(2025, 1, 1).date()
        
        # 如果是默认日期范围，返回所有项目
        if is_default_start and is_default_end:
            return projects
        
        filtered_projects = []
        
        for project in projects:
            # 检查项目创建时间
            created_time = project.get('created_time', '')
            if created_time:
                try:
                    # 解析项目创建时间
                    project_date = datetime.strptime(created_time, '%Y-%m-%d %H:%M:%S').date()
                    
                    # 检查是否在日期范围内
                    if start_date <= project_date <= end_date:
                        filtered_projects.append(project)
                    else:
                        # 即使项目不在范围内，也检查是否有资源在范围内
                        has_resources_in_range = False
                        for resource in project.get('resources', []):
                            if self.is_resource_in_date_range(resource, start_date, end_date):
                                has_resources_in_range = True
                                break
                        
                        if has_resources_in_range:
                            filtered_projects.append(project)
                except:
                    # 如果解析失败，检查是否有资源在范围内
                    has_resources_in_range = False
                    for resource in project.get('resources', []):
                        if self.is_resource_in_date_range(resource, start_date, end_date):
                            has_resources_in_range = True
                            break
                    
                    if has_resources_in_range:
                        filtered_projects.append(project)
            else:
                # 如果没有创建时间，检查是否有资源在范围内
                has_resources_in_range = False
                for resource in project.get('resources', []):
                    if self.is_resource_in_date_range(resource, start_date, end_date):
                        has_resources_in_range = True
                        break
                
                if has_resources_in_range:
                    filtered_projects.append(project)
        
        return filtered_projects
    
    def is_resource_in_date_range(self, resource, start_date, end_date):
        """检查资源是否在日期范围内"""
        if not start_date or not end_date:
            return True
        
        # 检查资源添加时间
        added_time = resource.get('added_time', '')
        if added_time:
            try:
                resource_date = datetime.strptime(added_time, '%Y-%m-%d %H:%M:%S').date()
                return start_date <= resource_date <= end_date
            except:
                pass
        
        # 如果没有添加时间，检查文件修改时间
        resource_path = resource.get('path', '')
        if resource_path and os.path.exists(resource_path):
            try:
                mtime = os.path.getmtime(resource_path)
                file_date = datetime.fromtimestamp(mtime).date()
                return start_date <= file_date <= end_date
            except:
                pass
        
        # 默认返回True（包含在统计中）
        return True
    
    def create_project_folder(self, project_name, parent_path):
        """创建项目文件夹"""
        try:
            if not parent_path or not os.path.exists(parent_path):
                return False, ''
            
            # 清理项目名称，移除不合法的文件名字符
            safe_name = "".join(c for c in project_name if c.isalnum() or c in (' ', '-', '_', '（', '）', '(', ')')).strip()
            if not safe_name:
                safe_name = "新项目"
            
            # 创建项目文件夹路径
            project_folder_path = os.path.join(parent_path, safe_name)
            
            # 如果文件夹已存在，添加数字后缀
            counter = 1
            original_path = project_folder_path
            while os.path.exists(project_folder_path):
                project_folder_path = f"{original_path}_{counter}"
                counter += 1
            
            # 创建文件夹
            os.makedirs(project_folder_path, exist_ok=True)
            
            # 创建项目笔记文件
            try:
                notes_path = os.path.join(project_folder_path, f"{safe_name}_笔记.md")
                self.create_project_notes_file(project_name, notes_path)
            except:
                pass  # 忽略笔记文件创建失败
            
            # 规范化路径，统一使用系统默认的路径分隔符
            normalized_path = os.path.normpath(project_folder_path)
            return True, normalized_path
            
        except Exception as e:
            logging.error(f"创建项目文件夹失败: {e}")
            return False, ''
    
    def open_inspiration_pool(self):
        """打开灵感池工具"""
        try:
            # 导入灵感池工具类
            import importlib.util
            spec = importlib.util.spec_from_file_location("inspiration_pool_tool", os.path.join(os.path.dirname(__file__), "inspiration_pool_tool.py"))
            inspiration_pool_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(inspiration_pool_module)
            InspirationPoolTool = inspiration_pool_module.InspirationPoolTool
            
            # 创建灵感池工具实例
            inspiration_pool = InspirationPoolTool()
            inspiration_pool.show()
            
            # 显示状态消息
            self.status_bar.showMessage("灵感池工具已打开")
            
        except Exception as e:
            error_msg = f"打开灵感池工具失败: {str(e)}"
            logging.error(error_msg, exc_info=True)
            QMessageBox.critical(self, "错误", error_msg)

    def cleanup(self):
        """清理资源"""
        self.save_config()
        self.save_data(create_backup=False)  # 程序关闭时不创建备份
    
    def closeEvent(self, event):
        """窗口关闭事件"""
        self.cleanup()
        event.accept()
    
    def config_project_types(self):
        """配置项目类型"""
        dialog = ProjectTypeConfigDialog(self, self.project_types)
        if dialog.exec_() == QDialog.Accepted:
            self.project_types = dialog.get_project_types()
            self.save_config()
            QMessageBox.information(self, "成功", "项目类型配置已保存！")
    
    def config_default_project_path(self):
        """配置默认项目路径"""
        dialog = DefaultProjectPathDialog(self, self.default_project_path)
        if dialog.exec_() == QDialog.Accepted:
            self.default_project_path = dialog.get_path()
            self.save_config()
            QMessageBox.information(self, "成功", "默认项目路径已保存！")
    
    def open_config_folder(self):
        """打开配置文件夹"""
        config_folder = os.path.dirname(self.config_path)
        if not os.path.exists(config_folder):
            QMessageBox.warning(self, "警告", "配置文件夹不存在！")
            return
            
        try:
            if sys.platform.startswith('win'):
                os.startfile(config_folder)
            elif sys.platform.startswith('darwin'):  # macOS
                subprocess.run(['open', config_folder])
            else:  # Linux
                subprocess.run(['xdg-open', config_folder])
            self.status_bar.showMessage(f"📂 已打开配置文件夹: {config_folder}")
        except Exception as e:
            QMessageBox.warning(self, "打开失败", f"无法打开配置文件夹:\n{str(e)}")
    
    def open_data_folder(self):
        """打开数据文件夹"""
        data_folder = os.path.dirname(os.path.abspath(self.data_path))
        if not os.path.exists(data_folder):
            QMessageBox.warning(self, "警告", "数据文件夹不存在！")
            return
            
        try:
            if sys.platform.startswith('win'):
                os.startfile(data_folder)
            elif sys.platform.startswith('darwin'):  # macOS
                subprocess.run(['open', data_folder])
            else:  # Linux
                subprocess.run(['xdg-open', data_folder])
            self.status_bar.showMessage(f"📂 已打开数据文件夹: {data_folder}")
        except Exception as e:
            QMessageBox.warning(self, "打开失败", f"无法打开数据文件夹:\n{str(e)}")
    
    def show_resource_inventory(self):
        """显示资源清单页面"""
        dialog = ResourceInventoryDialog(self)
        dialog.exec_()
    



class ProjectDialog(QDialog):
    """新建/编辑项目对话框"""
    
    def __init__(self, parent=None, project_types=None, edit_project=None):
        super().__init__(parent)
        self.project_types = project_types or []
        self.edit_project = edit_project
        self.is_edit_mode = edit_project is not None
        self.project_status = ["未开始", "进行中", "已完成", "已暂停", "已取消"]
        self.init_ui()
    
    def init_ui(self):
        """初始化UI"""
        self.setWindowTitle("新建项目")
        width, height = get_optimal_dialog_size(580, 850)
        self.setFixedSize(width, height)
        center_window(self)
        
        # 设置对话框样式
        c = DesignSystem.COLORS
        self.setStyleSheet(f"""
            QDialog {{
                background-color: {c['background']};
            }}
        """)
        
        main_layout = QVBoxLayout(self)
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(0, 0, 0, 0)
        
        # 创建内容区域
        content_widget = QFrame()
        c = DesignSystem.COLORS
        content_widget.setStyleSheet(f"""
            QFrame {{
                background-color: {c['surface']};
                border-radius: {DesignSystem.RADIUS['lg']}px;
                margin: 20px;
            }}
        """)
        
        content_layout = QVBoxLayout(content_widget)
        content_layout.setSpacing(20)
        content_layout.setContentsMargins(28, 28, 28, 28)
        
        # 标题区域
        header_layout = QVBoxLayout()
        header_layout.setSpacing(8)
        
        title_text = "✨ 编辑项目" if self.is_edit_mode else "✨ 新建项目"
        title_label = QLabel(title_text)
        c = DesignSystem.COLORS
        title_label.setStyleSheet(f"""
            QLabel {{
                font-size: 24px;
                font-weight: bold;
                color: {c['text_primary']};
                margin: 0;
            }}
        """)
        header_layout.addWidget(title_label)
        
        subtitle_text = "修改项目信息" if self.is_edit_mode else "创建一个新的知识管理项目"
        subtitle_label = QLabel(subtitle_text)
        c = DesignSystem.COLORS
        subtitle_label.setStyleSheet(f"""
            QLabel {{
                font-size: 14px;
                color: {c['text_secondary']};
                margin: 0;
            }}
        """)
        header_layout.addWidget(subtitle_label)
        
        content_layout.addLayout(header_layout)
        
        # 表单区域
        form_layout = QVBoxLayout()
        form_layout.setSpacing(20)  # 增加表单项之间的间距
        form_layout.setContentsMargins(0, 0, 0, 0)  # 确保没有额外的边距
        
        # 项目名称
        name_group = self.create_form_group(
            "项目名称", 
            "请输入项目名称", 
            is_required=True
        )
        self.name_edit = name_group['input']
        form_layout.addLayout(name_group['layout'])
        
        # 项目类型和状态并排
        type_status_layout = QHBoxLayout()
        type_status_layout.setSpacing(16)
        
        # 项目类型
        type_group = self.create_combo_group(
            "项目类型", 
            self.project_types
        )
        self.type_combo = type_group['combo']
        type_status_layout.addLayout(type_group['layout'])
        
        # 项目状态
        status_group = self.create_combo_group(
            "项目状态", 
            self.project_status
        )
        self.status_combo = status_group['combo']
        type_status_layout.addLayout(status_group['layout'])
        
        form_layout.addLayout(type_status_layout)
        
        # 项目标签
        tags_group = self.create_form_group(
            "项目标签", 
            "#标签1, #标签2"
        )
        self.tags_edit = tags_group['input']
        form_layout.addLayout(tags_group['layout'])
        
        # 项目描述（大文本框）
        desc_group = self.create_large_text_area_group(
            "项目描述", 
            "请输入项目描述（可选）"
        )
        self.desc_edit = desc_group['textarea']
        form_layout.addLayout(desc_group['layout'])
        
        # 文件夹创建选项
        folder_group = self.create_folder_creation_group()
        form_layout.addLayout(folder_group['layout'])
        self.create_folder_checkbox = folder_group['checkbox']
        self.folder_path_edit = folder_group['path_edit']
        self.browse_btn = folder_group['browse_btn']
        
        content_layout.addLayout(form_layout)
        
        # 底部按钮区域
        content_layout.addSpacing(30)
        button_layout = QHBoxLayout()
        button_layout.setSpacing(12)
        button_layout.setContentsMargins(0, 0, 0, 0)  # 确保没有额外的边距
        button_layout.addStretch(1)
        
        self.cancel_btn = QPushButton("取消")
        self.cancel_btn.clicked.connect(self.reject)
        c = DesignSystem.COLORS
        self.cancel_btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {c['surface_pressed']};
                color: {c['text_secondary']};
                border: 1px solid {c['border']};
                border-radius: {DesignSystem.RADIUS['md']}px;
                padding: 8px 16px;
                font-size: 13px;
                font-weight: 500;
                min-width: 80px;
                min-height: 32px;
            }}
            QPushButton:hover {{
                background-color: {c['surface_hover']};
                border-color: {c['border_hover']};
            }}
            QPushButton:pressed {{
                background-color: {c['surface_pressed']};
            }}
        """)
        button_layout.addWidget(self.cancel_btn)
        
        button_text = "保存修改" if self.is_edit_mode else "创建项目"
        self.ok_btn = QPushButton(button_text)
        self.ok_btn.clicked.connect(self.accept_project)
        c = DesignSystem.COLORS
        self.ok_btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {c['success']};
                color: white;
                border: none;
                border-radius: {DesignSystem.RADIUS['md']}px;
                padding: 8px 16px;
                font-size: 13px;
                font-weight: bold;
                min-width: 90px;
                min-height: 32px;
            }}
            QPushButton:hover {{
                background-color: {c['success_hover']};
            }}
            QPushButton:pressed {{
                background-color: {c['success_pressed']};
            }}
        """)
        button_layout.addWidget(self.ok_btn)
        
        content_layout.addLayout(button_layout)
        content_layout.addSpacing(10)  # 在底部添加一些空间
        main_layout.addWidget(content_widget)
        
        # 如果是编辑模式，预填充数据
        if self.is_edit_mode and self.edit_project:
            self.populate_edit_data()
    
    def create_form_group(self, label_text, placeholder, is_required=False):
        """创建表单组"""
        layout = QVBoxLayout()
        layout.setSpacing(8)
        
        # 标签
        label = QLabel(label_text + (" *" if is_required else ""))
        c = DesignSystem.COLORS
        label.setStyleSheet(f"""
            QLabel {{
                font-size: {DesignSystem.FONT_SIZES['lg']}px;
                font-weight: 600;
                color: {c['text_primary']};
                margin: 0;
            }}
        """)
        layout.addWidget(label)
        
        # 输入框
        input_edit = QLineEdit()
        input_edit.setPlaceholderText(placeholder)
        c = DesignSystem.COLORS
        input_edit.setStyleSheet(f"""
            QLineEdit {{
                border: 2px solid {c['border']};
                border-radius: {DesignSystem.RADIUS['md']}px;
                padding: 14px 16px;
                font-size: {DesignSystem.FONT_SIZES['lg']}px;
                background-color: {c['surface_hover']};
                min-height: 20px;
            }}
            QLineEdit:focus {{
                border-color: {c['success']};
                background-color: {c['surface']};
            }}
            QLineEdit:hover {{
                border-color: {c['border_hover']};
                background-color: {c['surface']};
            }}
        """)
        layout.addWidget(input_edit)
        
        return {'layout': layout, 'input': input_edit}
    
    def create_combo_group(self, label_text, items):
        """创建下拉框组"""
        layout = QVBoxLayout()
        layout.setSpacing(8)
        
        # 标签
        label = QLabel(label_text)
        c = DesignSystem.COLORS
        label.setStyleSheet(f"""
            QLabel {{
                font-size: {DesignSystem.FONT_SIZES['lg']}px;
                font-weight: 600;
                color: {c['text_primary']};
                margin: 0;
            }}
        """)
        layout.addWidget(label)
        
        # 下拉框
        combo = QComboBox()
        combo.addItems(items)
        c = DesignSystem.COLORS
        combo.setStyleSheet(f"""
            QComboBox {{
                border: 2px solid {c['border']};
                border-radius: {DesignSystem.RADIUS['md']}px;
                padding: 8px 16px;
                font-size: {DesignSystem.FONT_SIZES['lg']}px;
                background-color: {c['surface_hover']};
                min-height: 20px;
            }}
            QComboBox:focus {{
                border-color: {c['success']};
                background-color: {c['surface']};
            }}
            QComboBox:hover {{
                border-color: {c['border_hover']};
                background-color: {c['surface']};
            }}
            QComboBox::drop-down {{
                border: none;
                width: 30px;
            }}
            QComboBox::down-arrow {{
                image: none;
                border-left: 6px solid transparent;
                border-right: 6px solid transparent;
                border-top: 6px solid #666;
                margin-right: 8px;
            }}
            QComboBox QAbstractItemView {{
                border: 1px solid {c['border']};
                border-radius: {DesignSystem.RADIUS['md']}px;
                background-color: {c['surface']};
                selection-background-color: {c['success_light']};
            }}
        """)
        layout.addWidget(combo)
        
        return {'layout': layout, 'combo': combo}
    
    def create_text_area_group(self, label_text, placeholder):
        """创建文本区域组"""
        layout = QVBoxLayout()
        layout.setSpacing(8)
        
        # 标签
        label = QLabel(label_text)
        c = DesignSystem.COLORS
        label.setStyleSheet(f"""
            QLabel {{
                font-size: {DesignSystem.FONT_SIZES['lg']}px;
                font-weight: 600;
                color: {c['text_primary']};
                margin: 0;
            }}
        """)
        layout.addWidget(label)
        
        # 文本区域
        textarea = QTextEdit()
        textarea.setPlaceholderText(placeholder)
        textarea.setMaximumHeight(120)
        textarea.setMinimumHeight(80)
        c = DesignSystem.COLORS
        textarea.setStyleSheet(f"""
            QTextEdit {{
                border: 2px solid {c['border']};
                border-radius: {DesignSystem.RADIUS['md']}px;
                padding: 14px 16px;
                font-size: {DesignSystem.FONT_SIZES['lg']}px;
                background-color: {c['surface_hover']};
                font-family: 'Microsoft YaHei UI', sans-serif;
            }}
            QTextEdit:focus {{
                border-color: {c['success']};
                background-color: {c['surface']};
            }}
            QTextEdit:hover {{
                border-color: {c['border_hover']};
                background-color: {c['surface']};
            }}
        """)
        layout.addWidget(textarea)
        
        return {'layout': layout, 'textarea': textarea}
    
    def create_large_text_area_group(self, label_text, placeholder):
        """创建大文本区域组"""
        layout = QVBoxLayout()
        layout.setSpacing(8)
        
        # 标签
        label = QLabel(label_text)
        c = DesignSystem.COLORS
        label.setStyleSheet(f"""
            QLabel {{
                font-size: {DesignSystem.FONT_SIZES['lg']}px;
                font-weight: 600;
                color: {c['text_primary']};
                margin: 0;
            }}
        """)
        layout.addWidget(label)
        
        # 大文本区域
        textarea = QTextEdit()
        textarea.setPlaceholderText(placeholder)
        textarea.setMaximumHeight(150)
        textarea.setMinimumHeight(100)
        c = DesignSystem.COLORS
        textarea.setStyleSheet(f"""
            QTextEdit {{
                border: 2px solid {c['border']};
                border-radius: {DesignSystem.RADIUS['md']}px;
                padding: 14px 16px;
                font-size: {DesignSystem.FONT_SIZES['lg']}px;
                background-color: {c['surface_hover']};
                font-family: 'Microsoft YaHei UI', sans-serif;
                line-height: {DesignSystem.LINE_HEIGHTS['relaxed']};
            }}
            QTextEdit:focus {{
                border-color: {c['success']};
                background-color: {c['surface']};
            }}
            QTextEdit:hover {{
                border-color: {c['border_hover']};
                background-color: {c['surface']};
            }}
        """)
        layout.addWidget(textarea)
        
        return {'layout': layout, 'textarea': textarea}
    
    def create_folder_creation_group(self):
        """创建文件夹创建选项组"""
        layout = QVBoxLayout()
        layout.setSpacing(8)
        
        # 复选框
        self.create_folder_checkbox = QCheckBox("创建项目文件夹")
        c = DesignSystem.COLORS
        self.create_folder_checkbox.setStyleSheet(f"""
            QCheckBox {{
                font-size: {DesignSystem.FONT_SIZES['lg']}px;
                font-weight: 600;
                color: {c['text_primary']};
                spacing: 8px;
            }}
            QCheckBox::indicator {{
                width: 18px;
                height: 18px;
                border: 2px solid {c['border']};
                border-radius: {DesignSystem.RADIUS['sm']}px;
                background-color: {c['surface_hover']};
            }}
            QCheckBox::indicator:hover {{
                border-color: {c['success']};
                background-color: {c['surface']};
            }}
            QCheckBox::indicator:checked {{
                background-color: {c['success']};
                border-color: {c['success']};
                image: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIiIGhlaWdodD0iOSIgdmlld0JveD0iMCAwIDEyIDkiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjxwYXRoIGQ9Ik0xIDQuNUw0LjUgOEwxMSAxIiBzdHJva2U9IndoaXRlIiBzdHJva2Utd2lkdGg9IjIiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIvPgo8L3N2Zz4K);
            }}
        """)
        self.create_folder_checkbox.stateChanged.connect(self.on_folder_checkbox_changed)
        layout.addWidget(self.create_folder_checkbox)
        
        # 路径选择区域
        path_layout = QHBoxLayout()
        path_layout.setSpacing(8)
        path_layout.setContentsMargins(0, 0, 0, 0)  # 确保没有额外的边距
        
        # 路径输入框
        self.folder_path_edit = QLineEdit()
        self.folder_path_edit.setPlaceholderText("选择项目文件夹的父目录...")
        self.folder_path_edit.setEnabled(False)
        self.folder_path_edit.setMinimumHeight(44)  # 确保与按钮高度一致
        c = DesignSystem.COLORS
        self.folder_path_edit.setStyleSheet(f"""
            QLineEdit {{
                border: 2px solid {c['border']};
                border-radius: {DesignSystem.RADIUS['md']}px;
                padding: 12px 16px;
                font-size: {DesignSystem.FONT_SIZES['lg']}px;
                background-color: {c['surface_pressed']};
                min-height: 20px;
            }}
            QLineEdit:enabled {{
                background-color: {c['surface_hover']};
            }}
            QLineEdit:enabled:focus {{
                border-color: {c['success']};
                background-color: {c['surface']};
            }}
            QLineEdit:enabled:hover {{
                border-color: {c['border_hover']};
                background-color: {c['surface']};
            }}
        """)
        path_layout.addWidget(self.folder_path_edit)
        
        # 浏览按钮
        self.browse_btn = QPushButton("浏览")
        self.browse_btn.setEnabled(False)
        self.browse_btn.setFixedWidth(80)  # 只固定宽度，高度自适应
        self.browse_btn.setMinimumHeight(44)  # 设置最小高度
        c = DesignSystem.COLORS
        self.browse_btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {c['surface_pressed']};
                border: 2px solid {c['border']};
                border-radius: {DesignSystem.RADIUS['md']}px;
                font-size: {DesignSystem.FONT_SIZES['lg']}px;
                font-weight: 600;
                color: {c['text_tertiary']};
            }}
            QPushButton:enabled {{
                background-color: {c['success']};
                border-color: {c['success']};
                color: white;
            }}
            QPushButton:enabled:hover {{
                background-color: {c['success_hover']};
                border-color: {c['success_hover']};
            }}
            QPushButton:enabled:pressed {{
                background-color: {c['success_pressed']};
            }}
        """)
        self.browse_btn.clicked.connect(self.browse_folder)
        path_layout.addWidget(self.browse_btn)
        
        layout.addLayout(path_layout)
        layout.addSpacing(5)  # 在底部添加一些空间
        
        return {
            'layout': layout,
            'checkbox': self.create_folder_checkbox,
            'path_edit': self.folder_path_edit,
            'browse_btn': self.browse_btn
        }
    
    def on_folder_checkbox_changed(self, state):
        """文件夹复选框状态改变事件"""
        enabled = state == Qt.Checked
        self.folder_path_edit.setEnabled(enabled)
        self.browse_btn.setEnabled(enabled)
        
        if enabled and not self.folder_path_edit.text():
            # 优先使用配置的默认项目路径
            default_path = ''
            if hasattr(self.parent(), 'default_project_path') and self.parent().default_project_path:
                default_path = self.parent().default_project_path
            else:
                # 如果没有配置默认路径，使用用户文档目录
                default_path = os.path.expanduser("~/Documents")
            
            if default_path and os.path.exists(default_path):
                self.folder_path_edit.setText(default_path)
    
    def browse_folder(self):
        """浏览文件夹"""
        current_path = self.folder_path_edit.text() or os.path.expanduser("~/Documents")
        folder_path = QFileDialog.getExistingDirectory(
            self,
            "选择项目文件夹的父目录",
            current_path
        )
        if folder_path:
            # 规范化路径，统一使用系统默认的路径分隔符
            normalized_path = os.path.normpath(folder_path)
            self.folder_path_edit.setText(normalized_path)
    
    def populate_edit_data(self):
        """预填充编辑数据"""
        if self.edit_project:
            self.name_edit.setText(self.edit_project.get('name', ''))
            self.desc_edit.setPlainText(self.edit_project.get('description', ''))
            
            # 设置项目类型
            project_type = self.edit_project.get('type', '')
            index = self.type_combo.findText(project_type)
            if index >= 0:
                self.type_combo.setCurrentIndex(index)
            
            # 设置项目状态
            project_status = self.edit_project.get('status', '未开始')
            status_index = self.status_combo.findText(project_status)
            if status_index >= 0:
                self.status_combo.setCurrentIndex(status_index)
            
            # 设置标签
            tags = self.edit_project.get('tags', [])
            if tags:
                tags_text = ', '.join(tags)
                self.tags_edit.setText(tags_text)
            
            # 设置项目文件夹路径
            folder_path = self.edit_project.get('folder_path', '')
            if folder_path and os.path.exists(folder_path):
                # 项目已有文件夹路径且文件夹存在
                self.create_folder_checkbox.setChecked(True)
                # 规范化路径显示
                normalized_path = os.path.normpath(folder_path)
                self.folder_path_edit.setText(normalized_path)
                # 复选框状态改变会自动启用相关控件
            else:
                # 项目没有文件夹路径或文件夹不存在（历史项目）
                self.create_folder_checkbox.setChecked(False)
                # 为历史项目设置默认路径，方便用户创建文件夹
                default_path = ''
                if hasattr(self.parent(), 'default_project_path') and self.parent().default_project_path:
                    default_path = self.parent().default_project_path
                else:
                    default_path = os.path.expanduser("~/Documents")
                
                if default_path and os.path.exists(default_path):
                    # 规范化默认路径
                    normalized_default_path = os.path.normpath(default_path)
                    self.folder_path_edit.setText(normalized_default_path)
    
    def accept_project(self):
        """验证并接受项目创建"""
        name = self.name_edit.text().strip()
        if not name:
            QMessageBox.warning(self, "警告", "请输入项目名称！")
            return
        
        # 检查项目名称是否重复（仅在新建模式下检查）
        if not self.is_edit_mode:
            parent_tool = self.parent()
            if parent_tool and hasattr(parent_tool, 'projects'):
                for existing_project in parent_tool.projects:
                    if existing_project.get('name', '').strip() == name:
                        QMessageBox.warning(self, "重复项目名称", 
                                          f"项目名称 '{name}' 已存在，请使用不同的名称！")
                        return
        
        self.accept()
    
    def get_project_data(self):
        """获取项目数据"""
        tags_text = self.tags_edit.text().strip()
        tags = [tag.strip() for tag in tags_text.split(',') if tag.strip()] if tags_text else []
        
        project_data = {
            'name': self.name_edit.text().strip(),
            'description': self.desc_edit.toPlainText().strip(),
            'type': self.type_combo.currentText(),
            'status': self.status_combo.currentText(),
            'tags': tags
        }
        
        # 添加文件夹创建信息
        if hasattr(self, 'create_folder_checkbox') and self.create_folder_checkbox.isChecked():
            project_data['create_folder'] = True
            # 规范化路径，统一使用系统默认的路径分隔符
            folder_path = self.folder_path_edit.text().strip()
            project_data['folder_path'] = os.path.normpath(folder_path) if folder_path else ''
        else:
            project_data['create_folder'] = False
            project_data['folder_path'] = ''
        
        return project_data



class DefaultProjectPathDialog(QDialog):
    """默认项目路径设置对话框"""
    
    def __init__(self, parent=None, current_path=None):
        super().__init__(parent)
        self.current_path = current_path or ''
        self.init_ui()
    
    def init_ui(self):
        """初始化UI"""
        self.setWindowTitle("默认项目路径设置")
        width, height = get_optimal_dialog_size(700, 850)
        self.setFixedSize(width, height)
        center_window(self)
        
        # 设置对话框样式
        c = DesignSystem.COLORS
        self.setStyleSheet(f"""
            QDialog {{
                background-color: {c['background']};
            }}
        """)
        
        main_layout = QVBoxLayout(self)
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(0, 0, 0, 0)
        
        # 创建内容区域
        content_widget = QFrame()
        c = DesignSystem.COLORS
        content_widget.setStyleSheet(f"""
            QFrame {{
                background-color: {c['surface']};
                border-radius: {DesignSystem.RADIUS['lg']}px;
                margin: 20px;
            }}
        """)
        
        content_layout = QVBoxLayout(content_widget)
        content_layout.setSpacing(25)
        content_layout.setContentsMargins(35, 35, 35, 35)
        
        # 标题区域
        header_layout = QVBoxLayout()
        header_layout.setSpacing(8)
        
        title_label = QLabel("🗂️ 默认项目路径设置")
        c = DesignSystem.COLORS
        title_label.setStyleSheet(f"""
            QLabel {{
                font-size: 24px;
                font-weight: bold;
                color: {c['text_primary']};
                margin: 0;
            }}
        """)
        header_layout.addWidget(title_label)
        
        # 说明文字
        desc_label = QLabel("设置创建新项目时的默认文件夹路径。如果不设置，将使用系统文档目录作为默认位置。")
        c = DesignSystem.COLORS
        desc_label.setStyleSheet(f"""
            QLabel {{
                color: {c['text_secondary']};
                font-size: 15px;
                line-height: {DesignSystem.LINE_HEIGHTS['relaxed']};
                margin: 0;
            }}
        """)
        desc_label.setWordWrap(True)
        header_layout.addWidget(desc_label)
        
        content_layout.addLayout(header_layout)
        
        # 路径设置区域
        path_group = QGroupBox("路径配置")
        c = DesignSystem.COLORS
        path_group.setStyleSheet(f"""
            QGroupBox {{
                font-weight: 600;
                font-size: 16px;
                border: 2px solid {c['border']};
                border-radius: {DesignSystem.RADIUS['lg']}px;
                margin-top: 15px;
                padding-top: 15px;
                background-color: {c['background']};
            }}
            QGroupBox::title {{
                subcontrol-origin: margin;
                left: 15px;
                padding: 0 10px 0 10px;
                color: {c['text_primary']};
                background-color: {c['surface']};
            }}
        """)
        path_layout = QVBoxLayout(path_group)
        path_layout.setSpacing(20)
        path_layout.setContentsMargins(20, 25, 20, 20)
        
        # 当前路径显示（如果有）
        if self.current_path:
            current_label = QLabel("当前路径:")
            c = DesignSystem.COLORS
            current_label.setStyleSheet(f"""
                QLabel {{
                    font-size: {DesignSystem.FONT_SIZES['lg']}px;
                    font-weight: 600;
                    color: {c['text_primary']};
                    margin-bottom: 5px;
                }}
            """)
            path_layout.addWidget(current_label)
            
            current_path_display = QLabel(self.current_path)
            current_path_display.setStyleSheet(f"""
                QLabel {{
                    padding: 10px;
                    background-color: {c['surface_hover']};
                    border-radius: {DesignSystem.RADIUS['sm']}px;
                    font-size: 13px;
                    color: {c['text_secondary']};
                    font-family: 'Consolas', 'Monaco', monospace;
                }}
            """)
            current_path_display.setWordWrap(True)
            path_layout.addWidget(current_path_display)
        
        # 新路径输入标签
        input_label = QLabel("新路径设置:")
        c = DesignSystem.COLORS
        input_label.setStyleSheet(f"""
            QLabel {{
                font-size: {DesignSystem.FONT_SIZES['lg']}px;
                font-weight: 600;
                color: {c['text_primary']};
                margin-bottom: 5px;
                margin-top: 10px;
            }}
        """)
        path_layout.addWidget(input_label)
        
        # 路径输入区域
        input_layout = QHBoxLayout()
        input_layout.setSpacing(12)
        
        self.path_edit = QLineEdit()
        self.path_edit.setText(self.current_path)
        self.path_edit.setPlaceholderText("请选择或输入默认项目路径...")
        self.path_edit.setMinimumHeight(45)  # 增加输入框高度
        c = DesignSystem.COLORS
        self.path_edit.setStyleSheet(f"""
                 QLineEdit {{
                     padding: 12px 15px;
                     border: 2px solid {c['border']};
                     border-radius: {DesignSystem.RADIUS['md']}px;
                     font-size: {DesignSystem.FONT_SIZES['lg']}px;
                     background-color: {c['surface']};
                     font-family: 'Segoe UI', Arial, sans-serif;
                 }}
                 QLineEdit:focus {{
                     border-color: {c['primary']};
                 }}
                 QLineEdit:hover {{
                     border-color: {c['border_hover']};
                 }}
             """)
        # 添加实时验证
        self.path_edit.textChanged.connect(self.on_path_changed)
        input_layout.addWidget(self.path_edit, 1)
        
        browse_btn = QPushButton("📁 浏览")
        browse_btn.setMinimumHeight(45)
        browse_btn.setMinimumWidth(100)
        c = DesignSystem.COLORS
        browse_btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {c['primary']};
                color: white;
                border: none;
                padding: 12px 20px;
                border-radius: {DesignSystem.RADIUS['md']}px;
                font-weight: 600;
                font-size: {DesignSystem.FONT_SIZES['lg']}px;
            }}
            QPushButton:hover {{
                background-color: {c['primary_hover']};
            }}
            QPushButton:pressed {{
                background-color: {c['primary_pressed']};
            }}
        """)
        browse_btn.clicked.connect(self.browse_path)
        input_layout.addWidget(browse_btn)
        
        path_layout.addLayout(input_layout)
        
        # 操作按钮区域
        action_layout = QHBoxLayout()
        action_layout.setSpacing(10)
        
        # 清空按钮
        clear_btn = QPushButton("🗑️ 清空路径")
        clear_btn.setMinimumHeight(35)
        c = DesignSystem.COLORS
        clear_btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {c['text_secondary']};
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: {DesignSystem.RADIUS['md']}px;
                font-size: 13px;
                font-weight: 500;
            }}
            QPushButton:hover {{
                background-color: {c['text_primary']};
            }}
            QPushButton:pressed {{
                background-color: {c['text_primary']};
            }}
        """)
        clear_btn.clicked.connect(self.clear_path)
        action_layout.addWidget(clear_btn)
        
        # 使用默认路径按钮
        default_btn = QPushButton("📂 使用文档目录")
        default_btn.setMinimumHeight(35)
        c = DesignSystem.COLORS
        default_btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {c['success']};
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: {DesignSystem.RADIUS['md']}px;
                font-size: 13px;
                font-weight: 500;
            }}
            QPushButton:hover {{
                background-color: {c['success_hover']};
            }}
            QPushButton:pressed {{
                background-color: {c['success_pressed']};
            }}
        """)
        default_btn.clicked.connect(self.use_default_path)
        action_layout.addWidget(default_btn)
        
        action_layout.addStretch()
        path_layout.addLayout(action_layout)
        
        content_layout.addWidget(path_group)
        
        # 添加一些提示信息
        tips_label = QLabel("💡 提示: 路径可以手动输入或通过浏览按钮选择。清空路径将使用系统默认的文档目录。")
        c = DesignSystem.COLORS
        tips_label.setStyleSheet(f"""
            QLabel {{
                color: {c['text_secondary']};
                font-size: 13px;
                padding: 15px;
                background-color: {c['background']};
                border-radius: {DesignSystem.RADIUS['md']}px;
                border-left: 4px solid {c['primary']};
            }}
        """)
        tips_label.setWordWrap(True)
        content_layout.addWidget(tips_label)
        
        # 按钮区域
        button_layout = QHBoxLayout()
        button_layout.setSpacing(15)
        button_layout.addStretch()
        
        cancel_btn = QPushButton("❌ 取消")
        cancel_btn.setMinimumHeight(45)
        cancel_btn.setMinimumWidth(120)
        c = DesignSystem.COLORS
        cancel_btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {c['text_secondary']};
                color: white;
                border: none;
                padding: 12px 24px;
                border-radius: {DesignSystem.RADIUS['md']}px;
                font-weight: 600;
                font-size: {DesignSystem.FONT_SIZES['lg']}px;
            }}
            QPushButton:hover {{
                background-color: {c['text_primary']};
            }}
            QPushButton:pressed {{
                background-color: {c['text_primary']};
            }}
        """)
        cancel_btn.clicked.connect(self.reject)
        button_layout.addWidget(cancel_btn)
        
        save_btn = QPushButton("✅ 保存设置")
        save_btn.setMinimumHeight(45)
        save_btn.setMinimumWidth(120)
        c = DesignSystem.COLORS
        save_btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {c['success']};
                color: white;
                border: none;
                padding: 12px 24px;
                border-radius: {DesignSystem.RADIUS['md']}px;
                font-weight: 600;
                font-size: {DesignSystem.FONT_SIZES['lg']}px;
            }}
            QPushButton:hover {{
                background-color: {c['success_hover']};
            }}
            QPushButton:pressed {{
                background-color: {c['success_pressed']};
            }}
        """)
        save_btn.clicked.connect(self.accept)
        save_btn.setDefault(True)  # 设置为默认按钮
        button_layout.addWidget(save_btn)
        
        content_layout.addLayout(button_layout)
        main_layout.addWidget(content_widget)
    
    def browse_path(self):
        """浏览文件夹"""
        current_path = self.path_edit.text() or os.path.expanduser("~/Documents")
        path = QFileDialog.getExistingDirectory(
            self, 
            "选择默认项目路径", 
            current_path,
            QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks
        )
        if path:
            self.path_edit.setText(os.path.normpath(path))
            # 显示路径验证结果
            self.validate_path(path)
    
    def clear_path(self):
        """清空路径设置"""
        self.path_edit.clear()
        self.path_edit.setPlaceholderText("将使用系统默认文档目录...")
    
    def use_default_path(self):
        """使用系统默认文档目录"""
        default_path = os.path.expanduser("~/Documents")
        self.path_edit.setText(default_path)
        self.validate_path(default_path)
    
    def on_path_changed(self, text):
        """路径输入框内容改变时的处理"""
        # 延迟验证，避免频繁验证
        if hasattr(self, '_validation_timer'):
            self._validation_timer.stop()
        
        from PyQt5.QtCore import QTimer
        self._validation_timer = QTimer()
        self._validation_timer.setSingleShot(True)
        self._validation_timer.timeout.connect(lambda: self.validate_path(text))
        self._validation_timer.start(500)  # 500ms延迟
    
    def validate_path(self, path):
        """验证路径是否有效"""
        if not path.strip():
            # 空路径，恢复默认样式
            c = DesignSystem.COLORS
            self.path_edit.setStyleSheet(f"""
                QLineEdit {{
                    padding: 12px 15px;
                    border: 2px solid {c['border']};
                    border-radius: {DesignSystem.RADIUS['md']}px;
                    font-size: {DesignSystem.FONT_SIZES['lg']}px;
                    background-color: {c['surface']};
                    font-family: 'Segoe UI', Arial, sans-serif;
                }}
                QLineEdit:focus {{
                    border-color: {c['primary']};
                    box-shadow: {DesignSystem.SHADOWS['md']};
                }}
                QLineEdit:hover {{
                    border-color: {c['border_hover']};
                }}
            """)
            return
        
        if os.path.exists(path) and os.path.isdir(path):
            # 检查是否有写入权限
            if os.access(path, os.W_OK):
                c = DesignSystem.COLORS
                self.path_edit.setStyleSheet(f"""
                    QLineEdit {{
                        padding: 12px 15px;
                        border: 2px solid {c['success']};
                        border-radius: {DesignSystem.RADIUS['md']}px;
                        font-size: {DesignSystem.FONT_SIZES['lg']}px;
                        background-color: {c['surface']};
                        font-family: 'Segoe UI', Arial, sans-serif;
                    }}
                    QLineEdit:focus {{
                        border-color: {c['success_hover']};
                    }}
                """)
            else:
                c = DesignSystem.COLORS
                self.path_edit.setStyleSheet(f"""
                    QLineEdit {{
                        padding: 12px 15px;
                        border: 2px solid {c['warning']};
                        border-radius: {DesignSystem.RADIUS['md']}px;
                        font-size: {DesignSystem.FONT_SIZES['lg']}px;
                        background-color: {c['surface']};
                        font-family: 'Segoe UI', Arial, sans-serif;
                    }}
                    QLineEdit:focus {{
                        border-color: {c['warning_hover']};
                    }}
                """)
        else:
            c = DesignSystem.COLORS
            self.path_edit.setStyleSheet(f"""
                QLineEdit {{
                    padding: 12px 15px;
                    border: 2px solid {c['danger']};
                    border-radius: {DesignSystem.RADIUS['md']}px;
                    font-size: {DesignSystem.FONT_SIZES['lg']}px;
                    background-color: {c['surface']};
                    font-family: 'Segoe UI', Arial, sans-serif;
                }}
                QLineEdit:focus {{
                    border-color: {c['danger_hover']};
                }}
            """)
    
    def get_path(self):
        """获取设置的路径"""
        path = self.path_edit.text().strip()
        # 如果路径为空或无效，返回空字符串
        if not path or not os.path.exists(path):
            return ""
        return path


class ProjectTypeConfigDialog(QDialog):
    """项目类型配置对话框"""
    
    def __init__(self, parent=None, project_types=None):
        super().__init__(parent)
        self.project_types = project_types.copy() if project_types else []
        self.init_ui()
    
    def init_ui(self):
        """初始化UI"""
        self.setWindowTitle("项目类型配置")
        width, height = get_optimal_dialog_size(500, 400)
        self.setFixedSize(width, height)
        center_window(self)
        
        layout = QVBoxLayout(self)
        layout.setSpacing(16)
        layout.setContentsMargins(20, 20, 20, 20)
        
        # 标题
        title_label = QLabel("项目类型配置")
        c = DesignSystem.COLORS
        title_label.setStyleSheet(f"""
            QLabel {{
                font-size: 18px;
                font-weight: bold;
                color: {c['primary']};
                margin-bottom: 10px;
            }}
        """)
        layout.addWidget(title_label)
        
        # 说明文字
        desc_label = QLabel("管理项目类型的枚举值，用于项目分类")
        c = DesignSystem.COLORS
        desc_label.setStyleSheet(f"""
            QLabel {{
                color: {c['text_secondary']};
                font-size: 12px;
                margin-bottom: 10px;
            }}
        """)
        layout.addWidget(desc_label)
        
        # 项目类型列表
        list_layout = QHBoxLayout()
        
        # 左侧列表
        left_layout = QVBoxLayout()
        left_layout.addWidget(QLabel("项目类型列表:"))
        
        self.type_list = QListWidget()
        self.type_list.setStyleSheet(DesignSystem.list_style())
        
        # 加载现有项目类型
        for project_type in self.project_types:
            self.type_list.addItem(project_type)
        
        left_layout.addWidget(self.type_list)
        list_layout.addLayout(left_layout)
        
        # 右侧按钮
        button_layout = QVBoxLayout()
        button_layout.addStretch()
        
        self.add_btn = QPushButton("添加")
        self.add_btn.clicked.connect(self.add_type)
        self.add_btn.setStyleSheet(DesignSystem.button_style('success'))
        button_layout.addWidget(self.add_btn)
        
        self.edit_btn = QPushButton("编辑")
        self.edit_btn.clicked.connect(self.edit_type)
        self.edit_btn.setStyleSheet(DesignSystem.button_style('primary'))
        button_layout.addWidget(self.edit_btn)
        
        self.delete_btn = QPushButton("删除")
        self.delete_btn.clicked.connect(self.delete_type)
        self.delete_btn.setStyleSheet(DesignSystem.button_style('danger'))
        button_layout.addWidget(self.delete_btn)
        
        button_layout.addStretch()
        list_layout.addLayout(button_layout)
        
        layout.addLayout(list_layout)
        
        # 底部按钮
        bottom_layout = QHBoxLayout()
        bottom_layout.addStretch()
        
        self.ok_btn = QPushButton("确定")
        self.ok_btn.clicked.connect(self.accept)
        self.ok_btn.setStyleSheet(DesignSystem.button_style('primary'))
        bottom_layout.addWidget(self.ok_btn)
        
        self.cancel_btn = QPushButton("取消")
        self.cancel_btn.clicked.connect(self.reject)
        self.cancel_btn.setStyleSheet(DesignSystem.button_style('secondary'))
        bottom_layout.addWidget(self.cancel_btn)
        
        layout.addLayout(bottom_layout)
    
    def add_type(self):
        """添加项目类型"""
        text, ok = QInputDialog.getText(self, "添加项目类型", "请输入项目类型名称:")
        if ok and text.strip():
            text = text.strip()
            if text not in self.project_types:
                self.project_types.append(text)
                self.type_list.addItem(text)
            else:
                QMessageBox.warning(self, "警告", "该项目类型已存在！")
    
    def edit_type(self):
        """编辑项目类型"""
        current_item = self.type_list.currentItem()
        if current_item:
            old_text = current_item.text()
            text, ok = QInputDialog.getText(self, "编辑项目类型", "请输入项目类型名称:", text=old_text)
            if ok and text.strip():
                text = text.strip()
                if text != old_text and text in self.project_types:
                    QMessageBox.warning(self, "警告", "该项目类型已存在！")
                    return
                
                # 更新列表和数据
                index = self.project_types.index(old_text)
                self.project_types[index] = text
                current_item.setText(text)
        else:
            QMessageBox.information(self, "提示", "请先选择要编辑的项目类型！")
    
    def delete_type(self):
        """删除项目类型"""
        current_item = self.type_list.currentItem()
        if current_item:
            text = current_item.text()
            reply = QMessageBox.question(self, "确认删除", f"确定要删除项目类型 '{text}' 吗？",
                                       QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.project_types.remove(text)
                self.type_list.takeItem(self.type_list.row(current_item))
        else:
            QMessageBox.information(self, "提示", "请先选择要删除的项目类型！")
    
    def get_project_types(self):
        """获取项目类型列表"""
        return self.project_types.copy()


class ProjectDetailDialog(QDialog):
    """项目详情对话框"""
    
    def __init__(self, parent=None, project=None):
        super().__init__(parent)
        self.project = project
        self.parent_tool = parent
        self.setAcceptDrops(True)  # 启用拖拽功能
        
        # 确保每次打开项目详情时都获取最新的项目数据
        if self.project and self.parent_tool:
            # 重新从数据文件加载最新数据，确保获取到最新的项目资源信息
            self.parent_tool.load_data()
            
            # 从父工具中获取最新的项目数据（包含最新的资源信息）
            project_name = self.project.get('name')
            if project_name:
                # 在父工具的项目列表中查找最新的项目数据
                for latest_project in self.parent_tool.projects:
                    if latest_project.get('name') == project_name:
                        # 使用最新的项目数据，确保资源信息是最新的
                        self.project = latest_project.copy()
                        break
            
            # 从markdown文件加载项目数据（笔记和清单）
            self.load_from_markdown_file()
            # 确保每次打开对话框时都刷新最近打开的资源信息
            self.recently_opened_resource = self.get_recently_opened_resource()
        
        self.init_ui()
    
    def showEvent(self, event):
        """窗口显示事件，检查是否需要自动扫描项目文件夹"""
        super().showEvent(event)
        
        # 检查是否启用了自动扫描功能
        if self.project and self.project.get('auto_scan_resources', False):
            # 使用QTimer延迟执行自动扫描，确保界面完全显示后再执行
            QTimer.singleShot(500, self.auto_scan_on_open)
    
    def auto_scan_on_open(self):
        """在打开项目详情时执行自动扫描"""
        try:
            # 调用现有的扫描方法
            self.scan_project_folder_now()
            
            # 在状态栏显示提示信息
            if hasattr(self, 'status_bar'):
                self.status_bar.showMessage("✅ 已自动扫描项目文件夹并更新资源列表", 3000)
        except Exception as e:
            # 如果扫描出错，显示错误信息
            if hasattr(self, 'status_bar'):
                self.status_bar.showMessage(f"❌ 自动扫描失败: {str(e)}", 3000)
            logging.error(f"自动扫描项目文件夹失败: {str(e)}")
    
    def sync_and_save_project(self, create_backup=False):
        """同步项目数据到父工具并保存
        
        这个方法确保：
        1. 对话框中的项目数据同步到父工具的项目列表中
        2. 调用save_data()保存到文件
        3. 更新项目修改时间
        
        Args:
            create_backup (bool): 是否创建备份，默认为False
        """
        if not self.project or not self.parent_tool:
            return
        
        # 获取项目名称
        project_name = self.project.get('name')
        if not project_name:
            return
        
        # 在父工具的项目列表中找到对应的项目并更新
        for parent_project in self.parent_tool.projects:
            if parent_project.get('name') == project_name:
                # 同步所有项目数据
                parent_project.update(self.project)
                # 更新资源总数字段
                parent_project['resource_count'] = len(parent_project.get('resources', []))
                # 更新修改时间
                parent_project['modified_time'] = datetime.now().isoformat()
                break
        
        # 保存数据到文件
        self.parent_tool.save_data(create_backup=create_backup)
        
        # 刷新项目列表
        self.parent_tool.refresh_project_list()
    
    def dragEnterEvent(self, event):
        """拖拽进入事件"""
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()
    
    def dropEvent(self, event):
        """拖拽放下事件"""
        files = [u.toLocalFile() for u in event.mimeData().urls()]
        if files:
            # 收集所有有效文件
            valid_files = []
            
            for file_path in files:
                if os.path.isfile(file_path):
                    # 如果是文件，直接添加
                    valid_files.append(file_path)
                elif os.path.isdir(file_path):
                    # 如果是文件夹，遍历所有子文件夹中的文件
                    for root, dirs, folder_files in os.walk(file_path):
                        for file in folder_files:
                            full_path = os.path.join(root, file)
                            if os.path.isfile(full_path):
                                valid_files.append(full_path)
            
            if not valid_files:
                QMessageBox.warning(self, "警告", "未找到有效文件！")
                return
            
            # 处理拖拽的文件
            self.handle_dropped_files(valid_files)
    
    def handle_dropped_files(self, file_paths):
        """处理拖拽的文件"""
        if not self.project or 'resources' not in self.project:
            self.project['resources'] = []
        
        added_count = 0
        existing_count = 0
        
        for file_path in file_paths:
            # 检查文件是否已经存在于项目资源中
            existing_resource = self.find_existing_resource(file_path)
            
            if existing_resource:
                # 文件已存在，显示现有资源信息
                existing_count += 1
                continue
            
            # 文件不存在，添加为新资源
            try:
                # 获取文件信息
                file_name = os.path.basename(file_path)
                file_ext = os.path.splitext(file_path)[1].lower()
                
                # 确定资源类型（默认为空）
                resource_type = ''
                
                # 创建资源数据
                resource_data = {
                    'name': os.path.splitext(file_name)[0],  # 不包含扩展名的文件名
                    'path': file_path,
                    'type': resource_type,
                    'category': '默认',
                    'description': '',
                    'tags': [],
                    'created_time': datetime.now().isoformat(),
                'modified_time': datetime.now().isoformat()
                }
                
                # 添加到项目资源
                self.project['resources'].append(resource_data)
                added_count += 1
                
            except Exception as e:
                QMessageBox.warning(self, "添加失败", f"添加文件 {file_path} 失败：{str(e)}")
        
        # 保存数据并刷新界面
        if added_count > 0:
            self.parent_tool.update_project_modified_time(self.project['name'], save_immediately=False)
            self.parent_tool.save_data(create_backup=True)  # 移除资源时创建备份
            self.parent_tool.refresh_project_list()
            
            # 记录项目日志
            if added_count == 1:
                self.parent_tool.add_project_log(self.project['name'], "拖拽添加资源", 
                                                f"通过拖拽添加资源: {os.path.basename(file_paths[0])}", 
                                                "资源")
            else:
                self.parent_tool.add_project_log(self.project['name'], "批量拖拽添加资源", 
                                                f"通过拖拽批量添加 {added_count} 个资源", 
                                                "资源")
            
            # 刷新资源列表
            self.load_resources()
        
        # 显示结果消息
        if added_count > 0 and existing_count > 0:
            message = f"✅ 成功添加 {added_count} 个新资源，{existing_count} 个文件已存在于项目中"
        elif added_count > 0:
            message = f"✅ 成功添加 {added_count} 个资源到项目"
        elif existing_count > 0:
            message = f"ℹ️ {existing_count} 个文件已存在于项目中，未重复添加"
        else:
            message = "❌ 没有文件被添加"
        
        self.parent_tool.status_bar.showMessage(message)
        
        # 显示toast提示
        try:
            toast = QLabel(message, self)
            toast.setStyleSheet("""
                QLabel {
                    background-color: rgba(0, 0, 0, 0.7);
                    color: white;
                    padding: 10px 20px;
                    border-radius: 4px;
                    font-size: 14px;
                }
            """)
            toast.adjustSize()
            
            # 计算位置（居中显示）
            x = (self.width() - toast.width()) // 2
            y = self.height() - toast.height() - 40  # 底部上方40像素
            toast.move(x, y)
            
            # 显示提示
            toast.show()
            
            # 设置定时器在指定时间后隐藏并删除提示
            QTimer.singleShot(3000, lambda: (toast.hide(), toast.deleteLater()))
        except Exception as e:
            print(f"显示Toast提示失败: {str(e)}")
    
    def find_existing_resource(self, file_path):
        """查找已存在的资源"""
        if not self.project or 'resources' not in self.project:
            return None
        
        normalized_path = os.path.normpath(file_path)
        
        for resource in self.project['resources']:
            existing_path = os.path.normpath(resource.get('path', ''))
            if existing_path == normalized_path:
                return resource
        
        return None
    
    def determine_resource_type(self, file_ext):
        """根据文件扩展名确定资源类型（统一使用resource_categories）"""
        # 统一使用resource_categories中的类型（参考资料、灵感火花、产出成品）
        # 默认返回空字符串，不设置默认类型
        return ''  # 默认为空，让用户自行选择
        
    def edit_project(self):
        """编辑项目"""
        if not self.project:
            QMessageBox.warning(self, "警告", "项目数据不存在！")
            return
        
        # 创建编辑对话框
        dialog = ProjectDialog(self.parent_tool, self.parent_tool.project_types, self.project)
        if dialog.exec_() == QDialog.Accepted:
            # 获取编辑后的数据
            updated_data = dialog.get_project_data()
            
            # 检查哪些字段发生了变化
            changes = []
            old_data = self.project
            folder_renamed = False
            folder_migrated = False
            
            # 检查项目名称是否发生变化，如果是则重命名文件夹
            if 'name' in updated_data and updated_data['name'] != old_data.get('name'):
                old_name = old_data.get('name')
                new_name = updated_data['name']
                
                # 如果项目有文件夹，尝试重命名
                if self.project.get('folder_path') and os.path.exists(self.project.get('folder_path')):
                    new_folder_path = self.parent_tool.rename_project_folder(self.project, old_name, new_name)
                    if new_folder_path:
                        updated_data['folder_path'] = new_folder_path
                        folder_renamed = True
                    else:
                        # 如果重命名失败，保持原有的文件夹路径
                        updated_data['folder_path'] = self.project.get('folder_path')
                        logging.warning(f"项目文件夹重命名失败，保持原路径: {self.project.get('folder_path')}")
                elif self.project.get('folder_path'):
                    # 如果项目有文件夹路径但文件夹不存在，保持原路径记录
                    updated_data['folder_path'] = self.project.get('folder_path')
                    logging.warning(f"项目文件夹不存在，保持原路径记录: {self.project.get('folder_path')}")
            
            # 检查文件夹路径是否发生变化（用户修改了项目文件夹地址）
            if 'folder_path' in updated_data and updated_data['folder_path'] != old_data.get('folder_path'):
                old_folder_path = old_data.get('folder_path', '')
                new_folder_path = updated_data['folder_path']
                
                # 如果不是因为项目名称变更导致的文件夹路径变化，则需要迁移文件夹
                if not folder_renamed and old_folder_path and os.path.exists(old_folder_path):
                    try:
                        # 判断用户输入的是完整路径还是父目录路径
                        if os.path.exists(new_folder_path) and os.path.isdir(new_folder_path):
                            # 如果新路径已存在且是目录，检查是否包含项目文件
                            project_name = updated_data.get('name', self.project.get('name', ''))
                            safe_name = "".join(c for c in project_name if c.isalnum() or c in (' ', '-', '_', '（', '）', '(', ')')).strip()
                            if not safe_name:
                                safe_name = "新项目"
                            
                            expected_notes_file = os.path.join(new_folder_path, f"{safe_name}_笔记.md")
                            
                            # 如果新路径下已有同名项目的笔记文件，说明用户指定的是完整的项目文件夹路径
                            if os.path.exists(expected_notes_file):
                                # 直接使用新路径，不需要迁移
                                logging.info(f"项目文件夹路径已更新为: {new_folder_path}")
                                folder_migrated = True
                            else:
                                # 新路径是一个空目录或父目录，需要迁移
                                migrated_folder_path = self.parent_tool.migrate_project_notes(
                                    self.project, updated_data['name'], old_folder_path, new_folder_path
                                )
                                if migrated_folder_path:
                                    updated_data['folder_path'] = migrated_folder_path
                                    folder_migrated = True
                                    logging.info(f"项目文件夹已迁移: {old_folder_path} -> {migrated_folder_path}")
                                else:
                                    # 迁移失败，保持原路径
                                    updated_data['folder_path'] = old_folder_path
                                    QMessageBox.warning(self, "迁移失败", "项目文件夹迁移失败，保持原路径")
                        else:
                            # 新路径不存在，需要创建并迁移
                            # 获取新路径的父目录
                            new_parent_path = os.path.dirname(new_folder_path)
                            if new_parent_path and not os.path.exists(new_parent_path):
                                os.makedirs(new_parent_path, exist_ok=True)
                            
                            # 如果用户指定的是完整的项目文件夹路径，直接使用
                            if os.path.basename(new_folder_path):  # 确保路径有文件夹名
                                # 创建新文件夹并迁移内容
                                os.makedirs(new_folder_path, exist_ok=True)
                                
                                # 迁移文件内容
                                import shutil
                                for item in os.listdir(old_folder_path):
                                    old_item_path = os.path.join(old_folder_path, item)
                                    new_item_path = os.path.join(new_folder_path, item)
                                    
                                    # 特殊处理笔记文件
                                    if item.endswith('_笔记.md'):
                                        try:
                                            # 检查文件大小
                                            if os.path.getsize(old_item_path) == 0:
                                                logging.warning(f"旧笔记文件为空，直接使用移动方式: {old_item_path}")
                                                shutil.move(old_item_path, new_item_path)
                                                logging.info(f"使用移动方式迁移空笔记文件: {old_item_path} -> {new_item_path}")
                                                continue
                                            
                                            # 优先使用直接移动方式迁移笔记文件
                                            try:
                                                # 直接使用shutil.move移动笔记文件
                                                shutil.move(old_item_path, new_item_path)
                                                logging.info(f"成功移动笔记文件: {old_item_path} -> {new_item_path}")
                                                
                                                # 移动成功后，如果需要更新项目名称或添加迁移日志，再打开文件修改
                                                need_update = False
                                                
                                                # 读取移动后的文件内容
                                                with open(new_item_path, 'r', encoding='utf-8') as f:
                                                    content = f.read()
                                                
                                                # 检查内容是否为空
                                                if not content or len(content.strip()) == 0:
                                                    logging.warning(f"笔记文件内容为空，不需要更新: {new_item_path}")
                                                    continue
                                                
                                                # 添加迁移日志
                                                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                                                migration_log = f"- **{timestamp}** [系统] 项目文件夹迁移 - 从 {old_folder_path} 迁移到 {new_folder_path}\n"
                                                
                                                # 查找项目日志部分并添加迁移记录
                                                log_section_marker = "## 项目日志\n"
                                                if log_section_marker in content:
                                                    parts = content.split(log_section_marker, 1)
                                                    if len(parts) == 2:
                                                        before_log = parts[0] + log_section_marker
                                                        after_log = parts[1]
                                                        new_content = before_log + migration_log + after_log
                                                    else:
                                                        new_content = content + "\n" + log_section_marker + "\n" + migration_log
                                                else:
                                                    new_content = content + "\n" + log_section_marker + "\n" + migration_log
                                                
                                                if new_content != content:
                                                    content = new_content
                                                    need_update = True
                                                
                                                # 如果需要更新文件内容，写入文件
                                                if need_update:
                                                    # 先备份原始内容
                                                    original_content = content
                                                    
                                                    # 写入更新后的内容
                                                    with open(new_item_path, 'w', encoding='utf-8') as f:
                                                        f.write(content)
                                                    
                                                    # 验证写入是否成功
                                                    if os.path.exists(new_item_path):
                                                        with open(new_item_path, 'r', encoding='utf-8') as f:
                                                            new_file_content = f.read()
                                                        
                                                        # 检查新文件内容是否完整
                                                        if not new_file_content or len(new_file_content) < len(original_content) * 0.9:
                                                            logging.error(f"写入的笔记文件内容不完整: {new_item_path}")
                                                            # 恢复原始内容
                                                            with open(new_item_path, 'w', encoding='utf-8') as f:
                                                                f.write(original_content)
                                                        else:
                                                            logging.info(f"成功更新了笔记文件的内容: {new_item_path}")
                                                    else:
                                                        logging.error(f"更新后的笔记文件不存在: {new_item_path}")
                                            except Exception as e:
                                                logging.error(f"移动笔记文件失败: {e}")
                                                # 如果移动失败，尝试复制
                                                try:
                                                    shutil.copy2(old_item_path, new_item_path)
                                                    logging.info(f"使用复制方式迁移笔记文件: {old_item_path} -> {new_item_path}")
                                                    # 复制成功后尝试删除原文件
                                                    if os.path.exists(new_item_path):
                                                        try:
                                                            os.remove(old_item_path)
                                                            logging.info(f"复制后删除原笔记文件: {old_item_path}")
                                                        except Exception as e3:
                                                            logging.error(f"删除原笔记文件失败: {e3}")
                                                except Exception as e2:
                                                    logging.error(f"复制笔记文件也失败: {e2}")
                                            continue
                                        except Exception as e:
                                            logging.error(f"处理笔记文件失败: {e}")
                                    
                                    # 处理非笔记文件
                                    try:
                                        if os.path.isfile(old_item_path):
                                            # 使用move而不是copy2，确保文件被移动而不是复制
                                            shutil.move(old_item_path, new_item_path)
                                            logging.info(f"移动文件: {old_item_path} -> {new_item_path}")
                                        elif os.path.isdir(old_item_path):
                                            # 对于目录，先复制再删除，以确保数据安全
                                            shutil.copytree(old_item_path, new_item_path)
                                            # 确认目录复制成功后删除原目录
                                            if os.path.exists(new_item_path):
                                                shutil.rmtree(old_item_path)
                                                logging.info(f"移动目录: {old_item_path} -> {new_item_path}")
                                            else:
                                                logging.error(f"目录复制失败，保留原目录: {old_item_path}")
                                    except Exception as move_error:
                                        logging.error(f"移动项目文件失败: {old_item_path} -> {str(move_error)}")
                                        # 如果移动失败，尝试复制
                                        try:
                                            if os.path.isfile(old_item_path):
                                                shutil.copy2(old_item_path, new_item_path)
                                                logging.info(f"使用复制方式迁移文件: {old_item_path} -> {new_item_path}")
                                                # 复制成功后尝试删除原文件
                                                if os.path.exists(new_item_path):
                                                    try:
                                                        os.remove(old_item_path)
                                                        logging.info(f"复制后删除原文件: {old_item_path}")
                                                    except Exception as e3:
                                                        logging.error(f"删除原文件失败: {e3}")
                                            elif os.path.isdir(old_item_path) and not os.path.exists(new_item_path):
                                                shutil.copytree(old_item_path, new_item_path)
                                                logging.info(f"使用复制方式迁移目录: {old_item_path} -> {new_item_path}")
                                                # 复制成功后尝试删除原目录
                                                if os.path.exists(new_item_path):
                                                    try:
                                                        shutil.rmtree(old_item_path)
                                                        logging.info(f"复制后删除原目录: {old_item_path}")
                                                    except Exception as e3:
                                                        logging.error(f"删除原目录失败: {e3}")
                                        except Exception as copy_error:
                                            logging.error(f"复制项目文件也失败: {old_item_path} -> {str(copy_error)}")
                                
                                # 检查是否还有未迁移的文件
                                remaining_files = []
                                if os.path.exists(old_folder_path):
                                    for root, dirs, files in os.walk(old_folder_path):
                                        for file in files:
                                            if not file.startswith('.'):
                                                remaining_files.append(os.path.join(root, file))
                                
                                # 删除旧文件夹（如果没有剩余文件）
                                if not remaining_files and os.path.exists(old_folder_path):
                                    try:
                                        shutil.rmtree(old_folder_path)
                                        logging.info(f"成功删除原文件夹: {old_folder_path}")
                                    except Exception as e:
                                        logging.error(f"删除原文件夹失败: {e}")
                                elif remaining_files:
                                    logging.warning(f"原文件夹中还有{len(remaining_files)}个未迁移的文件，保留文件夹: {old_folder_path}")
                                
                                folder_migrated = True
                                logging.info(f"项目文件夹已迁移: {old_folder_path} -> {new_folder_path}")
                            else:
                                # 用户指定的是父目录，使用 migrate_project_notes 方法
                                migrated_folder_path = self.parent_tool.migrate_project_notes(
                                    self.project, updated_data['name'], old_folder_path, new_folder_path
                                )
                                if migrated_folder_path:
                                    updated_data['folder_path'] = migrated_folder_path
                                    folder_migrated = True
                                    logging.info(f"项目文件夹已迁移: {old_folder_path} -> {migrated_folder_path}")
                                else:
                                    # 迁移失败，保持原路径
                                    updated_data['folder_path'] = old_folder_path
                                    QMessageBox.warning(self, "迁移失败", "项目文件夹迁移失败，保持原路径")
                                    
                    except Exception as e:
                        logging.error(f"迁移项目文件夹时发生错误: {e}")
                        updated_data['folder_path'] = old_folder_path
                        QMessageBox.warning(self, "迁移失败", f"项目文件夹迁移失败：{str(e)}")
            
            for key, new_value in updated_data.items():
                old_value = old_data.get(key)
                if old_value != new_value:
                    if key == 'name':
                        if folder_renamed:
                            changes.append(f"项目名称：{old_value} → {new_value}（文件夹已同步重命名）")
                        else:
                            changes.append(f"项目名称：{old_value} → {new_value}")
                    elif key == 'description':
                        changes.append(f"项目描述已更新")
                    elif key == 'type':
                        changes.append(f"项目类型：{old_value} → {new_value}")
                    elif key == 'status':
                        changes.append(f"项目状态：{old_value} → {new_value}")
                    elif key == 'tags':
                        changes.append(f"项目标签已更新")
                    elif key == 'folder_path':
                        if folder_migrated:
                            changes.append(f"项目文件夹已迁移：{new_value}")
                        elif not folder_renamed:  # 避免重复记录文件夹变更
                            changes.append(f"项目文件夹路径已更新：{new_value}")
            
            # 更新项目数据（保留创建时间和资源数据）
            original_created_time = self.project.get('created_time')
            original_resources = self.project.get('resources', [])
            original_id = self.project.get('id')
            
            for key, value in updated_data.items():
                self.project[key] = value
            
            # 确保重要字段不被覆盖
            if original_created_time:
                self.project['created_time'] = original_created_time
            if original_resources:
                self.project['resources'] = original_resources
            if original_id:
                self.project['id'] = original_id
                
            # 更新修改时间
            self.project['modified_time'] = datetime.now().isoformat()
            
            # 同步更新parent_tool中的项目数据
            if self.parent_tool:
                for i, project in enumerate(self.parent_tool.projects):
                    if project.get('id') == self.project.get('id') or project.get('name') == self.project.get('name'):
                        self.parent_tool.projects[i] = self.project
                        break
            
            # 记录项目日志
            if changes:
                change_details = "；".join(changes)
                self.parent_tool.add_project_log(self.project['name'], "编辑项目", 
                                               f"项目信息已更新：{change_details}", 
                                               "操作")
            
            # 保存数据并刷新界面
            self.parent_tool.save_data(create_backup=True)  # 编辑项目时创建备份
            self.parent_tool.refresh_project_list()
            
            # 重新从markdown文件加载数据以确保同步
            self.load_from_markdown_file()
            
            # 重新获取最近打开的资源信息（项目名称可能已改变）
            new_recently_opened = self.get_recently_opened_resource()
            # 确保recently_opened_resource要么是有效的资源名称，要么是None
            self.recently_opened_resource = new_recently_opened if new_recently_opened else None
            
            # 更新当前对话框标题和内容
            self.setWindowTitle(f"项目详情 - {self.project['name']}")
            
            # 刷新项目信息卡片
            self.refresh_info_card()
            
            # 重新加载资源列表以反映最新的项目状态
            if hasattr(self, 'load_resources'):
                self.load_resources()
            
            # 在状态栏显示成功信息
            if folder_migrated:
                self.status_bar.showMessage("✅ 项目信息已更新，文件夹已迁移！", 3000)
            else:
                self.status_bar.showMessage("✅ 项目信息已更新！", 3000)
            
    def refresh_info_card(self):
        """刷新项目信息卡片"""
        # 移除旧的信息卡片和stretch
        for i in reversed(range(self.left_layout.count())):
            item = self.left_layout.itemAt(i)
            if item.widget():
                item.widget().deleteLater()
            elif item.spacerItem():
                self.left_layout.removeItem(item)
        
        # 创建新的信息卡片
        info_card = self.create_info_card()
        self.left_layout.addWidget(info_card)
        self.left_layout.addStretch()
        
    def init_ui(self):
        """初始化界面"""
        self.setWindowTitle(f"项目详情 - {self.project['name']}")
        self.setMinimumSize(800, 600)
        width, height = get_optimal_window_size()
        self.resize(width, height)
        center_window(self)
        
        # 设置窗口标志，允许最小化和关闭
        from PyQt5.QtCore import Qt
        self.setWindowFlags(Qt.Window | Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint)
        
        # 设置对话框样式
        c = DesignSystem.COLORS
        self.setStyleSheet(f"""
            QDialog {{
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 {c['background']}, stop:1 {c['surface_hover']});
            }}
        """)
        
        # 主布局
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(24, 24, 24, 0)
        main_layout.setSpacing(20)
        
        # 标题区域
        title_layout = QHBoxLayout()
        title_icon = QLabel("📋")
        title_icon.setStyleSheet("font-size: 24px;")
        title_label = QLabel("项目详情")
        c = DesignSystem.COLORS
        title_label.setStyleSheet(f"""
            QLabel {{
                font-size: 20px;
                font-weight: bold;
                color: {c['primary']};
                margin-left: 8px;
            }}
        """)
        title_layout.addWidget(title_icon)
        title_layout.addWidget(title_label)
        title_layout.addStretch()
        
        # 返回项目列表按钮
        close_btn = QPushButton("返回项目列表")
        c = DesignSystem.COLORS
        close_btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {c['text_secondary']};
                color: white;
                border: none;
                border-radius: {DesignSystem.RADIUS['md']}px;
                padding: 8px 16px;
                font-size: {DesignSystem.FONT_SIZES['lg']}px;
                font-weight: 500;
            }}
            QPushButton:hover {{
                background-color: {c['text_primary']};
            }}
        """)
        close_btn.clicked.connect(self.close)
        title_layout.addWidget(close_btn)
        
        main_layout.addLayout(title_layout)
        
        # 内容区域 - 使用左右布局
        content_layout = QHBoxLayout()
        content_layout.setSpacing(20)
        
        # 左侧：项目信息卡片
        left_widget = QWidget()
        self.left_layout = QVBoxLayout(left_widget)
        self.left_layout.setContentsMargins(0, 0, 0, 0)
        info_card = self.create_info_card()
        self.left_layout.addWidget(info_card)
        self.left_layout.addStretch()  # 添加弹性空间
        left_widget.setFixedWidth(350)  # 固定左侧宽度
        content_layout.addWidget(left_widget)
        
        # 右侧：选项卡布局（资源管理、项目笔记和项目清单）
        right_widget = QTabWidget()
        c = DesignSystem.COLORS
        right_widget.setStyleSheet(f"""
            QTabWidget::pane {{
                border: 1px solid {c['border']};
                border-radius: {DesignSystem.RADIUS['md']}px;
                background-color: {c['surface']};
            }}
            QTabBar::tab {{
                background-color: {c['background']};
                border: 1px solid {c['border']};
                border-bottom: none;
                border-radius: 6px 6px 0 0;
                padding: 10px 30px;
                margin-right: 4px;
                font-weight: 500;
                min-width: 120px;
            }}
            QTabBar::tab:selected {{
                background-color: {c['surface']};
                color: {c['primary']};
                border-bottom: 2px solid {c['primary']};
            }}
            QTabBar::tab:hover {{
                background-color: {c['surface_hover']};
            }}
        """)
        
        # 计算各个tab的数量
        resource_count = len(self.project.get('resources', []))
        notes_count = len(self.project.get('notes_timeline', []))
        checklist_count = len(self.project.get('checklist_items', []))
        
        # 从markdown文件计算日志数量
        logs_count = 0
        try:
            folder_path = self.project.get('folder_path', '')
            if folder_path and os.path.exists(folder_path):
                project_name = self.project['name']
                safe_name = "".join(c for c in project_name if c.isalnum() or c in (' ', '-', '_', '（', '）', '(', ')')).strip()
                if not safe_name:
                    safe_name = "新项目"
                notes_file = os.path.join(folder_path, f"{safe_name}_笔记.md")
                if os.path.exists(notes_file):
                    with open(notes_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                    logs = self.parent_tool.parse_project_logs_from_markdown(content)
                    logs_count = len(logs)
        except:
            logs_count = 0
        
        # 资源管理选项卡
        resource_widget = QWidget()
        resource_layout = QVBoxLayout(resource_widget)
        resource_layout.setContentsMargins(16, 16, 16, 16)
        resource_card = self.create_resource_card()
        resource_layout.addWidget(resource_card)
        right_widget.addTab(resource_widget, f"📁 项目资源 ({resource_count})")
        
        # 项目笔记选项卡
        notes_widget = QWidget()
        notes_layout = QVBoxLayout(notes_widget)
        notes_layout.setContentsMargins(16, 16, 16, 16)
        notes_card = self.create_notes_card()
        notes_layout.addWidget(notes_card)
        right_widget.addTab(notes_widget, f"📝 项目笔记 ({notes_count})")
        
        # 项目清单选项卡
        checklist_widget = QWidget()
        checklist_layout = QVBoxLayout(checklist_widget)
        checklist_layout.setContentsMargins(16, 16, 16, 16)
        checklist_card = self.create_checklist_card()
        checklist_layout.addWidget(checklist_card)
        right_widget.addTab(checklist_widget, f"📋 项目清单 ({checklist_count})")
        
        # IA资源选项卡
        ia_resource_widget = QWidget()
        ia_resource_layout = QVBoxLayout(ia_resource_widget)
        ia_resource_layout.setContentsMargins(16, 16, 16, 16)
        ia_resource_layout.setSpacing(16)
        
        # 创建IA资源卡片
        ia_card = self.create_ia_resource_card()
        ia_resource_layout.addWidget(ia_card)
        
        # 计算IA资源数量
        ia_resources_count = len(self.project.get('ia_resources', []))
        # right_widget.addTab(ia_resource_widget, f"🤖 IA资源 ({ia_resources_count})")
        
        # 项目日志选项卡
        logs_widget = QWidget()
        logs_layout = QVBoxLayout(logs_widget)
        logs_layout.setContentsMargins(16, 16, 16, 16)
        logs_card = self.create_logs_card()
        logs_layout.addWidget(logs_card)
        right_widget.addTab(logs_widget, f"📊 项目日志 ({logs_count})")
        
        content_layout.addWidget(right_widget)
        
        main_layout.addLayout(content_layout)
        
        # 底部状态栏布局（无左右边距，确保状态栏铺满整个宽度）
        bottom_layout = QVBoxLayout()
        bottom_layout.setContentsMargins(0, 0, 0, 0)
        bottom_layout.setSpacing(0)
        
        # 底部状态栏
        self.status_bar = QStatusBar()
        self.status_bar.setStyleSheet(DesignSystem.status_bar_style())
        self.status_bar.showMessage("拖动文件到本界面即可添加资源")
        
        # 设置状态栏大小策略，确保能够铺满整个宽度
        self.status_bar.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        
        # 添加版本标签到右侧永久区域
        version_label = QLabel(f"v{self.parent_tool.TOOL_INFO['version']}")
        version_label.setStyleSheet(f"color: {DesignSystem.COLORS['text_secondary']}; margin-right: 12px;")
        self.status_bar.addPermanentWidget(version_label)
        
        bottom_layout.addWidget(self.status_bar)
        main_layout.addLayout(bottom_layout)
        
        # 保存tab widget的引用以便后续更新
        self.tab_widget = right_widget
        
        # 绑定选项卡切换事件
        right_widget.currentChanged.connect(self.on_tab_changed)
        
        # 初始化时更新tab标题中的数量显示
        self.update_tab_counts()
    
    def on_tab_changed(self, index):
        """处理选项卡切换事件"""
        # 检查是否切换到日志选项卡（索引为3）
        if index == 3:  # 项目日志选项卡的索引
            # 自动刷新日志数据
            self.load_project_logs()
    
    def create_logs_card(self):
        """创建项目日志卡片"""
        card = QWidget()
        c = DesignSystem.COLORS
        card.setStyleSheet(f"""
            QWidget {{
                background-color: {c['surface']};
                border-radius: {DesignSystem.RADIUS['lg']}px;
                border: 1px solid {c['border']};
            }}
        """)
        
        layout = QVBoxLayout(card)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(16)
        
        # 标题和操作按钮
        header_layout = QHBoxLayout()
        
        # 标题
        title_layout = QHBoxLayout()
        title_icon = QLabel("📊")
        title_icon.setStyleSheet("font-size: 18px;")
        title_label = QLabel("项目日志")
        title_label.setStyleSheet("""
            QLabel {
                font-size: 16px;
                font-weight: bold;
                color: #333;
                margin-left: 8px;
            }
        """)
        title_layout.addWidget(title_icon)
        title_layout.addWidget(title_label)
        title_layout.addStretch()
        
        header_layout.addLayout(title_layout)
        
        # 刷新按钮
        refresh_btn = QPushButton("🔄 刷新")
        c = DesignSystem.COLORS
        refresh_btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {c['success']};
                color: white;
                border: none;
                border-radius: {DesignSystem.RADIUS['md']}px;
                padding: 8px 16px;
                font-size: {DesignSystem.FONT_SIZES['md']}px;
                font-weight: 500;
            }}
            QPushButton:hover {{
                background-color: {c['success_hover']};
            }}
        """)
        refresh_btn.clicked.connect(self.load_project_logs)
        header_layout.addWidget(refresh_btn)
        
        layout.addLayout(header_layout)
        
        # 日志类型筛选
        filter_layout = QHBoxLayout()
        filter_label = QLabel("筛选类型：")
        filter_label.setStyleSheet("font-weight: 500; color: #666;")
        
        self.logs_filter_combo = QComboBox()
        self.logs_filter_combo.addItems(["全部", "操作", "资源", "文件", "状态", "笔记", "清单"])
        c = DesignSystem.COLORS
        self.logs_filter_combo.setStyleSheet(f"""
            QComboBox {{
                border: 1px solid {c['border']};
                border-radius: {DesignSystem.RADIUS['sm']}px;
                padding: 6px 12px;
                background-color: {c['surface']};
                min-width: 100px;
            }}
            QComboBox:focus {{
                border-color: {c['primary']};
            }}
        """)
        self.logs_filter_combo.currentTextChanged.connect(self.filter_logs)
        
        filter_layout.addWidget(filter_label)
        filter_layout.addWidget(self.logs_filter_combo)
        filter_layout.addStretch()
        
        layout.addLayout(filter_layout)
        
        # 日志列表
        self.logs_list = QListWidget()
        c = DesignSystem.COLORS
        self.logs_list.setStyleSheet(f"""
            QListWidget {{
                border: 1px solid {c['border']};
                border-radius: {DesignSystem.RADIUS['md']}px;
                background-color: {c['surface_hover']};
                alternate-background-color: {c['background']};
            }}
            QListWidget::item {{
                padding: 12px;
                border-bottom: 1px solid {c['border']};
                background-color: {c['surface']};
                margin: 2px;
                border-radius: {DesignSystem.RADIUS['md']}px;
            }}
            QListWidget::item:hover {{
                background-color: {c['primary_light']};
            }}
            QListWidget::item:selected {{
                background-color: {c['primary_light']};
                color: {c['primary']};
            }}
        """)
        
        layout.addWidget(self.logs_list)
        
        # 加载日志数据
        self.load_project_logs()
        
        return card
    
    def load_project_logs(self):
        """从markdown文件加载项目日志"""
        self.logs_list.clear()
        
        try:
            folder_path = self.project.get('folder_path', '')
            if not folder_path or not os.path.exists(folder_path):
                item = QListWidgetItem("项目文件夹不存在")
                item.setTextAlignment(Qt.AlignCenter)
                self.logs_list.addItem(item)
                return
            
            project_name = self.project['name']
            safe_name = "".join(c for c in project_name if c.isalnum() or c in (' ', '-', '_', '（', '）', '(', ')')).strip()
            if not safe_name:
                safe_name = "新项目"
            
            notes_file = os.path.join(folder_path, f"{safe_name}_笔记.md")
            
            if not os.path.exists(notes_file):
                item = QListWidgetItem("暂无项目日志")
                item.setTextAlignment(Qt.AlignCenter)
                self.logs_list.addItem(item)
                return
            
            # 读取markdown文件
            with open(notes_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 解析项目日志部分
            logs = self.parent_tool.parse_project_logs_from_markdown(content)
            
            if not logs:
                item = QListWidgetItem("暂无项目日志")
                item.setTextAlignment(Qt.AlignCenter)
                self.logs_list.addItem(item)
                return
            
            # 按时间排序（最新的在前）
            sorted_logs = sorted(logs, key=lambda x: x.get('timestamp', ''), reverse=True)
            
            for log in sorted_logs:
                self.add_log_to_list(log)
                
        except Exception as e:
            item = QListWidgetItem(f"加载日志失败: {str(e)}")
            item.setTextAlignment(Qt.AlignCenter)
            self.logs_list.addItem(item)
    
    def add_log_to_list(self, log):
        """添加日志到列表"""
        timestamp = log.get('timestamp', '')
        action = log.get('action', '')
        details = log.get('details', '')
        log_type = log.get('type', '操作')
        
        # 格式化时间
        try:
            dt = datetime.fromisoformat(timestamp)
            time_str = dt.strftime('%Y-%m-%d %H:%M:%S')
        except:
            time_str = timestamp
        
        # 根据日志类型设置图标
        type_icons = {
            '操作': '⚙️',
            '资源': '📁',
            '文件': '📄',
            '状态': '🔄',
            '笔记': '📝',
            '清单': '📋'
        }
        icon = type_icons.get(log_type, '📌')
        
        # 创建显示文本
        display_text = f"{icon} [{log_type}] {action}\n{time_str}"
        if details:
            display_text += f"\n{details}"
        
        item = QListWidgetItem(display_text)
        item.setData(Qt.UserRole, log)
        
        # 根据日志类型设置颜色
        c = DesignSystem.COLORS
        type_colors = {
            '操作': c['primary'],
            '资源': c['success'],
            '文件': c['warning'],
            '状态': c['info'],
            '笔记': c['text_secondary'],
            '清单': c['text_primary']
        }
        color = type_colors.get(log_type, c['text_secondary'])
        
        font = item.font()
        font.setPointSize(11)
        item.setFont(font)
        
        self.logs_list.addItem(item)
    
    def filter_logs(self):
        """筛选日志"""
        filter_type = self.logs_filter_combo.currentText()
        
        for i in range(self.logs_list.count()):
            item = self.logs_list.item(i)
            log_data = item.data(Qt.UserRole)
            
            if not log_data:  # 空状态项
                continue
                
            if filter_type == "全部":
                item.setHidden(False)
            else:
                log_type = log_data.get('type', '操作')
                item.setHidden(log_type != filter_type)
        
        # 初始化时更新tab标题中的数量
        self.update_tab_counts()
        
    def update_tab_counts(self):
        """更新tab标题中的数量显示"""
        if hasattr(self, 'tab_widget'):
            resource_count = len(self.project.get('resources', []))
            notes_count = len(self.project.get('notes_timeline', []))
            checklist_count = len(self.project.get('checklist_items', []))
            
            # 计算IA资源数量
            ia_resources_count = len(self.project.get('ia_resources', []))
            
            # 计算日志数量
            logs_count = 0
            try:
                folder_path = self.project.get('folder_path', '')
                if folder_path and os.path.exists(folder_path):
                    project_name = self.project['name']
                    safe_name = "".join(c for c in project_name if c.isalnum() or c in (' ', '-', '_', '（', '）', '(', ')')).strip()
                    if not safe_name:
                        safe_name = "新项目"
                    notes_file = os.path.join(folder_path, f"{safe_name}_笔记.md")
                    if os.path.exists(notes_file):
                        with open(notes_file, 'r', encoding='utf-8') as f:
                            content = f.read()
                        logs = self.parent_tool.parse_project_logs_from_markdown(content)
                        logs_count = len(logs)
            except:
                logs_count = 0
            self.tab_widget.setTabText(0, f"📁 项目资源 ({resource_count})")
            self.tab_widget.setTabText(1, f"📝 项目笔记 ({notes_count})")
            self.tab_widget.setTabText(2, f"📋 项目清单 ({checklist_count})")
            # self.tab_widget.setTabText(3, f"🤖 IA资源 ({ia_resources_count})")
            self.tab_widget.setTabText(4, f"📊 项目日志 ({logs_count})")
        
    def on_auto_scan_switch_changed(self, state):
        """处理自动扫描开关状态变化"""
        is_checked = state == Qt.Checked
        
        # 更新项目数据
        self.project['auto_scan_resources'] = is_checked
        
        # 保存项目数据
        self.save_project_data()
        
        # 显示提示信息
        if is_checked:
            self.show_toast("已启用自动扫描资源功能，程序启动时将自动扫描项目文件夹", "success")
        else:
            self.show_toast("已禁用自动扫描资源功能", "info")
    
    def scan_project_folder_now(self):
        """立即扫描项目文件夹并添加新资源"""
        if not self.project.get('folder_path'):
            self.show_toast("项目未设置文件夹路径，无法扫描", "error")
            return
            
        # 获取项目文件夹路径
        folder_path = self.project['folder_path']
        
        if not os.path.exists(folder_path):
            self.show_toast("项目文件夹不存在，无法扫描", "error")
            return
            
        # 显示扫描中提示
        self.show_toast("正在扫描项目文件夹，请稍候...", "info")
        
        # 获取当前资源列表
        existing_resources = self.project.get('resources', [])
        existing_paths = {res.get('path', '') for res in existing_resources if res.get('path')}
        
        # 扫描文件夹
        new_resources = []
        scanned_count = 0
        
        try:
            for root, dirs, files in os.walk(folder_path):
                # 跳过隐藏目录
                dirs[:] = [d for d in dirs if not d.startswith('.')]
                
                for file in files:
                    # 跳过隐藏文件
                    if file.startswith('.'):
                        continue
                        
                    file_path = os.path.join(root, file)
                    relative_path = os.path.relpath(file_path, folder_path)
                    
                    # 检查是否已存在
                    if file_path not in existing_paths and relative_path not in existing_paths:
                        # 获取文件信息
                        try:
                            stat_info = os.stat(file_path)
                            file_size = stat_info.st_size
                            modified_time = datetime.fromtimestamp(stat_info.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
                            
                            # 确定文件类型
                            file_ext = os.path.splitext(file)[1].lower()
                            file_type = self.get_file_type_by_extension(file_ext)
                            
                            # 创建新资源
                            new_resource = {
                                'name': file,
                                'path': file_path,
                                'relative_path': relative_path,
                                'type': file_type,
                                'size': file_size,
                                'modified_time': modified_time,
                                'added_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                'tags': []
                            }
                            
                            new_resources.append(new_resource)
                            scanned_count += 1
                        except Exception as e:
                            print(f"处理文件时出错: {file_path}, 错误: {str(e)}")
                            
        except Exception as e:
            self.show_toast(f"扫描项目文件夹时出错: {str(e)}", "error")
            return
            
        # 添加新资源到项目
        if new_resources:
            # 合并新资源到现有资源列表
            self.project['resources'] = existing_resources + new_resources
            
            # 更新资源计数
            self.project['resource_count'] = len(self.project['resources'])
            
            # 同步更新parent_tool.projects中的对应项目
            project_id = self.project.get('id', '')
            if project_id:
                for i, p in enumerate(self.parent_tool.projects):
                    if p.get('id') == project_id:
                        self.parent_tool.projects[i] = self.project.copy()
                        break
            
            # 保存项目数据
            self.save_project_data()
            
            # 刷新资源管理选项卡
            self.refresh_resource_tab()
            
            # 刷新项目列表以更新资源计数
            self.parent_tool.refresh_project_list()
            
            # 显示成功消息
            self.show_toast(f"扫描完成，发现并添加了 {scanned_count} 个新资源", "success")
            
            # 添加项目日志
            self.parent_tool.add_project_log(self.project['name'], "自动扫描项目文件夹", 
                                           f"添加了 {scanned_count} 个新资源", "资源")
        else:
            self.show_toast("扫描完成，未发现新资源", "info")
    
    def get_file_type_by_extension(self, extension):
        """根据文件扩展名获取文件类型"""
        # 文档类型
        if extension in ['.txt', '.md', '.doc', '.docx', '.pdf', '.rtf']:
            return '文档'
        # 图片类型
        elif extension in ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp']:
            return '图片'
        # 视频类型
        elif extension in ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv']:
            return '视频'
        # 音频类型
        elif extension in ['.mp3', '.wav', '.flac', '.aac', '.ogg']:
            return '音频'
        # 代码类型
        elif extension in ['.py', '.js', '.html', '.css', '.java', '.cpp', '.c', '.php']:
            return '代码'
        # 压缩包类型
        elif extension in ['.zip', '.rar', '.7z', '.tar', '.gz']:
            return '压缩包'
        # 表格类型
        elif extension in ['.xls', '.xlsx', '.csv']:
            return '表格'
        # 演示文稿类型
        elif extension in ['.ppt', '.pptx']:
            return '演示文稿'
        # 其他类型
        else:
            return '其他'
    
    def save_project_data(self):
        """保存项目数据"""
        try:
            # 更新资源计数
            self.project['resource_count'] = len(self.project.get('resources', []))
            
            # 使用新的同步并保存方法
            self.sync_and_save_project(create_backup=False)
                    
        except Exception as e:
            print(f"保存项目数据时出错: {str(e)}")
            self.show_toast(f"保存项目数据失败: {str(e)}", "error")
    
    def refresh_resource_tab(self):
        """刷新资源管理选项卡"""
        try:
            # 如果资源管理选项卡存在，则刷新其内容
            if hasattr(self, 'resource_tree'):
                # 清空现有树形视图
                self.resource_tree.clear()
                
                # 重新加载资源
                self.load_resources()
                
                # 更新选项卡标题中的资源数量
                resource_count = len(self.project.get('resources', []))
                self.tab_widget.setTabText(0, f"资源管理 ({resource_count})")
                
        except Exception as e:
            print(f"刷新资源选项卡时出错: {str(e)}")
    
    def show_toast(self, message, msg_type="info"):
        """显示Toast提示消息"""
        try:
            # 在状态栏显示消息
            if hasattr(self, 'parent') and hasattr(self.parent, 'status_bar'):
                self.parent.status_bar.showMessage(message, 5000)  # 显示5秒
            else:
                print(message)  # 如果没有状态栏，则打印到控制台
        except Exception as e:
            print(f"显示提示消息时出错: {str(e)}")
            print(message)  # 出错时打印到控制台

    def create_info_card(self):
        """创建项目信息卡片"""
        card = ModernCard("项目信息")
        
        # 在标题旁边添加编辑项目按钮
        title_layout = QHBoxLayout()
        title_layout.addWidget(card.title_label)
        title_layout.addStretch()
        
        # 编辑项目按钮
        edit_btn = QPushButton("✏️ 编辑项目")
        c = DesignSystem.COLORS
        edit_btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {c['primary']};
                color: white;
                border: none;
                border-radius: {DesignSystem.RADIUS['md']}px;
                padding: 6px 12px;
                font-size: 13px;
                font-weight: 500;
            }}
            QPushButton:hover {{
                background-color: {c['primary_hover']};
            }}
            QPushButton:pressed {{
                background-color: {c['primary_pressed']};
            }}
        """)
        edit_btn.clicked.connect(self.edit_project)
        title_layout.addWidget(edit_btn)
        
        # 将标题布局插入到卡片的第一个位置
        card.layout.insertLayout(0, title_layout)
        
        # 项目名称
        name_layout = QHBoxLayout()
        name_icon = QLabel("📝")
        name_icon.setFixedSize(24, 24)
        name_layout.addWidget(name_icon)
        name_layout.addWidget(QLabel("项目名称:"))
        name_label = QLabel(self.project['name'])
        c = DesignSystem.COLORS
        name_label.setStyleSheet(f"""
            QLabel {{
                font-weight: 600;
                font-size: 16px;
                color: {c['primary']};
                padding: 4px 8px;
                background-color: {c['primary_light']};
                border-radius: {DesignSystem.RADIUS['sm']}px;
            }}
        """)
        name_layout.addWidget(name_label)
        name_layout.addStretch()
        card.addLayout(name_layout)
        
        # 项目描述
        desc_layout = QHBoxLayout()
        desc_icon = QLabel("📄")
        desc_icon.setFixedSize(24, 24)
        desc_layout.addWidget(desc_icon)
        desc_layout.addWidget(QLabel("描述:"))
        desc_label = QLabel(self.project.get('description', '无描述'))
        c = DesignSystem.COLORS
        desc_label.setStyleSheet(f"color: {c['text_secondary']}; font-style: italic;")
        desc_label.setWordWrap(True)
        desc_layout.addWidget(desc_label)
        desc_layout.addStretch()
        card.addLayout(desc_layout)
        
        # 项目类型
        type_layout = QHBoxLayout()
        type_icon = QLabel("🏷️")
        type_icon.setFixedSize(24, 24)
        type_layout.addWidget(type_icon)
        type_layout.addWidget(QLabel("类型:"))
        type_label = QLabel(self.project.get('type', '未分类'))
        c = DesignSystem.COLORS
        type_label.setStyleSheet(f"""
            QLabel {{
                color: {c['warning']};
                background-color: {c['warning_light']};
                padding: 2px 8px;
                border-radius: 12px;
                font-size: 12px;
            }}
        """)
        type_layout.addWidget(type_label)
        type_layout.addStretch()
        card.addLayout(type_layout)
        
        # 项目标签
        tags_layout = QHBoxLayout()
        tags_icon = QLabel("🏷️")
        tags_icon.setFixedSize(24, 24)
        tags_layout.addWidget(tags_icon)
        tags_layout.addWidget(QLabel("标签:"))
        
        tags = self.project.get('tags', '无标签')
        if isinstance(tags, list):
            tags_text = ', '.join(tags) if tags else '无标签'
        else:
            tags_text = str(tags) if tags else '无标签'
        
        tags_label = QLabel(tags_text)
        c = DesignSystem.COLORS
        tags_label.setStyleSheet(f"""
            QLabel {{
                color: {c['success']};
                background-color: {c['success_light']};
                padding: 2px 8px;
                border-radius: 12px;
                font-size: 12px;
            }}
        """)
        tags_layout.addWidget(tags_label)
        tags_layout.addStretch()
        card.addLayout(tags_layout)
        
        # 时间信息
        time_layout = QVBoxLayout()
        time_icon_layout = QHBoxLayout()
        time_icon = QLabel("⏰")
        time_icon.setFixedSize(24, 24)
        time_icon_layout.addWidget(time_icon)
        time_icon_layout.addWidget(QLabel("时间信息:"))
        time_icon_layout.addStretch()
        time_layout.addLayout(time_icon_layout)
        
        # 创建时间
        created_time = self.project.get('created_time', '')
        if created_time:
            try:
                # 处理浮点数时间戳
                if isinstance(created_time, (int, float)):
                    created_dt = datetime.fromtimestamp(created_time)
                else:
                    # 处理字符串格式的时间
                    created_dt = datetime.fromisoformat(str(created_time))
                created_str = created_dt.strftime('%Y-%m-%d %H:%M:%S')
            except:
                created_str = str(created_time)
        else:
            created_str = '未知'
        
        created_layout = QHBoxLayout()
        created_layout.addWidget(QLabel("  创建时间:"))
        created_label = QLabel(created_str)
        created_label.setStyleSheet("color: #666666; font-size: 12px;")
        created_layout.addWidget(created_label)
        created_layout.addStretch()
        time_layout.addLayout(created_layout)
        
        # 修改时间
        modified_time = self.project.get('modified_time', '')
        if modified_time:
            try:
                # 处理浮点数时间戳
                if isinstance(modified_time, (int, float)):
                    modified_dt = datetime.fromtimestamp(modified_time)
                else:
                    # 处理字符串格式的时间
                    modified_dt = datetime.fromisoformat(str(modified_time))
                modified_str = modified_dt.strftime('%Y-%m-%d %H:%M:%S')
            except:
                modified_str = str(modified_time)
        else:
            modified_str = '未知'
        
        modified_layout = QHBoxLayout()
        modified_layout.addWidget(QLabel("  修改时间:"))
        modified_label = QLabel(modified_str)
        modified_label.setStyleSheet("color: #666666; font-size: 12px;")
        modified_layout.addWidget(modified_label)
        modified_layout.addStretch()
        time_layout.addLayout(modified_layout)
        
        card.addLayout(time_layout)
        
        # 项目文件夹路径 - 使用垂直布局以便更好地显示长路径
        folder_main_layout = QVBoxLayout()
        
        # 标题行
        folder_title_layout = QHBoxLayout()
        folder_icon = QLabel("📁")
        folder_icon.setFixedSize(24, 24)
        folder_title_layout.addWidget(folder_icon)
        folder_title_layout.addWidget(QLabel("项目文件夹:"))
        
        # 添加编辑按钮到标题行
        edit_path_btn = QPushButton("编辑")
        edit_path_btn.setFixedSize(50, 24)
        edit_path_btn.setStyleSheet("""
            QPushButton {
                background-color: #f0f0f0;
                border: 1px solid #d0d0d0;
                border-radius: 4px;
                color: #666666;
                font-size: 11px;
                font-weight: 500;
            }
            QPushButton:hover {
                background-color: #e0e0e0;
                border-color: #b0b0b0;
                color: #333333;
            }
            QPushButton:pressed {
                background-color: #d0d0d0;
            }
        """)
        edit_path_btn.clicked.connect(self.edit_project_path)
        edit_path_btn.setToolTip("修改项目文件夹路径")
        folder_title_layout.addWidget(edit_path_btn)
        folder_title_layout.addStretch()
        folder_main_layout.addLayout(folder_title_layout)
        
        # 路径内容行 - 使用缩进增强可读性
        folder_path_layout = QHBoxLayout()
        folder_path_layout.addSpacing(30)  # 添加缩进
        
        folder_path = self.project.get('folder_path', '')
        if folder_path and os.path.exists(folder_path):
            # 规范化路径显示，统一使用系统默认的路径分隔符
            normalized_path = os.path.normpath(folder_path)
            folder_label = QLabel(normalized_path)
            folder_label.setStyleSheet("""
                QLabel {
                    color: #2196F3;
                    text-decoration: underline;
                    cursor: pointer;
                    padding: 2px 4px;
                    border-radius: 4px;
                    font-weight: 500;
                }
                QLabel:hover {
                    background-color: #e3f2fd;
                    color: #1976D2;
                }
            """)
            folder_label.setWordWrap(True)  # 添加自动换行
            folder_label.mousePressEvent = lambda event: self.open_folder(folder_path)
            folder_label.setToolTip(f"点击打开文件夹: {normalized_path}")
        else:
            folder_label = QLabel("没有设置项目文件夹")
            folder_label.setStyleSheet("color: #999999; font-style: italic;")
        
        folder_path_layout.addWidget(folder_label)
        folder_path_layout.addStretch()
        folder_main_layout.addLayout(folder_path_layout)
        
        card.addLayout(folder_main_layout)
        
        # 自动扫描资源设置
        scan_main_layout = QVBoxLayout()
        
        # 标题行
        scan_title_layout = QHBoxLayout()
        scan_icon = QLabel("🔄")
        scan_icon.setFixedSize(24, 24)
        scan_title_layout.addWidget(scan_icon)
        scan_title_layout.addWidget(QLabel("自动扫描资源:"))
        
        # 添加"立即扫描"按钮到标题行
        scan_now_btn = QPushButton("立即扫描")
        scan_now_btn.setFixedSize(70, 24)
        scan_now_btn.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                border: none;
                border-radius: 4px;
                color: white;
                font-size: 11px;
                font-weight: 500;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:pressed {
                background-color: #3d8b40;
            }
        """)
        scan_now_btn.clicked.connect(self.scan_project_folder_now)
        scan_now_btn.setToolTip("立即扫描项目文件夹并添加新资源")
        scan_title_layout.addWidget(scan_now_btn)
        scan_title_layout.addStretch()
        scan_main_layout.addLayout(scan_title_layout)
        
        # 开关内容行 - 使用缩进增强可读性
        scan_path_layout = QHBoxLayout()
        scan_path_layout.addSpacing(30)  # 添加缩进
        
        # 创建开关控件
        self.auto_scan_switch = QCheckBox()
        self.auto_scan_switch.setText("启动时自动扫描项目文件夹并添加新资源")
        self.auto_scan_switch.setStyleSheet("""
            QCheckBox {
                font-size: 13px;
                color: #333333;
                spacing: 8px;
            }
            QCheckBox::indicator {
                width: 18px;
                height: 18px;
                border-radius: 9px;
                border: 2px solid #cccccc;
                background-color: white;
            }
            QCheckBox::indicator:hover {
                border: 2px solid #2196F3;
            }
            QCheckBox::indicator:checked {
                background-color: #2196F3;
                border: 2px solid #2196F3;
                image: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQiIGhlaWdodD0iMTQiIHZpZXdCb3g9IjAgMCAxNCAxNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTEyIDQgNSAxMSAyIDgiIHN0cm9rZT0id2hpdGUiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIi8+Cjwvc3ZnPgo=);
            }
        """)
        
        # 设置开关状态 - 从项目数据中获取
        auto_scan_enabled = self.project.get('auto_scan_resources', False)
        self.auto_scan_switch.setChecked(auto_scan_enabled)
        
        # 连接开关状态变化事件
        self.auto_scan_switch.stateChanged.connect(self.on_auto_scan_switch_changed)
        
        scan_path_layout.addWidget(self.auto_scan_switch)
        scan_path_layout.addStretch()
        scan_main_layout.addLayout(scan_path_layout)
        
        card.addLayout(scan_main_layout)
        
        return card
    
    def create_notes_card(self):
        """创建项目笔记卡片"""
        card = ModernCard("项目笔记")
        
        # 笔记操作按钮
        btn_layout = QHBoxLayout()
        add_note_btn = ModernButton("+ 添加笔记", "primary")
        add_note_btn.clicked.connect(self.add_new_note)
        import_notes_btn = ModernButton("📥 导入笔记文件", "primary")
        import_notes_btn.clicked.connect(self.import_notes_file)
        open_btn = ModernButton("📂 打开笔记文件", "secondary")
        open_btn.clicked.connect(self.open_notes_file)
        refresh_btn = ModernButton("🔄 刷新", "secondary")
        refresh_btn.clicked.connect(self.load_notes_timeline)
        
        btn_layout.addWidget(add_note_btn)
        btn_layout.addWidget(import_notes_btn)
        btn_layout.addWidget(open_btn)
        btn_layout.addWidget(refresh_btn)
        btn_layout.addStretch()
        card.addLayout(btn_layout)
        
        # 搜索框
        search_layout = QHBoxLayout()
        search_label = QLabel("🔍 搜索笔记:")
        search_label.setStyleSheet("""
            QLabel {
                font-size: 14px;
                font-weight: 600;
                color: #333333;
                margin-right: 8px;
            }
        """)
        
        self.notes_search_input = QLineEdit()
        self.notes_search_input.setPlaceholderText("输入关键词搜索笔记标题或内容...")
        self.notes_search_input.setStyleSheet("""
            QLineEdit {
                border: 2px solid #e0e0e0;
                border-radius: 6px;
                padding: 8px 12px;
                font-size: 14px;
                background-color: white;
            }
            QLineEdit:focus {
                border-color: #2196F3;
                outline: none;
            }
        """)
        self.notes_search_input.textChanged.connect(self.filter_notes)
        
        clear_search_btn = QPushButton("✕")
        clear_search_btn.setFixedSize(32, 32)
        clear_search_btn.setStyleSheet("""
            QPushButton {
                background-color: #f5f5f5;
                border: 1px solid #e0e0e0;
                border-radius: 6px;
                color: #666666;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #e0e0e0;
                color: #333333;
            }
        """)
        clear_search_btn.setToolTip("清除搜索")
        clear_search_btn.clicked.connect(self.clear_notes_search)
        
        search_layout.addWidget(search_label)
        search_layout.addWidget(self.notes_search_input, 1)
        search_layout.addWidget(clear_search_btn)
        card.addLayout(search_layout)
        
        # 笔记时间轴列表
        notes_label = QLabel("📝 笔记时间轴 (拖拽 .txt/.md/.markdown 文件到笔记区域自动导入):")
        notes_label.setStyleSheet("""
            QLabel {
                font-size: 14px;
                font-weight: 600;
                color: #333333;
                margin-top: 10px;
                margin-bottom: 5px;
            }
        """)
        card.addWidget(notes_label)
        
        # 笔记列表显示区域
        self.notes_list = QListWidget()
        self.notes_list.setMinimumHeight(300)
        self.notes_list.setStyleSheet("""
            QListWidget {
                border: 2px solid #e8e8e8;
                border-radius: 8px;
                background-color: #fafafa;
                padding: 8px;
            }
            QListWidget::item {
                border: 1px solid #ddd;
                padding: 12px;
                margin: 4px 0;
                border-radius: 6px;
                background-color: white;
                /* 允许项目自动换行和扩展 */
                min-height: 50px;
            }
            QListWidget::item:hover {
                background-color: #f0f8ff;
                border-color: #4CAF50;
            }
            QListWidget::item:selected {
                background-color: #e3f2fd;
                border-color: #2196F3;
                color: #333333; /* 确保选中项的文字颜色为黑色 */
            }
        """)
        # 设置自动调整大小
        self.notes_list.setWordWrap(True)
        self.notes_list.setTextElideMode(Qt.ElideNone)
        self.notes_list.itemDoubleClicked.connect(self.edit_note_item)
        
        # 设置右键菜单
        self.notes_list.setContextMenuPolicy(Qt.CustomContextMenu)
        self.notes_list.customContextMenuRequested.connect(self.show_notes_context_menu)
        
        # 启用拖拽功能
        self.notes_list.setAcceptDrops(True)
        self.notes_list.dragEnterEvent = self._notes_drag_enter_event
        self.notes_list.dragMoveEvent = self._notes_drag_move_event
        self.notes_list.dropEvent = self._notes_drop_event
        
        card.addWidget(self.notes_list)
        
        # 初始化笔记数据结构
        if 'notes_timeline' not in self.project:
            self.project['notes_timeline'] = []
        
        # 初始化搜索相关属性
        self.all_notes = []
        
        # 加载笔记内容
        self.load_notes_timeline()
        
        return card
        
    def create_checklist_card(self):
        """创建项目清单卡片"""
        card = ModernCard("项目清单")
        
        # 清单操作按钮
        btn_layout = QHBoxLayout()
        add_checklist_btn = ModernButton("+ 增加清单项", "primary")
        add_checklist_btn.clicked.connect(self.add_checklist_item)
        refresh_btn = ModernButton("🔄 刷新", "secondary")
        refresh_btn.clicked.connect(self.load_checklist_items)
        
        btn_layout.addWidget(add_checklist_btn)
        btn_layout.addWidget(refresh_btn)
        btn_layout.addStretch()
        card.addLayout(btn_layout)
        
        # 搜索框
        search_layout = QHBoxLayout()
        search_label = QLabel("🔍 搜索清单:")
        search_label.setStyleSheet("""
            QLabel {
                font-size: 14px;
                font-weight: 600;
                color: #333333;
                margin-right: 8px;
            }
        """)
        
        self.checklist_search_input = QLineEdit()
        self.checklist_search_input.setPlaceholderText("输入关键词搜索清单项内容...")
        self.checklist_search_input.setStyleSheet("""
            QLineEdit {
                border: 2px solid #e0e0e0;
                border-radius: 6px;
                padding: 8px 12px;
                font-size: 14px;
                background-color: white;
            }
            QLineEdit:focus {
                border-color: #2196F3;
                outline: none;
            }
        """)
        self.checklist_search_input.textChanged.connect(self.filter_checklist)
        
        clear_search_btn = QPushButton("✕")
        clear_search_btn.setFixedSize(32, 32)
        clear_search_btn.setStyleSheet("""
            QPushButton {
                background-color: #f5f5f5;
                border: 1px solid #e0e0e0;
                border-radius: 6px;
                color: #666666;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #e0e0e0;
                color: #333333;
            }
        """)
        clear_search_btn.setToolTip("清除搜索")
        clear_search_btn.clicked.connect(self.clear_checklist_search)
        
        search_layout.addWidget(search_label)
        search_layout.addWidget(self.checklist_search_input, 1)
        search_layout.addWidget(clear_search_btn)
        card.addLayout(search_layout)
        
        # 清单列表
        checklist_label = QLabel("📋 项目清单:")
        checklist_label.setStyleSheet("""
            QLabel {
                font-size: 14px;
                font-weight: 600;
                color: #333333;
                margin-top: 10px;
                margin-bottom: 5px;
            }
        """)
        card.addWidget(checklist_label)
        
        # 清单列表显示区域
        self.checklist_list = QListWidget()
        self.checklist_list.setMinimumHeight(300)
        self.checklist_list.setStyleSheet("""
            QListWidget {
                border: 2px solid #e8e8e8;
                border-radius: 10px;
                background-color: #fafafa;
                padding: 10px;
            }
            QListWidget::item {
                border: none;
                padding: 0px;
                margin: 8px 0;
                border-radius: 10px;
                background-color: transparent;
                min-height: 50px;
            }
            QScrollBar:vertical {
                border: none;
                background: #f0f0f0;
                width: 10px;
                margin: 0px;
                border-radius: 5px;
            }
            QScrollBar::handle:vertical {
                background: #c0c0c0;
                min-height: 20px;
                border-radius: 5px;
            }
            QScrollBar::handle:vertical:hover {
                background: #a0a0a0;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                height: 0px;
            }
        """)
        # 设置自动调整大小
        self.checklist_list.setWordWrap(True)
        self.checklist_list.setTextElideMode(Qt.ElideNone)
        self.checklist_list.setSelectionMode(QAbstractItemView.NoSelection)  # 禁用选择，因为我们使用按钮
        self.checklist_list.setFocusPolicy(Qt.NoFocus)  # 禁用焦点，避免选中高亮
        card.addWidget(self.checklist_list)
        
        # 初始化清单数据结构
        if 'checklist_items' not in self.project:
            self.project['checklist_items'] = []
        
        # 初始化搜索相关属性
        self.all_checklist_items = []
        
        # 加载清单内容
        self.load_checklist_items()
        
        return card

    def create_ia_resource_card(self):
        """创建IA资源卡片"""
        card = ModernCard("IA资源管理")
        
        # 主布局 - 使用网格布局来组织四个区域
        main_layout = QGridLayout()
        main_layout.setSpacing(16)
        main_layout.setContentsMargins(0, 0, 0, 0)
        
        # 1. 提示词资源区域
        prompt_card = self.create_prompt_resource_section()
        
        main_layout.addWidget(prompt_card, 0, 0)
        
        # 2. 资源绑定区域
        resource_card = self.create_resource_binding_section()
        main_layout.addWidget(resource_card, 0, 1)
        
        # 3. 账户密码区域
        account_card = self.create_account_password_section()
        main_layout.addWidget(account_card, 1, 0)
        
        # 4. 快速启动项绑定区域
        quick_launch_card = self.create_quick_launch_binding_section()
        main_layout.addWidget(quick_launch_card, 1, 1)
        
        # 设置列的拉伸比例
        main_layout.setColumnStretch(0, 1)
        main_layout.setColumnStretch(1, 1)
        
        card.addLayout(main_layout)
        

        
        return card
    
    def create_prompt_resource_section(self):
        """创建提示词资源区域"""
        section_card = QWidget()
        section_card.setStyleSheet("""
            QWidget {
                background-color: white;
                border: 1px solid #e0e0e0;
                border-radius: 8px;
                padding: 16px;
            }
        """)
        
        layout = QVBoxLayout(section_card)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(12)
        
        # 标题和添加按钮
        header_layout = QHBoxLayout()
        title_label = QLabel("📝 提示词资源")
        title_label.setStyleSheet("""
            QLabel {
                font-size: 16px;
                font-weight: bold;
                color: #333333;
            }
        """)
        header_layout.addWidget(title_label)
        header_layout.addStretch()
        
        add_prompt_btn = ModernButton("+ 绑定提示词", "primary")
        add_prompt_btn.clicked.connect(self.add_prompt_resource)
        header_layout.addWidget(add_prompt_btn)
        
        layout.addLayout(header_layout)
        
        # 已绑定的提示词列表
        self.prompt_list = QListWidget()
        self.prompt_list.setStyleSheet("""
            QListWidget {
                border: 1px solid #e0e0e0;
                border-radius: 4px;
                background-color: #fafafa;
                padding: 8px;
                min-height: 120px;
            }
            QListWidget::item {
                border: 1px solid #ddd;
                padding: 8px;
                margin: 2px 0;
                border-radius: 4px;
                background-color: white;
                color: black;
            }
            QListWidget::item:hover {
                background-color: #f5f5f5;
                color: black;
            }
            QListWidget::item:selected {
                background-color: #e3f2fd;
                border-color: #2196F3;
                color: black;
            }
        """)
        self.prompt_list.setWordWrap(True)
        self.prompt_list.setContextMenuPolicy(Qt.CustomContextMenu)
        self.prompt_list.customContextMenuRequested.connect(self.show_prompt_context_menu)
        
        layout.addWidget(self.prompt_list)
        
        # 提示词资源文件地址显示
        self.resource_file_path_label = QLabel()
        self.resource_file_path_label.setStyleSheet("""
            QLabel {
                color: #666666;
                font-size: 12px;
                padding: 8px;
                background-color: #f8f9fa;
                border-radius: 4px;
                border: 1px solid #e9ecef;
            }
        """)
        self.update_resource_file_path_display()
        layout.addWidget(self.resource_file_path_label)
        
        # 加载已绑定的提示词
        self.load_bound_prompts()
        
        return section_card
    
    def create_resource_binding_section(self):
        """创建资源绑定区域"""
        section_card = QWidget()
        section_card.setStyleSheet("""
            QWidget {
                background-color: white;
                border: 1px solid #e0e0e0;
                border-radius: 8px;
                padding: 16px;
            }
        """)
        
        layout = QVBoxLayout(section_card)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(12)
        
        # 标题和添加按钮
        header_layout = QHBoxLayout()
        title_label = QLabel("📁 资源绑定")
        title_label.setStyleSheet("""
            QLabel {
                font-size: 16px;
                font-weight: bold;
                color: #333333;
            }
        """)
        header_layout.addWidget(title_label)
        header_layout.addStretch()
        
        add_resource_btn = ModernButton("+ 绑定资源", "secondary")
        add_resource_btn.clicked.connect(self.add_resource_binding)
        header_layout.addWidget(add_resource_btn)
        
        layout.addLayout(header_layout)
        
        # 占位文本
        placeholder_label = QLabel("资源绑定功能开发中...")
        placeholder_label.setStyleSheet("""
            QLabel {
                color: #999999;
                font-style: italic;
                text-align: center;
                padding: 20px;
            }
        """)
        placeholder_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(placeholder_label)
        
        return section_card
    
    def create_account_password_section(self):
        """创建账户密码区域"""
        section_card = QWidget()
        section_card.setStyleSheet("""
            QWidget {
                background-color: white;
                border: 1px solid #e0e0e0;
                border-radius: 8px;
                padding: 16px;
            }
        """)
        
        layout = QVBoxLayout(section_card)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(12)
        
        # 标题和添加按钮
        header_layout = QHBoxLayout()
        title_label = QLabel("🔐 账户密码")
        title_label.setStyleSheet("""
            QLabel {
                font-size: 16px;
                font-weight: bold;
                color: #333333;
            }
        """)
        header_layout.addWidget(title_label)
        header_layout.addStretch()
        
        add_account_btn = ModernButton("+ 绑定账户", "secondary")
        add_account_btn.clicked.connect(self.add_account_password)
        header_layout.addWidget(add_account_btn)
        
        layout.addLayout(header_layout)
        
        # 占位文本
        placeholder_label = QLabel("账户密码功能开发中...")
        placeholder_label.setStyleSheet("""
            QLabel {
                color: #999999;
                font-style: italic;
                text-align: center;
                padding: 20px;
            }
        """)
        placeholder_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(placeholder_label)
        
        return section_card
    
    def create_quick_launch_binding_section(self):
        """创建快速启动项绑定区域"""
        section_card = QWidget()
        section_card.setStyleSheet("""
            QWidget {
                background-color: white;
                border: 1px solid #e0e0e0;
                border-radius: 8px;
                padding: 16px;
            }
        """)
        
        layout = QVBoxLayout(section_card)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(12)
        
        # 标题和添加按钮
        header_layout = QHBoxLayout()
        title_label = QLabel("🚀 快速启动项绑定")
        title_label.setStyleSheet("""
            QLabel {
                font-size: 16px;
                font-weight: bold;
                color: #333333;
            }
        """)
        header_layout.addWidget(title_label)
        header_layout.addStretch()
        
        add_quick_launch_btn = ModernButton("+ 绑定快启项", "secondary")
        add_quick_launch_btn.clicked.connect(self.add_quick_launch_binding)
        header_layout.addWidget(add_quick_launch_btn)
        
        layout.addLayout(header_layout)
        
        # 快速启动项列表
        self.quick_launch_list = QListWidget()
        self.quick_launch_list.setStyleSheet("""
            QListWidget {
                border: 1px solid #e0e0e0;
                border-radius: 4px;
                background-color: #fafafa;
                padding: 8px;
            }
            QListWidget::item {
                border: 1px solid #ddd;
                padding: 6px;
                margin: 3px 0;
                border-radius: 4px;
                background-color: white;
                color: black;
                min-height: 45px;  /* 减少最小高度，与组件最小高度匹配 */
            }
            QListWidget::item:hover {
                background-color: #f5f5f5;
                color: black;
            }
            QListWidget::item:selected {
                background-color: #e3f2fd;
                border-color: #2196F3;
                color: black;
            }
        """)
        self.quick_launch_list.setWordWrap(True)
        self.quick_launch_list.setContextMenuPolicy(Qt.CustomContextMenu)
        self.quick_launch_list.customContextMenuRequested.connect(self.show_quick_launch_context_menu)
        
        layout.addWidget(self.quick_launch_list)
        
        # 数据文件地址显示
        quick_launch_file_path_label = QLabel()
        quick_launch_file_path_label.setStyleSheet("""
            QLabel {
                font-size: 12px;
                color: #888888;
                margin-top: 8px;
                margin-bottom: 10px;
            }
        """)
        
        # 设置数据文件地址
        quick_launch_file = os.path.join('config', 'quick_settings.json')
        if os.path.exists(quick_launch_file):
            file_path = os.path.abspath(quick_launch_file)
            quick_launch_file_path_label.setText(f"📁 数据文件地址：{file_path}")
        else:
            quick_launch_file_path_label.setText("📁 数据文件地址：未找到 config/quick_settings.json")
        
        layout.addWidget(quick_launch_file_path_label)
        
        # 加载已绑定的快速启动项
        self.load_bound_quick_launch_items()
        
        return section_card
    
    def add_prompt_resource(self):
        """添加提示词资源"""
        try:
            # 读取提示词文件
            prompts_file = os.path.join('data', 'ai_prompt_data.json')
            if not os.path.exists(prompts_file):
                QMessageBox.warning(self, "警告", "未找到提示词文件 data/ai_prompt_data.json")
                return
            
            with open(prompts_file, 'r', encoding='utf-8') as f:
                prompts_data = json.load(f)
            
            if not prompts_data:
                QMessageBox.information(self, "提示", "提示词文件为空")
                return
            
            # 创建选择对话框
            dialog = QDialog(self)
            dialog.setWindowTitle("选择提示词")
            dialog.setModal(True)
            width, height = get_optimal_dialog_size(1200, 800)
            dialog.resize(width, height)
            center_window(dialog)
            
            layout = QVBoxLayout(dialog)
            layout.setContentsMargins(20, 20, 20, 20)
            layout.setSpacing(16)
            
            # 标题
            title_label = QLabel("选择要绑定的提示词")
            title_label.setStyleSheet("""
                QLabel {
                    font-size: 18px;
                    font-weight: bold;
                    color: #333333;
                    margin-bottom: 10px;
                }
            """)
            layout.addWidget(title_label)
            
            # 搜索框
            search_layout = QHBoxLayout()
            search_label = QLabel("搜索：")
            search_label.setStyleSheet("""
                QLabel {
                    font-size: 14px;
                    font-weight: 500;
                    color: #666666;
                }
            """)
            search_layout.addWidget(search_label)
            
            search_input = QLineEdit()
            search_input.setPlaceholderText("输入关键词搜索提示词内容或场景...")
            search_input.setStyleSheet("""
                QLineEdit {
                    border: 1px solid #e0e0e0;
                    border-radius: 4px;
                    padding: 8px 12px;
                    font-size: 14px;
                    background-color: white;
                }
                QLineEdit:focus {
                    border-color: #2196F3;
                }
            """)
            search_layout.addWidget(search_input)
            
            # 清除搜索按钮
            clear_search_btn = ModernButton("清除", "secondary")
            clear_search_btn.setFixedSize(80, 32)
            clear_search_btn.clicked.connect(search_input.clear)
            search_layout.addWidget(clear_search_btn)
            
            layout.addLayout(search_layout)
            
            # 提示词列表
            prompt_list = QListWidget()
            prompt_list.setStyleSheet("""
                QListWidget {
                    border: 1px solid #e0e0e0;
                    border-radius: 4px;
                    background-color: #fafafa;
                    padding: 8px;
                }
                QListWidget::item {
                    border: 1px solid #ddd;
                    padding: 12px;
                    margin: 4px 0;
                    border-radius: 4px;
                    background-color: white;
                    color: black;
                }
                QListWidget::item:hover {
                    background-color: #f5f5f5;
                    color: black;
                }
                QListWidget::item:selected {
                    background-color: #e3f2fd;
                    border-color: #2196F3;
                    color: black;
                }
            """)
            prompt_list.setWordWrap(True)
            
            # 添加提示词到列表 - 正确处理新格式数据
            prompts_to_display = []
            
            # 新的数据格式：从content.prompts数组中提取
            if 'content' in prompts_data and 'prompts' in prompts_data['content']:
                prompts_to_display = [(item.get('id', ''), item) for item in prompts_data['content']['prompts']]
            # 兼容旧格式（如果有的话）
            else:
                prompts_to_display = list(prompts_data.items())
            
            # 存储所有提示词数据，用于搜索过滤
            all_prompts = prompts_to_display.copy()
            
            # 创建列表项的函数
            def create_prompt_items(prompts_list):
                """创建提示词列表项"""
                prompt_list.clear()
                for prompt_id, prompt_data in prompts_list:
                    # 创建自定义列表项小部件 - 使用ModernPromptListItemWidget，实现现代化UI
                    item_widget = ModernPromptListItemWidget(prompt_id, prompt_data, dialog)
                    
                    # 创建列表项并设置小部件
                    item = QListWidgetItem()
                    item.setSizeHint(item_widget.sizeHint())
                    item.setData(Qt.UserRole, {'id': prompt_id, 'data': prompt_data})
                    
                    # 添加到列表
                    prompt_list.addItem(item)
                    prompt_list.setItemWidget(item, item_widget)
            
            # 初始加载所有提示词
            create_prompt_items(prompts_to_display)
            
            # 搜索功能
            def filter_prompts(text):
                """根据搜索文本过滤提示词"""
                if not text.strip():
                    # 如果搜索框为空，显示所有提示词
                    create_prompt_items(all_prompts)
                    return
                
                search_text = text.lower().strip()
                filtered_prompts = []
                
                for prompt_id, prompt_data in all_prompts:
                    # 检查提示词内容是否包含搜索文本
                    prompt_content = prompt_data.get('prompt', '').lower()
                    # 检查场景是否包含搜索文本
                    scene = prompt_data.get('scene', '').lower()
                    
                    if search_text in prompt_content or search_text in scene:
                        filtered_prompts.append((prompt_id, prompt_data))
                
                # 更新列表显示
                create_prompt_items(filtered_prompts)
            
            # 连接搜索框的文本变化信号
            search_input.textChanged.connect(filter_prompts)
            
            layout.addWidget(prompt_list)
            
            # 备注输入
            remark_label = QLabel("备注（可选）：")
            remark_label.setStyleSheet("""
                QLabel {
                    font-size: 14px;
                    font-weight: 500;
                    color: #666666;
                    margin-top: 10px;
                }
            """)
            layout.addWidget(remark_label)
            
            remark_input = QLineEdit()
            remark_input.setPlaceholderText("为这个提示词添加备注说明...")
            remark_input.setStyleSheet("""
                QLineEdit {
                    border: 1px solid #e0e0e0;
                    border-radius: 4px;
                    padding: 8px 12px;
                    font-size: 14px;
                    background-color: white;
                }
                QLineEdit:focus {
                    border-color: #2196F3;
                }
            """)
            layout.addWidget(remark_input)
            

            
            # 按钮区域 - 添加新增提示词按钮
            button_layout = QHBoxLayout()
            
            # 添加新增提示词按钮
            add_new_prompt_btn = ModernButton("+ 新增提示词", "success")
            # 使用lambda传递dialog对象，以便在添加提示词后刷新当前对话框
            add_new_prompt_btn.clicked.connect(lambda: self.add_new_prompt_from_dialog(dialog, prompt_list, search_input, all_prompts, create_prompt_items))
            button_layout.addWidget(add_new_prompt_btn)
            
            # 添加弹性空间
            button_layout.addStretch()
            
            cancel_btn = ModernButton("取消", "secondary")
            cancel_btn.clicked.connect(dialog.reject)
            button_layout.addWidget(cancel_btn)
            
            ok_btn = ModernButton("确定", "primary")
            ok_btn.clicked.connect(dialog.accept)
            button_layout.addWidget(ok_btn)
            
            layout.addLayout(button_layout)
            
            # 显示对话框
            if dialog.exec_() == QDialog.Accepted:
                selected_items = prompt_list.selectedItems()
                if not selected_items:
                    QMessageBox.warning(self, "警告", "请选择一个提示词")
                    return
                
                selected_item = selected_items[0]
                prompt_info = selected_item.data(Qt.UserRole)
                remark = remark_input.text().strip()
                
                # 创建绑定信息
                bound_prompt = {
                    'id': f"prompt_{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}",
                    'prompt_id': prompt_info['id'],
                    'scene': prompt_info['data'].get('scene', '未分类'),
                    'prompt': prompt_info['data']['prompt'],
                    'remark': remark,
                    'bound_time': datetime.now().isoformat(),
                    'resource_type': 'prompt',
                    'resource_file': os.path.abspath(prompts_file)
                }
                
                # 添加到项目数据
                if 'ia_resources' not in self.project:
                    self.project['ia_resources'] = []
                
                self.project['ia_resources'].append(bound_prompt)
                
                # 保存项目数据
                self.save_project_data()
                
                # 刷新显示
                self.load_bound_prompts()
                self.update_resource_file_path_display()
                
                # 更新tab标题中的数量
                self.update_tab_counts()
                
                # 记录项目日志
                self.parent().add_project_log(self.project['name'], "绑定提示词资源", 
                                             f"绑定了提示词：[{bound_prompt['scene']}] {bound_prompt['prompt'][:50]}...", 
                                             "资源")
                
                QMessageBox.information(self, "成功", "提示词资源绑定成功！")
                
        except Exception as e:
            QMessageBox.critical(self, "错误", f"添加提示词资源失败：{str(e)}")
    
    def add_new_prompt_from_dialog(self, dialog, prompt_list, search_input, all_prompts, create_prompt_items):
        """从提示词选择对话框中添加新提示词"""
        try:
            # 导入ai_prompt_tool模块
            import sys
            import os
            
            # 获取ai_prompt_tool.py的路径
            current_dir = os.path.dirname(os.path.abspath(__file__))
            ai_prompt_tool_path = os.path.join(current_dir, 'ai_prompt_tool.py')
            
            # 动态导入ai_prompt_tool模块
            if ai_prompt_tool_path not in sys.path:
                sys.path.insert(0, current_dir)
            
            from ai_prompt_tool import PromptTool
            
            # 创建提示词添加对话框
            add_dialog = QDialog(dialog)
            add_dialog.setWindowTitle("新增提示词")
            add_dialog.setModal(True)
            width, height = get_optimal_dialog_size(800, 600)
            add_dialog.resize(width, height)
            center_window(add_dialog)
            
            layout = QVBoxLayout(add_dialog)
            layout.setContentsMargins(20, 20, 20, 20)
            layout.setSpacing(16)
            
            # 标题
            title_label = QLabel("添加新提示词")
            title_label.setStyleSheet("""
                QLabel {
                    font-size: 18px;
                    font-weight: bold;
                    color: #333333;
                    margin-bottom: 10px;
                }
            """)
            layout.addWidget(title_label)
            
            # 提示词输入区域
            prompt_label = QLabel("提示词内容：")
            prompt_label.setStyleSheet("""
                QLabel {
                    font-size: 14px;
                    font-weight: 500;
                    color: #666666;
                }
            """)
            layout.addWidget(prompt_label)
            
            prompt_input = QTextEdit()
            prompt_input.setPlaceholderText("请输入提示词内容...")
            prompt_input.setStyleSheet("""
                QTextEdit {
                    border: 1px solid #e0e0e0;
                    border-radius: 4px;
                    padding: 8px 12px;
                    font-size: 14px;
                    background-color: white;
                    min-height: 120px;
                }
                QTextEdit:focus {
                    border-color: #2196F3;
                }
            """)
            layout.addWidget(prompt_input)
            
            # 使用场景输入
            scene_label = QLabel("使用场景：")
            scene_label.setStyleSheet("""
                QLabel {
                    font-size: 14px;
                    font-weight: 500;
                    color: #666666;
                }
            """)
            layout.addWidget(scene_label)
            
            scene_input = QLineEdit()
            scene_input.setPlaceholderText("请输入使用场景，如：代码生成、文本分析等...")
            scene_input.setStyleSheet("""
                QLineEdit {
                    border: 1px solid #e0e0e0;
                    border-radius: 4px;
                    padding: 8px 12px;
                    font-size: 14px;
                    background-color: white;
                }
                QLineEdit:focus {
                    border-color: #2196F3;
                }
            """)
            layout.addWidget(scene_input)
            
            # 关联软件路径
            software_layout = QHBoxLayout()
            software_label = QLabel("关联软件：")
            software_label.setStyleSheet("""
                QLabel {
                    font-size: 14px;
                    font-weight: 500;
                    color: #666666;
                }
            """)
            software_layout.addWidget(software_label)
            
            software_path = QLineEdit()
            software_path.setPlaceholderText("选择关联的软件路径（可选）...")
            software_path.setStyleSheet("""
                QLineEdit {
                    border: 1px solid #e0e0e0;
                    border-radius: 4px;
                    padding: 8px 12px;
                    font-size: 14px;
                    background-color: white;
                }
                QLineEdit:focus {
                    border-color: #2196F3;
                }
            """)
            software_layout.addWidget(software_path)
            
            browse_btn = ModernButton("选择", "secondary")
            browse_btn.clicked.connect(lambda: self.browse_software_file(software_path))
            software_layout.addWidget(browse_btn)
            
            layout.addLayout(software_layout)
            
            # 字数统计标签
            word_count_label = QLabel("字数：0")
            word_count_label.setStyleSheet("""
                QLabel {
                    color: #666666;
                    font-size: 12px;
                    text-align: right;
                }
            """)
            layout.addWidget(word_count_label)
            
            # 更新字数统计
            def update_word_count():
                text = prompt_input.toPlainText()
                word_count_label.setText(f"字数：{len(text)}")
            
            prompt_input.textChanged.connect(update_word_count)
            
            # 按钮
            button_layout = QHBoxLayout()
            button_layout.addStretch()
            
            cancel_btn = ModernButton("取消", "secondary")
            cancel_btn.clicked.connect(add_dialog.reject)
            button_layout.addWidget(cancel_btn)
            
            save_btn = ModernButton("保存", "primary")
            save_btn.clicked.connect(add_dialog.accept)
            button_layout.addWidget(save_btn)
            
            layout.addLayout(button_layout)
            
            # 显示对话框
            if add_dialog.exec_() == QDialog.Accepted:
                prompt_text = prompt_input.toPlainText().strip()
                scene = scene_input.text().strip() or "未分类"
                software = software_path.text().strip()
                
                if not prompt_text:
                    QMessageBox.warning(self, "警告", "请输入提示词内容")
                    return
                
                # 使用ai_prompt_tool的add_prompt函数添加提示词
                from ai_prompt_tool import add_prompt
                add_prompt(prompt_text, scene, software)
                
                QMessageBox.information(self, "成功", "提示词添加成功！")
                
                # 刷新提示词列表 - 清空当前列表并重新加载
                self.refresh_prompt_list(prompt_list)
                
                # 刷新搜索结果 - 更新all_prompts并重新应用搜索过滤
                self.update_all_prompts(all_prompts)
                # 应用当前的搜索过滤
                filter_text = search_input.text().strip()
                if filter_text:
                    self.filter_prompts(filter_text, all_prompts, prompt_list, create_prompt_items)
                else:
                    # 如果没有搜索文本，显示所有提示词
                    self.create_prompt_items(all_prompts, prompt_list)
                
        except Exception as e:
            QMessageBox.critical(self, "错误", f"添加新提示词失败：{str(e)}")
    
    def update_all_prompts(self, all_prompts):
        """更新all_prompts列表"""
        try:
            # 清空当前列表
            all_prompts.clear()
            
            # 重新读取提示词文件
            prompts_file = os.path.join('data', 'ai_prompt_data.json')
            if not os.path.exists(prompts_file):
                return
            
            with open(prompts_file, 'r', encoding='utf-8') as f:
                prompts_data = json.load(f)
            
            # 添加提示词到列表
            prompts_to_display = []
            
            # 新的数据格式：从content.prompts数组中提取
            if 'content' in prompts_data and 'prompts' in prompts_data['content']:
                prompts_to_display = [(item.get('id', ''), item) for item in prompts_data['content']['prompts']]
            # 兼容旧格式（如果有的话）
            else:
                prompts_to_display = list(prompts_data.items())
            
            all_prompts.extend(prompts_to_display)
                
        except Exception as e:
            print(f"更新all_prompts失败: {str(e)}")
    
    def create_prompt_items(self, prompts_data, prompt_list):
        """创建提示词列表项"""
        try:
            # 清空当前列表
            prompt_list.clear()
            
            for prompt_id, prompt_data in prompts_data:
                # 创建自定义列表项小部件 - 使用ModernPromptListItemWidget，实现现代化UI
                item_widget = ModernPromptListItemWidget(prompt_id, prompt_data, prompt_list.parentWidget())
                
                # 创建列表项并设置小部件
                item = QListWidgetItem()
                item.setSizeHint(item_widget.sizeHint())
                item.setData(Qt.UserRole, {'id': prompt_id, 'data': prompt_data})
                
                # 添加到列表
                prompt_list.addItem(item)
                prompt_list.setItemWidget(item, item_widget)
                
        except Exception as e:
            print(f"创建提示词列表项失败: {str(e)}")

    def refresh_prompt_list(self, prompt_list):
        """刷新提示词列表"""
        try:
            # 清空当前列表
            prompt_list.clear()
            
            # 重新读取提示词文件
            prompts_file = os.path.join('data', 'ai_prompt_data.json')
            if not os.path.exists(prompts_file):
                return
            
            with open(prompts_file, 'r', encoding='utf-8') as f:
                prompts_data = json.load(f)
            
            # 添加提示词到列表
            prompts_to_display = []
            
            # 新的数据格式：从content.prompts数组中提取
            if 'content' in prompts_data and 'prompts' in prompts_data['content']:
                prompts_to_display = [(item.get('id', ''), item) for item in prompts_data['content']['prompts']]
            # 兼容旧格式（如果有的话）
            else:
                prompts_to_display = list(prompts_data.items())
            
            for prompt_id, prompt_data in prompts_to_display:
                # 创建自定义列表项小部件 - 使用ModernPromptListItemWidget，实现现代化UI
                item_widget = ModernPromptListItemWidget(prompt_id, prompt_data, prompt_list.parentWidget())
                
                # 创建列表项并设置小部件
                item = QListWidgetItem()
                item.setSizeHint(item_widget.sizeHint())
                item.setData(Qt.UserRole, {'id': prompt_id, 'data': prompt_data})
                
                # 添加到列表
                prompt_list.addItem(item)
                prompt_list.setItemWidget(item, item_widget)
                
        except Exception as e:
            print(f"刷新提示词列表失败: {str(e)}")
    
    def browse_software_file(self, line_edit):
        """浏览软件文件"""
        file_path, _ = QFileDialog.getOpenFileName(
            self, 
            "选择软件文件", 
            "", 
            "可执行文件 (*.exe);;所有文件 (*.*)"
        )
        if file_path:
            line_edit.setText(file_path)
    
    def load_bound_prompts(self):
        """加载已绑定的提示词"""
        self.prompt_list.clear()
        
        ia_resources = self.project.get('ia_resources', [])
        prompt_resources = [res for res in ia_resources if res.get('resource_type') == 'prompt']
        
        if not prompt_resources:
            placeholder_item = QListWidgetItem("暂无绑定的提示词资源")
            placeholder_item.setTextAlignment(Qt.AlignCenter)
            placeholder_item.setFlags(Qt.NoItemFlags)
            self.prompt_list.addItem(placeholder_item)
            return
        
        for resource in prompt_resources:
            # 获取最新的提示词内容
            prompt_content = self.get_latest_prompt_content(resource['prompt_id'])
            if prompt_content:
                resource['prompt'] = prompt_content
            
            # 确保备注字段存在，如果不存在则设置为空字符串
            if 'remark' not in resource:
                resource['remark'] = ''
            
            # 创建固定大小的卡片小部件
            item_widget = BoundPromptCardWidget(resource, self, self)
            
            # 创建列表项并设置小部件
            item = QListWidgetItem()
            item.setSizeHint(QSize(410, 180))  # 增加高度以适应新的卡片设计
            item.setData(Qt.UserRole, resource)
            
            # 添加到列表
            self.prompt_list.addItem(item)
            self.prompt_list.setItemWidget(item, item_widget)
    
    def get_latest_prompt_content(self, prompt_id):
        """获取最新的提示词内容"""
        try:
            prompts_file = os.path.join('data', 'ai_prompt_data.json')
            if not os.path.exists(prompts_file):
                return None
            
            with open(prompts_file, 'r', encoding='utf-8') as f:
                prompts_data = json.load(f)
            
            # 新的数据格式：从content.prompts数组中查找
            if 'content' in prompts_data and 'prompts' in prompts_data['content']:
                for prompt_item in prompts_data['content']['prompts']:
                    if prompt_item.get('id') == prompt_id:
                        return prompt_item.get('prompt', '')
            
            # 兼容旧格式（如果有的话）
            elif prompt_id in prompts_data:
                return prompts_data[prompt_id].get('prompt', '')
            
            return None
        except:
            return None
    
    def show_prompt_context_menu(self, pos):
        """显示提示词右键菜单"""
        item = self.prompt_list.itemAt(pos)
        if not item:
            return
        
        resource = item.data(Qt.UserRole)
        
        menu = QMenu(self)
        menu.setStyleSheet("""
            QMenu {
                background-color: white;
                border: 1px solid #e0e0e0;
                border-radius: 4px;
                padding: 4px;
            }
            QMenu::item {
                padding: 8px 16px;
                border-radius: 4px;
            }
            QMenu::item:selected {
                background-color: #e3f2fd;
                color: #1976d2;
            }
        """)
        
        # 添加复制动作
        copy_action = menu.addAction("复制提示词")
        copy_action.triggered.connect(lambda: self.copy_prompt_to_clipboard(resource['prompt']))
        
        # 添加编辑备注动作
        edit_action = menu.addAction("编辑备注")
        edit_action.triggered.connect(lambda: self.edit_prompt_remark(item))
        
        # 添加删除绑定动作
        delete_action = menu.addAction("删除绑定")
        delete_action.triggered.connect(lambda: self.delete_prompt_binding(item))
        
        menu.exec_(self.prompt_list.mapToGlobal(pos))
    
    def copy_prompt_to_clipboard(self, text):
        """复制文本到剪贴板"""
        clipboard = QApplication.clipboard()
        clipboard.setText(text)
        self.parent().show_status_message("提示词已复制到剪贴板")
    
    def edit_prompt_remark(self, item):
        """编辑提示词备注"""
        resource = item.data(Qt.UserRole)
        if not resource:
            return
        
        current_remark = resource.get('remark', '')
        new_remark, ok = QInputDialog.getText(self, "编辑备注", "请输入新的备注：", text=current_remark)
        
        if ok:
            # 更新资源备注
            resource['remark'] = new_remark.strip()
            
            # 在项目数据中更新对应的资源
            ia_resources = self.project.get('ia_resources', [])
            for i, res in enumerate(ia_resources):
                if res.get('id') == resource.get('id'):
                    ia_resources[i] = resource
                    break
            
            # 保存项目数据
            self.save_project_data()
            
            # 刷新显示
            self.load_bound_prompts()
            
            # 更新tab标题中的数量
            self.update_tab_counts()
            
            # 记录项目日志
            self.parent().add_project_log(self.project['name'], "编辑提示词备注", 
                                         f"修改了提示词备注：[{resource['scene']}] {resource['prompt'][:30]}...", 
                                         "资源")
    
    def delete_prompt_binding(self, item):
        """删除提示词绑定"""
        resource = item.data(Qt.UserRole)
        if not resource:
            return
        
        reply = QMessageBox.question(self, "确认删除", 
                                   f"确定要删除提示词绑定吗？\n\n[{resource['scene']}] {resource['prompt'][:50]}...",
                                   QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            # 从项目数据中删除
            ia_resources = self.project.get('ia_resources', [])
            self.project['ia_resources'] = [res for res in ia_resources if res.get('id') != resource.get('id')]
            
            # 保存项目数据
            self.save_project_data()
            
            # 刷新显示
            self.load_bound_prompts()
            
            # 更新tab标题中的数量
            self.update_tab_counts()
            
            # 记录项目日志
            self.parent().add_project_log(self.project['name'], "删除提示词绑定", 
                                         f"删除了提示词绑定：[{resource['scene']}] {resource['prompt'][:50]}...", 
                                         "资源")
    
    def update_resource_file_path_display(self):
        """更新资源文件路径显示"""
        if hasattr(self, 'resource_file_path_label'):
            prompts_file = os.path.join('data', 'ai_prompt_data.json')
            if os.path.exists(prompts_file):
                file_path = os.path.abspath(prompts_file)
                self.resource_file_path_label.setText(f"📁 资源文件地址：{file_path}")
            else:
                self.resource_file_path_label.setText("📁 资源文件地址：未找到 data/ai_prompt_data.json")
    
    def add_resource_binding(self):
        """添加资源绑定（占位方法）"""
        QMessageBox.information(self, "提示", "资源绑定功能开发中...")
    
    def add_account_password(self):
        """添加账户密码（占位方法）"""
        QMessageBox.information(self, "提示", "账户密码功能开发中...")
    
    def add_quick_launch_binding(self):
        """添加快速启动项绑定"""
        try:
            # 读取快速启动项文件
            quick_launch_file = os.path.join('config', 'quick_settings.json')
            if not os.path.exists(quick_launch_file):
                QMessageBox.warning(self, "警告", "未找到快速启动项文件 config/quick_settings.json")
                return
            
            with open(quick_launch_file, 'r', encoding='utf-8') as f:
                quick_launch_data = json.load(f)
            
            if not quick_launch_data:
                QMessageBox.information(self, "提示", "快速启动项文件为空")
                return
            
            # 创建选择对话框
            dialog = QDialog(self)
            dialog.setWindowTitle("选择快速启动项")
            dialog.setModal(True)
            width, height = get_optimal_dialog_size(1200, 800)
            dialog.resize(width, height)
            center_window(dialog)
            
            layout = QVBoxLayout(dialog)
            layout.setContentsMargins(20, 20, 20, 20)
            layout.setSpacing(16)
            
            # 标题
            title_label = QLabel("选择要绑定的快速启动项")
            title_label.setStyleSheet("""
                QLabel {
                    font-size: 16px;
                    font-weight: bold;
                    color: #333333;
                    margin-bottom: 10px;
                }
            """)
            layout.addWidget(title_label)
            
            # 学习绑定提示区域
            tip_label = QLabel("💡 学习绑定提示：选择下方的快速启动项，系统会将其绑定到当前项目中，方便快速访问和启动")
            tip_label.setStyleSheet("""
                QLabel {
                    font-size: 13px;
                    color: #666666;
                    background-color: #f0f8ff;
                    border: 1px solid #b3d9ff;
                    border-radius: 6px;
                    padding: 10px;
                    margin-bottom: 15px;
                }
            """)
            tip_label.setWordWrap(True)
            layout.addWidget(tip_label)
            
            # 快速启动项列表 - 适应ModernQuickLaunchListItemWidget的卡片式设计
            quick_launch_list = QListWidget()
            quick_launch_list.setStyleSheet("""
                QListWidget {
                    background-color: #f8f9fa;
                    border: none;
                    outline: none;
                    padding: 4px;
                }
                QListWidget::item {
                    background: transparent;
                    border: none;
                    padding: 4px 8px;
                    margin: 2px 0;
                }
                QListWidget::item:selected {
                    background: transparent;
                    border: 2px solid #3498db;
                    border-radius: 8px;
                    padding: 2px 6px;
                }
                QListWidget::item:hover {
                    background: transparent;
                }
            """)
            quick_launch_list.setWordWrap(True)
            
            # 添加快速启动项到列表
            # 确保launches节点存在
            if 'launches' not in quick_launch_data:
                QMessageBox.information(self, "提示", "快速启动项文件中没有找到launches节点")
                return
                
            for launch_id, launch_data in quick_launch_data['launches'].items():
                # 创建自定义列表项小部件 - 使用ModernQuickLaunchListItemWidget，实现现代化UI
                item_widget = ModernQuickLaunchListItemWidget(launch_id, launch_data, dialog)
                
                # 创建列表项并设置小部件
                item = QListWidgetItem()
                item.setSizeHint(item_widget.sizeHint())
                item.setData(Qt.UserRole, {'id': launch_id, 'data': launch_data})
                
                # 添加到列表
                quick_launch_list.addItem(item)
                quick_launch_list.setItemWidget(item, item_widget)
            
            # 连接选择事件，用于更新选中状态样式
            def on_item_selection_changed():
                # 获取所有项
                for i in range(quick_launch_list.count()):
                    item = quick_launch_list.item(i)
                    widget = quick_launch_list.itemWidget(item)
                    if widget and isinstance(widget, ModernQuickLaunchListItemWidget):
                        # 检查是否被选中
                        is_selected = item.isSelected()
                        widget.set_selected(is_selected)
            
            quick_launch_list.itemSelectionChanged.connect(on_item_selection_changed)
            
            layout.addWidget(quick_launch_list)
            
            # 备注输入
            remark_label = QLabel("备注（可选）：")
            remark_label.setStyleSheet("""
                QLabel {
                    font-size: 14px;
                    font-weight: 500;
                    color: #666666;
                    margin-top: 10px;
                }
            """)
            layout.addWidget(remark_label)
            
            remark_input = QLineEdit()
            remark_input.setPlaceholderText("为这个快速启动项添加备注说明...")
            remark_input.setStyleSheet("""
                QLineEdit {
                    border: 1px solid #e0e0e0;
                    border-radius: 4px;
                    padding: 8px 12px;
                    font-size: 14px;
                    background-color: white;
                }
                QLineEdit:focus {
                    border-color: #2196F3;
                }
            """)
            layout.addWidget(remark_input)
            
            # 按钮
            button_layout = QHBoxLayout()
            button_layout.addStretch()
            
            cancel_btn = ModernButton("取消", "secondary")
            cancel_btn.clicked.connect(dialog.reject)
            button_layout.addWidget(cancel_btn)
            
            ok_btn = ModernButton("确定", "primary")
            ok_btn.clicked.connect(dialog.accept)
            button_layout.addWidget(ok_btn)
            
            layout.addLayout(button_layout)
            
            # 显示对话框
            if dialog.exec_() == QDialog.Accepted:
                selected_items = quick_launch_list.selectedItems()
                if not selected_items:
                    QMessageBox.warning(self, "警告", "请选择一个快速启动项")
                    return
                
                selected_item = selected_items[0]
                launch_info = selected_item.data(Qt.UserRole)
                remark = remark_input.text().strip()
                
                # 创建绑定信息
                bound_launch = {
                    'id': f"quick_launch_{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}",
                    'launch_id': launch_info['id'],
                    'category': launch_info['data'].get('type', '未分类'),
                    'name': launch_info['id'],  # 使用launch_id作为名称
                    'description': launch_info['data'].get('description', ''),
                    'remark': remark,
                    'bound_time': datetime.now().isoformat(),
                    'resource_type': 'quick_launch',
                    'resource_file': os.path.abspath(quick_launch_file)
                }
                
                # 添加到项目数据
                if 'ia_resources' not in self.project:
                    self.project['ia_resources'] = []
                
                self.project['ia_resources'].append(bound_launch)
                
                # 保存项目数据
                self.save_project_data()
                
                # 刷新显示
                self.load_bound_quick_launch_items()
                
                # 更新tab标题中的数量
                self.update_tab_counts()
                
                # 记录项目日志
                self.parent().add_project_log(self.project['name'], "绑定快速启动项", 
                                             f"绑定了快速启动项：[{bound_launch['category']}] {bound_launch['name']}", 
                                             "资源")
                
                QMessageBox.information(self, "成功", "快速启动项绑定成功！")
                
        except Exception as e:
            QMessageBox.critical(self, "错误", f"添加快速启动项绑定失败：{str(e)}")

    
    def load_bound_quick_launch_items(self):
        """加载已绑定的快速启动项"""
        self.quick_launch_list.clear()
        
        ia_resources = self.project.get('ia_resources', [])
        quick_launch_resources = [res for res in ia_resources if res.get('resource_type') == 'quick_launch']
        
        if not quick_launch_resources:
            placeholder_item = QListWidgetItem("暂无绑定的快速启动项")
            placeholder_item.setTextAlignment(Qt.AlignCenter)
            placeholder_item.setFlags(Qt.NoItemFlags)
            self.quick_launch_list.addItem(placeholder_item)
            return
        
        for resource in quick_launch_resources:
            # 获取最新的快速启动项内容
            latest_content = self.get_latest_quick_launch_content(resource['launch_id'])
            if latest_content:
                # 使用launch_id作为名称，因为quick_settings.json中的launches节点是以名称为键的
                resource['name'] = resource['launch_id']
                resource['description'] = latest_content.get('description', resource.get('description', ''))
            
            display_text = f"[{resource['category']}] {resource['name']}"
            if resource.get('description'):
                display_text += f"\n{resource['description']}"
            if resource.get('remark'):
                display_text += f"\n💡 {resource['remark']}"
            
            # 创建自定义列表项小部件 - 使用QuickLaunchItemWidget而不是PromptListItemWidget
            item_widget = QuickLaunchItemWidget(display_text, resource['launch_id'], self)
            
            # 确保小部件已经正确计算了大小
            item_widget.adjust_widget_height()
            
            # 创建列表项并设置小部件
            item = QListWidgetItem()
            # 减少额外高度，确保内容完全显示且按钮不超出边框
            item.setSizeHint(QSize(self.quick_launch_list.width(), item_widget.sizeHint().height() + 5))
            item.setData(Qt.UserRole, resource)
            
            # 添加到列表
            self.quick_launch_list.addItem(item)
            self.quick_launch_list.setItemWidget(item, item_widget)
    
    def get_latest_quick_launch_content(self, launch_id):
        """获取最新的快速启动项内容"""
        try:
            quick_launch_file = os.path.join('config', 'quick_settings.json')
            if not os.path.exists(quick_launch_file):
                return None
            
            with open(quick_launch_file, 'r', encoding='utf-8') as f:
                quick_launch_data = json.load(f)
            
            # 确保launches节点存在
            if 'launches' not in quick_launch_data:
                return None
                
            if launch_id in quick_launch_data['launches']:
                return quick_launch_data['launches'][launch_id]
            
            return None
        except:
            return None
    
    def show_quick_launch_context_menu(self, pos):
        """显示快速启动项右键菜单"""
        item = self.quick_launch_list.itemAt(pos)
        if not item:
            return
        
        menu = QMenu(self)
        menu.setStyleSheet("""
            QMenu {
                background-color: white;
                border: 1px solid #e0e0e0;
                border-radius: 4px;
                padding: 4px;
            }
            QMenu::item {
                padding: 8px 16px;
                border-radius: 4px;
            }
            QMenu::item:selected {
                background-color: #e3f2fd;
                color: #1976d2;
            }
        """)
        
        edit_action = menu.addAction("编辑备注")
        delete_action = menu.addAction("删除绑定")
        
        action = menu.exec_(self.quick_launch_list.mapToGlobal(pos))
        
        if action == edit_action:
            self.edit_quick_launch_remark(item)
        elif action == delete_action:
            self.delete_quick_launch_binding(item)
    
    def edit_quick_launch_remark(self, item):
        """编辑快速启动项备注"""
        resource = item.data(Qt.UserRole)
        if not resource:
            return
        
        current_remark = resource.get('remark', '')
        new_remark, ok = QInputDialog.getText(self, "编辑备注", "请输入新的备注：", text=current_remark)
        
        if ok:
            # 更新资源备注
            resource['remark'] = new_remark.strip()
            
            # 在项目数据中更新对应的资源
            ia_resources = self.project.get('ia_resources', [])
            for i, res in enumerate(ia_resources):
                if res.get('id') == resource.get('id'):
                    ia_resources[i] = resource
                    break
            
            # 保存项目数据
            self.save_project_data()
            
            # 刷新显示
            self.load_bound_quick_launch_items()
            
            # 更新tab标题中的数量
            self.update_tab_counts()
            
            # 记录项目日志
            self.parent().add_project_log(self.project['name'], "编辑快速启动项备注", 
                                         f"修改了快速启动项备注：[{resource['category']}] {resource['name']}", 
                                         "资源")
    
    def delete_quick_launch_binding(self, item):
        """删除快速启动项绑定"""
        resource = item.data(Qt.UserRole)
        if not resource:
            return
        
        reply = QMessageBox.question(self, "确认删除", 
                                   f"确定要删除快速启动项绑定吗？\n\n[{resource['category']}] {resource['name']}",
                                   QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            # 从项目数据中删除
            ia_resources = self.project.get('ia_resources', [])
            self.project['ia_resources'] = [res for res in ia_resources if res.get('id') != resource.get('id')]
            
            # 保存项目数据
            self.save_project_data()
            
            # 刷新显示
            self.load_bound_quick_launch_items()
            
            # 更新tab标题中的数量
            self.update_tab_counts()
            
            # 记录项目日志
            self.parent().add_project_log(self.project['name'], "删除快速启动项绑定", 
                                         f"删除了快速启动项绑定：[{resource['category']}] {resource['name']}", 
                                         "资源")
    
    def add_checklist_item(self):
        """添加清单项"""
        text, ok = QInputDialog.getMultiLineText(self, "添加清单项", "请输入清单项内容:", "")
        if ok and text.strip():
            # 创建新清单项
            new_item = {
                'id': f"checklist_{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}",
                'text': text.strip(),
                'completed': False,
                'timestamp': datetime.now().isoformat()
            }
            
            # 添加到项目数据
            if 'checklist_items' not in self.project:
                self.project['checklist_items'] = []
            self.project['checklist_items'].append(new_item)
            
            # 记录项目日志
            self.parent().add_project_log(self.project['name'], "添加清单项", 
                                         f"添加了新清单项：{new_item['text']}", 
                                         "清单")
            
            # 保存项目数据
            self.save_project_data()
            
            # 刷新显示
            self.load_checklist_items()
            
            # 更新tab标题中的数量
            self.update_tab_counts()
            
            # 如果有搜索条件，重新应用搜索
            if hasattr(self, 'checklist_search_input') and self.checklist_search_input.text().strip():
                self.filter_checklist()
            
            QMessageBox.information(self, "成功", "清单项已添加！")
    
    def edit_checklist_item(self, item):
        """编辑清单项"""
        item_data = item.data(Qt.UserRole)
        if item_data:
            current_text = item_data.get('text', '')
            text, ok = QInputDialog.getMultiLineText(self, "编辑清单项", "请修改清单项内容:", current_text)
            if ok and text.strip():
                # 更新清单项文本
                item_data['text'] = text.strip()
                
                # 在项目数据中找到并更新对应的清单项
                checklist_items = self.project.get('checklist_items', [])
                for i, checklist_item in enumerate(checklist_items):
                    if checklist_item.get('id') == item_data.get('id'):
                        checklist_items[i] = item_data
                        break
                
                # 记录项目日志
                self.parent().add_project_log(self.project['name'], "编辑清单项", 
                                             f"编辑了清单项：{text.strip()}", 
                                             "清单")
                
                # 保存项目数据
                self.save_project_data()
                
                # 刷新显示
                self.load_checklist_items()
                # 更新tab标题中的数量
                self.update_tab_counts()
                
                # 如果有搜索条件，重新应用搜索
                if hasattr(self, 'checklist_search_input') and self.checklist_search_input.text().strip():
                    self.filter_checklist()
                
                QMessageBox.information(self, "成功", "清单项已更新！")
    
    def delete_checklist_item(self, item):
        """删除清单项"""
        item_data = item.data(Qt.UserRole)
        if item_data:
            reply = QMessageBox.question(self, "确认删除", 
                                       f"确定要删除清单项：\n{item_data.get('text', '')}？",
                                       QMessageBox.Yes | QMessageBox.No,
                                       QMessageBox.No)
            
            if reply == QMessageBox.Yes:
                # 从项目数据中删除清单项
                checklist_items = self.project.get('checklist_items', [])
                deleted_item_text = item_data.get('text', '')
                for i, checklist_item in enumerate(checklist_items):
                    if checklist_item.get('id') == item_data.get('id'):
                        del checklist_items[i]
                        break
                
                # 记录项目日志
                self.parent().add_project_log(self.project['name'], "删除清单项", 
                                             f"删除了清单项：{deleted_item_text}", 
                                             "清单")
                
                # 保存项目数据
                self.save_project_data()
                
                # 刷新显示
                self.load_checklist_items()
                # 更新tab标题中的数量
                self.update_tab_counts()
                
                # 如果有搜索条件，重新应用搜索
                if hasattr(self, 'checklist_search_input') and self.checklist_search_input.text().strip():
                    self.filter_checklist()
                
                QMessageBox.information(self, "成功", "清单项已删除！")
    
    def toggle_checklist_item(self, item):
        """切换清单项的完成状态"""
        item_data = item.data(Qt.UserRole)
        if item_data:
            # 确保清单项有id字段，如果没有则生成一个
            if 'id' not in item_data or not item_data['id']:
                item_data['id'] = f"checklist_{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}"
            
            # 切换完成状态
            item_data['completed'] = not item_data.get('completed', False)
            
            # 如果标记为已完成，记录完成时间
            if item_data['completed']:
                item_data['completed_time'] = datetime.now().isoformat()
            else:
                # 如果取消完成，移除完成时间
                if 'completed_time' in item_data:
                    del item_data['completed_time']
            
            # 在项目数据中找到并更新对应的清单项
            checklist_items = self.project.get('checklist_items', [])
            item_found = False
            for i, checklist_item in enumerate(checklist_items):
                # 确保项目数据中的清单项也有id字段
                if 'id' not in checklist_item or not checklist_item['id']:
                    checklist_item['id'] = f"checklist_{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}_{i}"
                
                if checklist_item.get('id') == item_data.get('id'):
                    checklist_items[i] = item_data
                    item_found = True
                    break
            
            # 如果没有找到对应的清单项，可能是数据不一致，尝试按文本内容匹配
            if not item_found:
                for i, checklist_item in enumerate(checklist_items):
                    if checklist_item.get('text') == item_data.get('text'):
                        # 更新找到的项目
                        checklist_items[i] = item_data
                        item_found = True
                        break
            
            # 如果还是没找到，添加为新项目
            if not item_found:
                checklist_items.append(item_data)
            
            # 记录项目日志
            status_text = "完成" if item_data['completed'] else "取消完成"
            self.parent().add_project_log(self.project['name'], f"{status_text}清单项", 
                                         f"{status_text}了清单项：{item_data.get('text', '')}", 
                                         "清单")
            
            # 保存项目数据
            self.save_project_data()
            
            # 刷新显示
            self.load_checklist_items()
    
    # 自定义清单项小部件
    class ChecklistItemWidget(QWidget):
        def __init__(self, item_data, parent=None, index=None):
            super().__init__(parent)
            self.item_data = item_data
            self.parent_tool = parent
            self.index = index or 1
            self.setup_ui()
            
        def setup_ui(self):
            # 主布局
            layout = QVBoxLayout(self)
            layout.setContentsMargins(10, 12, 10, 12)  # 增加内边距
            layout.setSpacing(8)  # 增加间距
            
            # 顶部布局（文本和完成按钮）
            top_layout = QHBoxLayout()
            top_layout.setSpacing(15)  # 增加文本和按钮之间的间距
            top_layout.setContentsMargins(0, 0, 0, 5)  # 底部增加一点间距
            
            # 清单项文本
            text = self.item_data.get('text', '')
            completed = self.item_data.get('completed', False)
            
            # 文本标签（包含序号）
            display_text = f"<span style='color: #2196F3; font-weight: bold;'>#{self.index}</span> {text}"
            self.text_label = QLabel(display_text)
            self.text_label.setWordWrap(True)
            font = self.text_label.font()
            font.setPointSize(11)  # 更大的字体
            font.setFamily("Arial")  # 使用与按钮相同的字体
            if completed:
                font.setStrikeOut(True)
                self.text_label.setStyleSheet("color: #888888;")  # 已完成项目的颜色
            else:
                self.text_label.setStyleSheet("color: #333333; font-weight: 500;")  # 未完成项目的颜色和粗细
            self.text_label.setFont(font)
            
            # 完成按钮
            self.complete_btn = QPushButton("✓ 完成" if not completed else "⟲ 取消完成")
            self.complete_btn.setFixedSize(140, 40)  # 更大的按钮
            self.complete_btn.setCursor(Qt.PointingHandCursor)
            self.complete_btn.setFont(QFont("Arial", 11, QFont.Bold))  # 更大更粗的字体
            
            # 设置按钮样式
            if not completed:
                self.complete_btn.setStyleSheet("""
                    QPushButton {
                        background-color: #4CAF50;
                        color: white;
                        border: none;
                        border-radius: 8px;
                        padding: 10px 15px;
                        font-weight: bold;
                        box-shadow: 0 3px 6px rgba(0,0,0,0.2);
                        letter-spacing: 1px;
                    }
                    QPushButton:hover {
                        background-color: #45a049;
                        box-shadow: 0 4px 8px rgba(0,0,0,0.3);
                        transform: translateY(-1px);
                    }
                    QPushButton:pressed {
                        background-color: #3d8b40;
                        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
                        transform: translateY(1px);
                    }
                """)
            else:
                self.complete_btn.setStyleSheet("""
                    QPushButton {
                        background-color: #FF9800;
                        color: white;
                        border: none;
                        border-radius: 8px;
                        padding: 10px 15px;
                        font-weight: bold;
                        box-shadow: 0 3px 6px rgba(0,0,0,0.2);
                        letter-spacing: 1px;
                    }
                    QPushButton:hover {
                        background-color: #F57C00;
                        box-shadow: 0 4px 8px rgba(0,0,0,0.3);
                        transform: translateY(-1px);
                    }
                    QPushButton:pressed {
                        background-color: #EF6C00;
                        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
                        transform: translateY(1px);
                    }
                """)
            
            # 连接按钮点击事件
            self.complete_btn.clicked.connect(self.toggle_complete)
            
            # 编辑按钮
            self.edit_btn = QPushButton("✏️ 编辑")
            self.edit_btn.setFixedSize(80, 40)
            self.edit_btn.setCursor(Qt.PointingHandCursor)
            self.edit_btn.setFont(QFont("Arial", 10, QFont.Bold))
            self.edit_btn.setStyleSheet("""
                QPushButton {
                    background-color: #2196F3;
                    color: white;
                    border: none;
                    border-radius: 6px;
                    padding: 8px 12px;
                    font-weight: bold;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.2);
                }
                QPushButton:hover {
                    background-color: #1976D2;
                    box-shadow: 0 3px 6px rgba(0,0,0,0.3);
                }
                QPushButton:pressed {
                    background-color: #1565C0;
                    box-shadow: 0 1px 2px rgba(0,0,0,0.2);
                }
            """)
            self.edit_btn.clicked.connect(self.edit_item)
            
            # 删除按钮
            self.delete_btn = QPushButton("🗑️ 删除")
            self.delete_btn.setFixedSize(80, 40)
            self.delete_btn.setCursor(Qt.PointingHandCursor)
            self.delete_btn.setFont(QFont("Arial", 10, QFont.Bold))
            self.delete_btn.setStyleSheet("""
                QPushButton {
                    background-color: #F44336;
                    color: white;
                    border: none;
                    border-radius: 6px;
                    padding: 8px 12px;
                    font-weight: bold;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.2);
                }
                QPushButton:hover {
                    background-color: #D32F2F;
                    box-shadow: 0 3px 6px rgba(0,0,0,0.3);
                }
                QPushButton:pressed {
                    background-color: #C62828;
                    box-shadow: 0 1px 2px rgba(0,0,0,0.2);
                }
            """)
            self.delete_btn.clicked.connect(self.delete_item)
            
            # 添加到顶部布局
            top_layout.addWidget(self.text_label, 1)  # 1表示拉伸因子
            top_layout.addWidget(self.edit_btn, 0)  # 0表示不拉伸
            top_layout.addWidget(self.delete_btn, 0)  # 0表示不拉伸
            top_layout.addWidget(self.complete_btn, 0)  # 0表示不拉伸
            
            # 时间信息布局
            time_layout = QVBoxLayout()
            time_layout.setSpacing(4)  # 增加时间标签之间的间距
            time_layout.setContentsMargins(2, 0, 0, 0)  # 左侧增加一点内边距
            
            # 创建时间
            timestamp = self.item_data.get('timestamp', '')
            if timestamp:
                try:
                    dt = datetime.fromisoformat(timestamp)
                    time_str = dt.strftime('%Y-%m-%d %H:%M:%S')
                except:
                    time_str = timestamp
            else:
                time_str = '未知时间'
            
            self.create_time_label = QLabel(f"🕒 创建时间: {time_str}")
            self.create_time_label.setStyleSheet("color: #666666; font-size: 9pt; padding-left: 2px;")
            self.create_time_label.setFont(QFont("Arial", 9))
            time_layout.addWidget(self.create_time_label)
            
            # 如果已完成，显示完成时间
            if completed:
                completed_time = self.item_data.get('completed_time', '')
                if completed_time:
                    try:
                        dt = datetime.fromisoformat(completed_time)
                        completed_time_str = dt.strftime('%Y-%m-%d %H:%M:%S')
                    except:
                        completed_time_str = completed_time
                else:
                    completed_time_str = '未知时间'
                
                self.complete_time_label = QLabel(f"✓ 完成时间: {completed_time_str}")
                self.complete_time_label.setStyleSheet("color: #4CAF50; font-size: 9pt; padding-left: 2px; font-weight: 500;")
                self.complete_time_label.setFont(QFont("Arial", 9))
                time_layout.addWidget(self.complete_time_label)
            
            # 添加所有布局
            layout.addLayout(top_layout)
            layout.addLayout(time_layout)
            
            # 设置背景和边框
            self.setStyleSheet("""
                QWidget {
                    background-color: white;
                    border: 1px solid #ddd;
                    border-radius: 8px;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.05);
                    padding: 2px;
                }
            """)
        
        def toggle_complete(self):
            # 获取列表项
            list_widget = self.parent_tool.checklist_list
            for i in range(list_widget.count()):
                item = list_widget.item(i)
                widget = list_widget.itemWidget(item)
                if widget == self:
                    # 调用父工具的切换方法
                    self.parent_tool.toggle_checklist_item(item)
                    break
        
        def edit_item(self):
            # 获取列表项
            list_widget = self.parent_tool.checklist_list
            for i in range(list_widget.count()):
                item = list_widget.item(i)
                widget = list_widget.itemWidget(item)
                if widget == self:
                    # 调用父工具的编辑方法
                    self.parent_tool.edit_checklist_item(item)
                    break
        
        def delete_item(self):
            # 获取列表项
            list_widget = self.parent_tool.checklist_list
            for i in range(list_widget.count()):
                item = list_widget.item(i)
                widget = list_widget.itemWidget(item)
                if widget == self:
                    # 调用父工具的删除方法
                    self.parent_tool.delete_checklist_item(item)
                    break
    
    def load_checklist_items(self):
        """加载项目清单项"""
        try:
            self.checklist_list.clear()
            
            # 从项目数据中加载清单项
            checklist_items = self.project.get('checklist_items', [])
            
            # 确保所有清单项都有id字段
            data_updated = False
            for i, item in enumerate(checklist_items):
                if 'id' not in item or not item['id']:
                    item['id'] = f"checklist_{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}_{i}"
                    data_updated = True
            
            # 如果有数据更新，保存项目数据
            if data_updated:
                self.save_project_data()
            
            # 按时间正序排列（最旧的在前，最新的在后）
            checklist_items.sort(key=lambda x: x.get('timestamp', ''), reverse=False)
            
            # 存储所有清单项数据以便搜索
            self.all_checklist_items = checklist_items
            
            for index, item in enumerate(checklist_items, 1):
                self.add_checklist_item_to_list(item, index)
                
        except Exception as e:
            QMessageBox.warning(self, "警告", f"加载清单项失败: {str(e)}")
    
    def add_checklist_item_to_list(self, item, index):
        """将清单项添加到列表中显示"""
        try:
            # 创建列表项
            list_item = QListWidgetItem()
            list_item.setData(Qt.UserRole, item)  # 存储完整的清单项数据
            
            # 创建自定义小部件，传入序号
            item_widget = self.ChecklistItemWidget(item, self, index)
            
            # 设置列表项大小
            list_item.setSizeHint(item_widget.sizeHint())
            
            # 添加到列表并设置小部件
            self.checklist_list.addItem(list_item)
            self.checklist_list.setItemWidget(list_item, item_widget)
            
        except Exception as e:
            logging.error(f"添加清单项到列表失败: {e}")
    
    def load_notes_timeline(self):
        """加载项目笔记时间轴"""
        try:
            self.notes_list.clear()
            
            # 从项目数据中加载笔记时间轴
            notes_timeline = self.project.get('notes_timeline', [])
            
            # 移除自动迁移逻辑，避免创建不必要的迁移笔记
            # if not notes_timeline:
            #     # 如果没有时间轴数据，尝试从旧的笔记文件迁移
            #     self.migrate_old_notes_to_timeline()
            #     notes_timeline = self.project.get('notes_timeline', [])
            
            # 按时间倒序排列（最新的在前）
            notes_timeline.sort(key=lambda x: x.get('timestamp', ''), reverse=True)
            
            # 存储所有笔记数据以便搜索
            self.all_notes = notes_timeline
            
            for index, note in enumerate(notes_timeline, 1):
                self.add_note_to_list(note, index)

                
        except Exception as e:
            QMessageBox.warning(self, "警告", f"加载笔记时间轴失败: {str(e)}")
    
    def filter_notes(self):
        """根据搜索关键词过滤笔记"""
        try:
            search_text = self.notes_search_input.text().strip().lower()
            self.notes_list.clear()
            
            if not search_text:
                # 如果搜索框为空，显示所有笔记
                for index, note in enumerate(self.all_notes, 1):
                    self.add_note_to_list(note, index)
            else:
                # 根据关键词过滤笔记
                filtered_notes = []
                for note in self.all_notes:
                    title = note.get('title', '').lower()
                    content = note.get('content', '').lower()
                    
                    # 检查标题或内容是否包含搜索关键词
                    if search_text in title or search_text in content:
                        filtered_notes.append(note)
                
                # 显示过滤后的笔记
                for index, note in enumerate(filtered_notes, 1):
                    self.add_note_to_list(note, index)
                    
        except Exception as e:
            logging.error(f"过滤笔记失败: {e}")
    
    def clear_notes_search(self):
        """清除笔记搜索"""
        self.notes_search_input.clear()
        self.filter_notes()  # 重新显示所有笔记
    
    def filter_checklist(self):
        """根据搜索关键词过滤清单项"""
        try:
            search_text = self.checklist_search_input.text().strip().lower()
            self.checklist_list.clear()
            
            if not search_text:
                # 如果搜索框为空，显示所有清单项
                for index, item in enumerate(self.all_checklist_items, 1):
                    self.add_checklist_item_to_list(item, index)
            else:
                # 根据关键词过滤清单项
                filtered_items = []
                for item in self.all_checklist_items:
                    text = item.get('text', '').lower()
                    
                    # 检查清单项文本是否包含搜索关键词
                    if search_text in text:
                        filtered_items.append(item)
                
                # 显示过滤后的清单项
                for index, item in enumerate(filtered_items, 1):
                    self.add_checklist_item_to_list(item, index)
                    
        except Exception as e:
            logging.error(f"过滤清单项失败: {e}")
    
    def clear_checklist_search(self):
        """清除清单项搜索"""
        self.checklist_search_input.clear()
        self.filter_checklist()  # 重新显示所有清单项
    
    def migrate_old_notes_to_timeline(self):
        """将旧的笔记文件迁移到时间轴格式"""
        try:
            folder_path = self.project.get('folder_path', '')
            if not folder_path or not os.path.exists(folder_path):
                return
            
            project_name = self.project['name']
            safe_name = "".join(c for c in project_name if c.isalnum() or c in (' ', '-', '_', '（', '）', '(', ')')).strip()
            if not safe_name:
                safe_name = "新项目"
            
            notes_file = os.path.join(folder_path, f"{safe_name}_笔记.md")
            
            if os.path.exists(notes_file):
                with open(notes_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # 解析旧笔记内容
                lines = content.split('\n')
                notes_content = []
                in_notes_section = False
                
                for line in lines:
                    if line.strip() == "## 项目笔记":
                        in_notes_section = True
                        continue
                    elif line.startswith("## ") and in_notes_section:
                        break
                    elif in_notes_section and line.strip():
                        notes_content.append(line)
                
                # 如果有内容，创建一个迁移笔记
                if notes_content:
                    migrated_content = '\n'.join(notes_content).strip()
                    if migrated_content:
                        migration_note = {
                            'id': f"migrated_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
                            'content': migrated_content,
                            'timestamp': datetime.now().isoformat(),
                            'title': '迁移的笔记内容'
                        }
                        
                        if 'notes_timeline' not in self.project:
                            self.project['notes_timeline'] = []
                        self.project['notes_timeline'].append(migration_note)
                        
                        # 保存项目数据
                        self.save_project_data()
                
        except Exception as e:
            logging.error(f"迁移旧笔记失败: {e}")
    
    def add_note_to_list(self, note, index=None):
        """将笔记添加到列表中显示"""
        try:
            # 格式化时间显示
            timestamp = note.get('timestamp', '')
            if timestamp:
                try:
                    dt = datetime.fromisoformat(timestamp)
                    time_str = dt.strftime('%Y-%m-%d %H:%M:%S')
                except:
                    time_str = timestamp
            else:
                time_str = '未知时间'
            
            # 获取笔记标题和内容预览
            title = note.get('title', '无标题')
            content = note.get('content', '')
            
            # 完整显示内容，保留换行符以便更好地展示格式
            formatted_content = content.replace('\n\n', '\n').replace('\n\n', '\n')  # 减少过多的空行
            
            # 获取序号
            if index is None:
                # 如果没有传入序号，则计算当前列表中的项目数量+1
                index = self.notes_list.count() + 1
            
            # 创建显示文本，使用HTML格式让标题加粗
            display_text = f"#{index} 📝 <b>{title}</b>\n🕒 {time_str}\n💬 {formatted_content}"
            
            # 创建列表项
            item = QListWidgetItem()
            item.setData(Qt.UserRole, note)  # 存储完整的笔记数据
            
            # 创建自定义widget来显示富文本
            widget = QWidget()
            layout = QVBoxLayout(widget)
            layout.setContentsMargins(12, 10, 12, 10)
            layout.setSpacing(6)
            
            # 标题标签（加粗，包含序号）
            title_label = QLabel(f"<span style='color: #2196F3; font-weight: bold;'>#{index}</span> 📝 <b>{title}</b>")
            title_label.setStyleSheet("font-size: 15px; color: #333; padding: 4px 0px; line-height: 1.4;")
            title_label.setWordWrap(True)  # 启用自动换行
            title_label.setMinimumHeight(26)  # 设置最小高度
            title_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
            layout.addWidget(title_label)
            
            # 时间标签
            time_label = QLabel(f"🕒 {time_str}")
            time_label.setStyleSheet("font-size: 14px; color: #666; padding: 2px 0px; line-height: 1.3;")
            time_label.setMinimumHeight(20)  # 设置最小高度
            layout.addWidget(time_label)
            
            # 内容标签
            content_label = QLabel(f"💬 {formatted_content}")
            content_label.setStyleSheet("font-size: 14px; color: #333; padding: 4px 0px; line-height: 1.4;")
            content_label.setWordWrap(True)
            content_label.setMinimumHeight(22)  # 设置最小高度
            content_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
            layout.addWidget(content_label)
            
            # 设置widget的大小策略
            widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
            
            # 强制widget重新计算大小
            widget.adjustSize()
            
            # 设置item大小，确保有足够的高度
            size_hint = widget.sizeHint()
            # 计算更合理的最小高度：基础高度 + 内容行数估算
            content_lines = max(1, len(formatted_content.split('\n')))
            title_lines = max(1, len(title) // 30 + 1)  # 估算标题行数
            estimated_height = 60 + (content_lines * 18) + (title_lines * 20)
            min_height = max(size_hint.height(), estimated_height, 90)
            item.setSizeHint(QSize(size_hint.width(), min_height))
            
            self.notes_list.addItem(item)
            self.notes_list.setItemWidget(item, widget)
            
        except Exception as e:
            logging.error(f"添加笔记到列表失败: {e}")
    
    def add_new_note(self):
        """添加新笔记"""
        dialog = NoteEditDialog(self, project=self.project)
        if dialog.exec_() == QDialog.Accepted:
            note_data = dialog.get_note_data()
            if note_data['content'].strip():  # 确保内容不为空
                # 创建新笔记
                new_note = {
                    'id': f"note_{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}",
                    'title': note_data['title'] or '无标题',
                    'content': note_data['content'],
                    'timestamp': note_data['timestamp']
                }
                
                # 添加到项目数据
                if 'notes_timeline' not in self.project:
                    self.project['notes_timeline'] = []
                self.project['notes_timeline'].append(new_note)
                
                # 记录项目日志
                self.parent().add_project_log(self.project['name'], "添加笔记", 
                                             f"添加了新笔记：{new_note['title']}", 
                                             "笔记")
                
                # 保存项目数据
                self.save_project_data()
                
                # 同时保存主工具的项目数据
                if hasattr(self, 'parent_tool') and self.parent_tool:
                    self.parent_tool.save_data()
                
                # 刷新显示
                self.load_notes_timeline()
                # 更新tab标题中的数量
                self.update_tab_counts()
                
                # 如果有搜索条件，重新应用搜索
                if hasattr(self, 'notes_search_input') and self.notes_search_input.text().strip():
                    self.filter_notes()
                
                QMessageBox.information(self, "成功", "笔记已添加！")
    
    def import_notes_file(self):
        """导入笔记文件，智能识别并分别导入笔记、清单、日志"""
        from PyQt5.QtWidgets import QFileDialog
        
        # 选择要导入的文件
        file_path, _ = QFileDialog.getOpenFileName(
            self, 
            "选择要导入的笔记文件", 
            "", 
            "文本文件 (*.txt *.md *.markdown);;所有文件 (*.*)"
        )
        
        if not file_path:
            return
        
        try:
            # 读取文件内容
            content = self._read_file_with_encoding(file_path)
            
            if not content.strip():
                QMessageBox.warning(self, "警告", "选择的文件内容为空！")
                return
            
            # 获取文件名
            import os
            file_name = os.path.basename(file_path)
            title = os.path.splitext(file_name)[0]
            
            # 智能解析文件内容
            import_result = self._parse_import_content(content, title)
            
            # 导入解析的内容
            self._import_parsed_content(import_result, title)
            
            # 保存项目数据
            self.save_project_data()
            
            # 同时保存主工具的项目数据
            if hasattr(self, 'parent_tool') and self.parent_tool:
                self.parent_tool.save_data()
            
            # 刷新显示
            self._refresh_all_tabs()
            
            # 显示导入结果
            self._show_import_result(import_result, file_name)
            
        except Exception as e:
            QMessageBox.critical(self, "错误", f"导入笔记文件失败：{str(e)}")
    
    def _notes_drag_enter_event(self, event):
        """处理拖拽进入事件"""
        if event.mimeData().hasUrls():
            # 检查是否为支持的文件类型
            urls = event.mimeData().urls()
            if urls:
                file_path = urls[0].toLocalFile()
                if file_path.lower().endswith(('.txt', '.md', '.markdown')):
                    event.acceptProposedAction()
                    return
        event.ignore()
    
    def _notes_drag_move_event(self, event):
        """处理拖拽移动事件"""
        if event.mimeData().hasUrls():
            urls = event.mimeData().urls()
            if urls:
                file_path = urls[0].toLocalFile()
                if file_path.lower().endswith(('.txt', '.md', '.markdown')):
                    event.acceptProposedAction()
                    return
        event.ignore()
    
    def _notes_drop_event(self, event):
        """处理拖拽放下事件"""
        if event.mimeData().hasUrls():
            urls = event.mimeData().urls()
            if urls:
                file_path = urls[0].toLocalFile()
                if file_path.lower().endswith(('.txt', '.md', '.markdown')):
                    try:
                        # 读取文件内容
                        content = self._read_file_with_encoding(file_path)
                        
                        if not content.strip():
                            QMessageBox.warning(self, "警告", "拖拽的文件内容为空！")
                            return
                        
                        # 获取文件名
                        import os
                        file_name = os.path.basename(file_path)
                        title = os.path.splitext(file_name)[0]
                        
                        # 智能解析文件内容
                        import_result = self._parse_import_content(content, title)
                        
                        # 导入解析的内容
                        self._import_parsed_content(import_result, title)
                        
                        # 保存项目数据
                        self.save_project_data()
                        
                        # 同时保存主工具的项目数据
                        if hasattr(self, 'parent_tool') and self.parent_tool:
                            self.parent_tool.save_data()
                        
                        # 刷新显示
                        self._refresh_all_tabs()
                        
                        # 显示导入结果
                        self._show_import_result(import_result, file_name)
                        
                        event.acceptProposedAction()
                        
                    except Exception as e:
                        QMessageBox.critical(self, "错误", f"拖拽导入文件失败：{str(e)}")
                        event.ignore()
                else:
                    QMessageBox.warning(self, "警告", "只支持拖拽 .txt、.md、.markdown 格式的文件！")
                    event.ignore()
        else:
            event.ignore()
    
    def _read_file_with_encoding(self, file_path):
        """尝试不同编码读取文件"""
        encodings = ['utf-8', 'gbk', 'gb2312', 'utf-16']
        
        for encoding in encodings:
            try:
                with open(file_path, 'r', encoding=encoding) as f:
                    return f.read()
            except UnicodeDecodeError:
                continue
        
        # 如果所有编码都失败，抛出异常
        raise UnicodeDecodeError("无法识别文件编码")
    
    def _parse_import_content(self, content, title):
        """智能解析导入内容，识别笔记、清单、日志"""
        import re
        
        result = {
            'notes': [],
            'checklist': [],
            'logs': [],
            'plain_content': ''
        }
        
        # 检查是否为markdown格式的项目文件
        if self._is_project_markdown(content):
            # 解析项目markdown文件
            notes, checklist = self.parse_markdown_content(content)
            result['notes'] = notes
            result['checklist'] = checklist
            
            # 解析日志部分
            logs = self._parse_logs_from_markdown(content)
            result['logs'] = logs
        else:
            # 检查是否包含清单格式
            checklist_items = self._extract_checklist_items(content)
            if checklist_items:
                result['checklist'] = checklist_items
                # 移除清单内容，剩余作为笔记
                remaining_content = self._remove_checklist_from_content(content)
                if remaining_content.strip():
                    result['notes'] = [{
                        'id': f"note_{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}",
                        'title': f"导入：{title}",
                        'content': remaining_content.strip(),
                        'timestamp': datetime.now().isoformat()
                    }]
            else:
                # 纯文本内容，作为笔记导入
                result['notes'] = [{
                    'id': f"note_{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}",
                    'title': f"导入：{title}",
                    'content': content.strip(),
                    'timestamp': datetime.now().isoformat()
                }]
        
        return result
    
    def _is_project_markdown(self, content):
        """检查是否为项目markdown文件格式"""
        return ('## 项目清单' in content or 
                '## 笔记时间轴' in content or 
                '## 项目日志' in content)
    
    def _extract_checklist_items(self, content):
        """从内容中提取清单项"""
        import re
        checklist_items = []
        
        # 匹配清单格式：- [ ] 或 - [x] 或 * [ ] 或 * [x]
        pattern = r'^[\s]*[-*]\s*\[([x\s])\]\s*(.+)$'
        
        for line in content.split('\n'):
            match = re.match(pattern, line, re.IGNORECASE)
            if match:
                completed = match.group(1).lower() == 'x'
                text = match.group(2).strip()
                
                checklist_item = {
                    'id': f"checklist_{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}",
                    'text': text,
                    'completed': completed,
                    'timestamp': datetime.now().isoformat()
                }
                
                if completed:
                    checklist_item['completed_time'] = datetime.now().isoformat()
                
                checklist_items.append(checklist_item)
        
        return checklist_items
    
    def _remove_checklist_from_content(self, content):
        """从内容中移除清单项，返回剩余内容"""
        import re
        lines = content.split('\n')
        remaining_lines = []
        
        pattern = r'^[\s]*[-*]\s*\[([x\s])\]\s*(.+)$'
        
        for line in lines:
            if not re.match(pattern, line, re.IGNORECASE):
                remaining_lines.append(line)
        
        return '\n'.join(remaining_lines)
    
    def _parse_logs_from_markdown(self, content):
        """从markdown内容中解析日志"""
        logs = []
        
        # 查找项目日志部分
        log_section_start = content.find("## 项目日志\n")
        if log_section_start != -1:
            log_section_start += len("## 项目日志\n")
            # 查找下一个二级标题或文件结尾
            next_section = content.find("\n## ", log_section_start)
            if next_section != -1:
                log_content = content[log_section_start:next_section].strip()
            else:
                log_content = content[log_section_start:].strip()
            
            if log_content and log_content != "暂无项目日志":
                # 将日志内容作为一个整体导入
                logs.append({
                    'content': log_content,
                    'timestamp': datetime.now().isoformat()
                })
        
        return logs
    
    def _import_parsed_content(self, import_result, title):
        """导入解析的内容到对应模块"""
        imported_count = {'notes': 0, 'checklist': 0, 'logs': 0}
        
        # 导入笔记
        if import_result['notes']:
            if 'notes_timeline' not in self.project:
                self.project['notes_timeline'] = []
            
            for note in import_result['notes']:
                self.project['notes_timeline'].append(note)
                imported_count['notes'] += 1
        
        # 导入清单
        if import_result['checklist']:
            if 'checklist_items' not in self.project:
                self.project['checklist_items'] = []
            
            for item in import_result['checklist']:
                self.project['checklist_items'].append(item)
                imported_count['checklist'] += 1
        
        # 导入日志（添加到项目日志文件中）
        if import_result['logs']:
            for log in import_result['logs']:
                self.parent().add_project_log(
                    self.project['name'], 
                    "导入日志", 
                    f"从文件导入日志内容：{title}", 
                    "导入"
                )
                imported_count['logs'] += 1
        
        # 记录导入操作日志
        total_imported = sum(imported_count.values())
        if total_imported > 0:
            self.parent().add_project_log(
                self.project['name'], 
                "导入文件", 
                f"从文件 {title} 导入了 {imported_count['notes']} 条笔记、{imported_count['checklist']} 个清单项、{imported_count['logs']} 条日志", 
                "导入"
            )
        
        return imported_count
    
    def _refresh_all_tabs(self):
        """刷新所有相关标签页"""
        # 刷新笔记
        self.load_notes_timeline()
        
        # 刷新清单
        if hasattr(self, 'load_checklist_items'):
            self.load_checklist_items()
        
        # 刷新日志
        if hasattr(self, 'load_project_logs'):
            self.load_project_logs()
        
        # 更新tab标题中的数量
        self.update_tab_counts()
        
        # 如果有搜索条件，重新应用搜索
        if hasattr(self, 'notes_search_input') and self.notes_search_input.text().strip():
            self.filter_notes()
    
    def _show_import_result(self, import_result, file_name):
        """显示导入结果"""
        notes_count = len(import_result['notes'])
        checklist_count = len(import_result['checklist'])
        logs_count = len(import_result['logs'])
        
        result_msg = f"文件 {file_name} 导入完成！\n\n"
        result_msg += f"📝 导入笔记：{notes_count} 条\n"
        result_msg += f"✅ 导入清单：{checklist_count} 项\n"
        result_msg += f"📋 导入日志：{logs_count} 条\n\n"
        
        if notes_count + checklist_count + logs_count == 0:
            result_msg += "未识别到有效的笔记、清单或日志内容。"
        else:
            result_msg += "所有内容已按类型分别导入到对应模块中。"
        
        QMessageBox.information(self, "导入完成", result_msg)
    
    def edit_note_item(self, item):
        """编辑笔记项"""
        note_data = item.data(Qt.UserRole)
        if note_data:
            dialog = NoteEditDialog(self, note_data, self.project)
            if dialog.exec_() == QDialog.Accepted:
                updated_data = dialog.get_note_data()
                
                # 更新笔记数据
                note_data['title'] = updated_data['title'] or '无标题'
                note_data['content'] = updated_data['content']
                note_data['timestamp'] = updated_data['timestamp']
                
                # 在项目数据中找到并更新对应的笔记
                notes_timeline = self.project.get('notes_timeline', [])
                for i, note in enumerate(notes_timeline):
                    if note.get('id') == note_data.get('id'):
                        notes_timeline[i] = note_data
                        break
                
                # 记录项目日志
                self.parent().add_project_log(self.project['name'], "编辑笔记", 
                                             f"编辑了笔记：{updated_data['title']}", 
                                             "笔记")
                
                # 保存项目数据
                self.save_project_data()
                
                # 同时保存主工具的项目数据
                if hasattr(self, 'parent_tool') and self.parent_tool:
                    self.parent_tool.save_data()
                
                # 刷新显示
                self.load_notes_timeline()
                # 更新tab标题中的数量
                self.update_tab_counts()
                
                # 如果有搜索条件，重新应用搜索
                if hasattr(self, 'notes_search_input') and self.notes_search_input.text().strip():
                    self.filter_notes()
                
                QMessageBox.information(self, "成功", "笔记已更新！")
    
    def show_notes_context_menu(self, position):
        """显示笔记列表右键菜单"""
        item = self.notes_list.itemAt(position)
        if item:
            menu = QMenu(self)
            
            # 编辑笔记
            edit_action = menu.addAction("✏️ 编辑笔记")
            edit_action.triggered.connect(lambda: self.edit_note_item(item))
            
            # 删除笔记
            delete_action = menu.addAction("🗑️ 删除笔记")
            delete_action.triggered.connect(lambda: self.delete_note(item))
            
            menu.exec_(self.notes_list.mapToGlobal(position))
    
    def delete_note(self, item):
        """删除笔记"""
        note_data = item.data(Qt.UserRole)
        if note_data:
            title = note_data.get('title', '无标题')
            reply = QMessageBox.question(self, "确认删除", 
                                       f"确定要删除笔记 '{title}' 吗？",
                                       QMessageBox.Yes | QMessageBox.No)
            
            if reply == QMessageBox.Yes:
                # 从项目数据中删除笔记
                notes_timeline = self.project.get('notes_timeline', [])
                note_id = note_data.get('id')
                
                # 找到并删除对应的笔记
                deleted_note_title = None
                for i, note in enumerate(notes_timeline):
                    if note.get('id') == note_id:
                        deleted_note_title = note.get('title', '无标题')
                        del notes_timeline[i]
                        break
                
                # 记录项目日志
                if deleted_note_title:
                    self.parent().add_project_log(self.project['name'], "删除笔记", 
                                                 f"删除了笔记：{deleted_note_title}", 
                                                 "笔记")
                
                # 保存项目数据
                self.save_project_data()
                
                # 同时保存主工具的项目数据
                if hasattr(self, 'parent_tool') and self.parent_tool:
                    self.parent_tool.save_data()
                
                # 刷新显示
                self.load_notes_timeline()
                # 更新tab标题中的数量
                self.update_tab_counts()
                
                # 如果有搜索条件，重新应用搜索
                if hasattr(self, 'notes_search_input') and self.notes_search_input.text().strip():
                    self.filter_notes()
                
                QMessageBox.information(self, "成功", "笔记已删除！")



    
    def save_to_markdown_file(self):
        """保存项目数据到markdown文件"""
        try:
            folder_path = self.project.get('folder_path', '')
            if not folder_path or not os.path.exists(folder_path):
                return False
            
            project_name = self.project['name']
            safe_name = "".join(c for c in project_name if c.isalnum() or c in (' ', '-', '_', '（', '）', '(', ')')).strip()
            if not safe_name:
                safe_name = "新项目"
            
            notes_file = os.path.join(folder_path, f"{safe_name}_笔记.md")
            
            # 构建完整的markdown内容
            content = self.build_markdown_content()
            
            # 保存文件
            with open(notes_file, 'w', encoding='utf-8') as f:
                f.write(content)
            
            # 将笔记文件添加到项目资源中（如果还没有的话）
            self.add_notes_to_resources(notes_file)
            
            return True
            
        except Exception as e:
            print(f"保存markdown文件失败: {e}")
            return False
    
    def save_notes_to_file(self):
        """将笔记时间轴保存到文件（兼容性方法）"""
        try:
            if self.save_to_markdown_file():
                QMessageBox.information(self, "成功", "项目笔记已保存到文件！")
            else:
                QMessageBox.warning(self, "警告", "项目文件夹不存在，无法保存笔记。")
        except Exception as e:
            QMessageBox.critical(self, "错误", f"保存笔记失败: {str(e)}")
    
    def build_markdown_content(self):
        """构建markdown内容"""
        project_name = self.project['name']
        content = f"# {project_name} 项目笔记\n\n"
        content += f"**最后更新：** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        
        # 项目概述
        content += "## 项目概述\n\n"
        content += f"**项目描述：** {self.project.get('description', '暂无描述')}\n"
        content += f"**项目类型：** {self.project.get('type', '其他')}\n"
        
        tags = self.project.get('tags', [])
        if tags:
            content += f"**项目标签：** {', '.join(tags)}\n"
        
        content += f"**创建时间：** {self.project.get('created_time', '未知')}\n"
        content += f"**修改时间：** {self.project.get('modified_time', '未知')}\n\n"
        
        # 项目清单
        content += "## 项目清单\n\n"
        checklist_items = self.project.get('checklist_items', [])
        if checklist_items:
            # 按时间排序（最新的在前）
            sorted_items = sorted(checklist_items, key=lambda x: x.get('timestamp', ''), reverse=True)
            for item in sorted_items:
                text = item.get('text', '')
                completed = item.get('completed', False)
                timestamp = item.get('timestamp', '')
                
                if timestamp:
                    try:
                        dt = datetime.fromisoformat(timestamp)
                        time_str = dt.strftime('%Y-%m-%d %H:%M:%S')
                    except:
                        time_str = timestamp
                else:
                    time_str = '未知时间'
                
                if completed:
                    completed_time = item.get('completed_time', '')
                    if completed_time:
                        try:
                            dt = datetime.fromisoformat(completed_time)
                            completed_time_str = dt.strftime('%Y-%m-%d %H:%M:%S')
                        except:
                            completed_time_str = completed_time
                    else:
                        completed_time_str = '未知时间'
                    content += f"- [x] {text} (创建: {time_str}, 完成: {completed_time_str})\n"
                else:
                    content += f"- [ ] {text} (创建: {time_str})\n"
        else:
            content += "暂无清单项\n"
        
        content += "\n"
        
        # 笔记时间轴
        content += "## 笔记时间轴\n\n"
        notes_timeline = self.project.get('notes_timeline', [])
        if notes_timeline:
            # 按时间排序（最新的在前）
            sorted_notes = sorted(notes_timeline, key=lambda x: x.get('timestamp', ''), reverse=True)
            for note in sorted_notes:
                timestamp = note.get('timestamp', '')
                if timestamp:
                    try:
                        dt = datetime.fromisoformat(timestamp)
                        time_str = dt.strftime('%Y-%m-%d %H:%M:%S')
                    except:
                        time_str = timestamp
                else:
                    time_str = '未知时间'
                
                title = note.get('title', '无标题')
                note_content = note.get('content', '')
                
                content += f"### {title}\n\n"
                content += f"**时间：** {time_str}\n\n"
                content += f"{note_content}\n\n"
                content += "---\n\n"
        else:
            content += "暂无笔记内容\n\n"
        
        # 项目日志
        content += "## 项目日志\n\n"
        # 从现有的markdown文件中读取项目日志
        try:
            folder_path = self.project.get('folder_path', '')
            if folder_path and os.path.exists(folder_path):
                project_name = self.project['name']
                safe_name = "".join(c for c in project_name if c.isalnum() or c in (' ', '-', '_', '（', '）', '(', ')')).strip()
                if not safe_name:
                    safe_name = "新项目"
                notes_file = os.path.join(folder_path, f"{safe_name}_笔记.md")
                
                if os.path.exists(notes_file):
                    with open(notes_file, 'r', encoding='utf-8') as f:
                        existing_content = f.read()
                    
                    # 从现有内容中提取项目日志部分
                    log_section_start = existing_content.find("## 项目日志\n")
                    if log_section_start != -1:
                        log_section_start += len("## 项目日志\n")
                        # 查找下一个二级标题或文件结尾
                        next_section = existing_content.find("\n## ", log_section_start)
                        if next_section != -1:
                            log_content = existing_content[log_section_start:next_section].strip()
                        else:
                            log_content = existing_content[log_section_start:].strip()
                        
                        if log_content:
                            content += log_content + "\n"
                        else:
                            content += "暂无项目日志\n"
                    else:
                        content += "暂无项目日志\n"
                else:
                    content += "暂无项目日志\n"
            else:
                content += "暂无项目日志\n"
        except Exception as e:
            content += "暂无项目日志\n"
        
        content += "\n"
        
        # 项目进展
        content += "## 项目进展\n\n"
        content += "在这里记录项目的重要进展和里程碑...\n\n"
        
        return content
    
    def load_from_markdown_file(self):
        """从markdown文件加载项目数据"""
        try:
            folder_path = self.project.get('folder_path', '')
            if not folder_path or not os.path.exists(folder_path):
                return False
            
            project_name = self.project['name']
            safe_name = "".join(c for c in project_name if c.isalnum() or c in (' ', '-', '_', '（', '）', '(', ')')).strip()
            if not safe_name:
                safe_name = "新项目"
            
            notes_file = os.path.join(folder_path, f"{safe_name}_笔记.md")
            
            if not os.path.exists(notes_file):
                # 如果markdown文件不存在，初始化空的数据结构
                self.project['notes_timeline'] = []
                self.project['checklist_items'] = []
                return True
            
            # 读取markdown文件
            with open(notes_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 解析markdown内容
            notes_timeline, checklist_items = self.parse_markdown_content(content)
            
            # 更新项目数据
            self.project['notes_timeline'] = notes_timeline
            self.project['checklist_items'] = checklist_items
            
            return True
            
        except Exception as e:
            print(f"从markdown文件加载数据失败: {e}")
            # 初始化空的数据结构
            self.project['notes_timeline'] = []
            self.project['checklist_items'] = []
            return False
    
    def parse_markdown_content(self, content):
        """解析markdown内容，提取笔记和清单"""
        notes_timeline = []
        checklist_items = []
        
        lines = content.split('\n')
        current_section = None
        current_note = None
        current_note_content = []
        
        for line in lines:
            line = line.strip()
            
            # 检测章节
            if line.startswith('## 项目清单'):
                current_section = 'checklist'
                continue
            elif line.startswith('## 笔记时间轴'):
                current_section = 'notes'
                continue
            elif line.startswith('## '):
                current_section = None
                continue
            
            # 解析清单项
            if current_section == 'checklist' and (line.startswith('- [x]') or line.startswith('- [ ]')):
                completed = line.startswith('- [x]')
                text_part = line[5:].strip()  # 移除 "- [x] " 或 "- [ ] "
                
                # 提取时间信息
                import re
                time_pattern = r'\(创建: ([^,)]+)(?:, 完成: ([^)]+))?\)'
                match = re.search(time_pattern, text_part)
                
                if match:
                    text = text_part[:match.start()].strip()
                    created_time = match.group(1)
                    completed_time = match.group(2) if completed else None
                    
                    checklist_item = {
                        'id': f"checklist_{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}",
                        'text': text,
                        'completed': completed,
                        'timestamp': self.parse_time_string(created_time),
                    }
                    
                    if completed_time:
                        checklist_item['completed_time'] = self.parse_time_string(completed_time)
                    
                    checklist_items.append(checklist_item)
            
            # 解析笔记
            elif current_section == 'notes':
                if line.startswith('### '):
                    # 保存上一个笔记
                    if current_note:
                        current_note['content'] = '\n'.join(current_note_content).strip()
                        notes_timeline.append(current_note)
                    
                    # 开始新笔记
                    title = line[4:].strip()  # 移除 "### "
                    current_note = {
                        'id': f"note_{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}",
                        'title': title,
                        'content': '',
                        'timestamp': datetime.now().isoformat()
                    }
                    current_note_content = []
                    
                elif line.startswith('**时间：**'):
                    if current_note:
                        time_str = line.replace('**时间：**', '').strip()
                        current_note['timestamp'] = self.parse_time_string(time_str)
                        
                elif line == '---':
                    # 笔记结束
                    if current_note:
                        current_note['content'] = '\n'.join(current_note_content).strip()
                        notes_timeline.append(current_note)
                        current_note = None
                        current_note_content = []
                        
                elif current_note and line and not line.startswith('**时间：**'):
                    current_note_content.append(line)
        
        # 保存最后一个笔记
        if current_note:
            current_note['content'] = '\n'.join(current_note_content).strip()
            notes_timeline.append(current_note)
        
        return notes_timeline, checklist_items
    
    def parse_time_string(self, time_str):
        """解析时间字符串为ISO格式"""
        try:
            # 尝试解析 YYYY-MM-DD HH:MM:SS 格式
            dt = datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')
            return dt.isoformat()
        except:
            try:
                # 尝试解析其他格式
                dt = datetime.fromisoformat(time_str)
                return dt.isoformat()
            except:
                # 如果都失败，返回当前时间
                return datetime.now().isoformat()
    
    def add_notes_to_resources(self, notes_file):
        """将笔记文件添加到项目资源中"""
        try:
            # 检查是否已经存在
            resources = self.project.get('resources', [])
            for resource in resources:
                if resource.get('path') == notes_file:
                    return  # 已存在，不重复添加
            
            # 添加笔记资源
            note_resource = {
                'name': f"{self.project['name']}_笔记.md",
                'path': notes_file,
                'type': '项目笔记',
                'size': os.path.getsize(notes_file) if os.path.exists(notes_file) else 0,
                'modified_time': datetime.now().isoformat()
            }
            
            resources.append(note_resource)
            self.project['resources'] = resources
            
            # 更新父工具的项目数据
            if self.parent_tool:
                for i, project in enumerate(self.parent_tool.projects):
                    if project.get('id') == self.project.get('id'):
                        self.parent_tool.projects[i] = self.project
                        break
            
            # 刷新资源列表
            self.refresh_resources()
            
        except Exception as e:
            logging.error(f"添加笔记资源失败: {e}")
    
    def open_notes_file(self):
        """打开笔记文件"""
        try:
            folder_path = self.project.get('folder_path', '')
            if not folder_path or not os.path.exists(folder_path):
                QMessageBox.warning(self, "警告", "项目文件夹不存在。")
                return
            
            project_name = self.project['name']
            safe_name = "".join(c for c in project_name if c.isalnum() or c in (' ', '-', '_', '（', '）', '(', ')')).strip()
            if not safe_name:
                safe_name = "新项目"
            
            notes_file = os.path.join(folder_path, f"{safe_name}_笔记.md")
            
            # 如果文件不存在，先保存当前笔记到文件
            if not os.path.exists(notes_file):
                self.save_notes_to_file()
            
            if os.path.exists(notes_file):
                if sys.platform == "win32":
                    os.startfile(notes_file)
                elif sys.platform == "darwin":
                    subprocess.run(["open", notes_file])
                else:
                    subprocess.run(["xdg-open", notes_file])
            else:
                QMessageBox.warning(self, "警告", "笔记文件不存在。")
                
        except Exception as e:
            QMessageBox.critical(self, "错误", f"无法打开笔记文件: {str(e)}")
    
    def edit_project_path(self):
        """编辑项目文件夹路径"""
        try:
            current_path = self.project.get('folder_path', '')
            
            # 打开文件夹选择对话框
            new_path = QFileDialog.getExistingDirectory(
                self, 
                "选择项目文件夹", 
                current_path if current_path and os.path.exists(current_path) else os.path.expanduser("~")
            )
            
            if new_path:
                # 规范化新路径，统一使用系统默认的路径分隔符
                new_path = os.path.normpath(new_path)
                old_path = self.project.get('folder_path', '')
                
                # 如果新旧路径不同且旧路径存在，则需要迁移文件
                if old_path and os.path.exists(old_path) and old_path != new_path:
                    # 调用迁移方法将笔记文件从旧路径迁移到新路径
                    migrated_folder_path = self.parent_tool.migrate_project_notes(
                        self.project, self.project['name'], old_path, new_path
                    )
                    
                    if migrated_folder_path:
                        # 更新为实际迁移后的路径，并规范化
                        new_path = os.path.normpath(migrated_folder_path)
                        QMessageBox.information(self, "迁移成功", f"项目文件已从 '{old_path}' 迁移到 '{new_path}'")
                    else:
                        # 迁移失败，保持原路径
                        QMessageBox.warning(self, "迁移失败", "项目文件迁移失败，保持原路径")
                        return
                
                # 更新项目数据
                self.project['folder_path'] = new_path
                self.project['modified_time'] = datetime.now().isoformat()
                
                # 记录项目日志
                if self.parent_tool:
                    self.parent_tool.add_project_log(self.project['name'], "编辑项目路径", 
                                                    f"项目路径从 '{old_path}' 更新为 '{new_path}'", 
                                                    "操作")
                
                # 更新父工具中的项目数据
                if self.parent_tool:
                    for i, project in enumerate(self.parent_tool.projects):
                        if project['name'] == self.project['name']:
                            self.parent_tool.projects[i] = self.project
                            break
                    
                    # 保存数据
                    self.parent_tool.save_data()
                    
                    # 刷新项目表格
                    self.parent_tool.refresh_project_list()
                
                # 刷新当前对话框显示
                self.refresh_info_display()
                
                QMessageBox.information(self, "成功", f"项目路径已更新为:\n{new_path}")
                
        except Exception as e:
            QMessageBox.critical(self, "错误", f"更新项目路径失败: {str(e)}")
    
    def refresh_info_display(self):
        """刷新信息显示"""
        try:
            # 重新创建信息卡片
            new_info_card = self.create_info_card()
            
            # 找到左侧布局
            main_layout = self.layout()
            content_layout = None
            
            # 遍历主布局找到内容布局
            for i in range(main_layout.count()):
                item = main_layout.itemAt(i)
                if item and hasattr(item, 'layout') and item.layout():
                    layout = item.layout()
                    if isinstance(layout, QHBoxLayout):  # 内容区域是水平布局
                        content_layout = layout
                        break
            
            if content_layout:
                # 找到左侧widget
                left_widget = content_layout.itemAt(0).widget()
                if left_widget:
                    left_layout = left_widget.layout()
                    if left_layout and left_layout.count() > 0:
                        # 移除旧的信息卡片
                        old_card = left_layout.itemAt(0).widget()
                        if old_card:
                            left_layout.removeWidget(old_card)
                            old_card.deleteLater()
                        
                        # 添加新的信息卡片
                        left_layout.insertWidget(0, new_info_card)
            
        except Exception as e:
            print(f"刷新显示失败: {str(e)}")
    
    def open_folder(self, folder_path):
        """打开项目文件夹"""
        try:
            if os.path.exists(folder_path):
                if sys.platform == "win32":
                    os.startfile(folder_path)
                elif sys.platform == "darwin":
                    subprocess.run(["open", folder_path])
                else:
                    subprocess.run(["xdg-open", folder_path])
            else:
                QMessageBox.warning(self, "警告", f"文件夹不存在: {folder_path}")
        except Exception as e:
            QMessageBox.critical(self, "错误", f"无法打开文件夹: {str(e)}")
    
    def edit_project_path(self):
        """编辑项目文件夹路径"""
        try:
            current_path = self.project.get('folder_path', '')
            
            # 打开文件夹选择对话框
            new_path = QFileDialog.getExistingDirectory(
                self, 
                "选择项目文件夹", 
                current_path if current_path and os.path.exists(current_path) else os.path.expanduser("~")
            )
            
            if new_path:
                # 规范化新路径，统一使用系统默认的路径分隔符
                new_path = os.path.normpath(new_path)
                old_path = self.project.get('folder_path', '')
                
                # 如果新旧路径不同且旧路径存在，则需要迁移文件
                if old_path and os.path.exists(old_path) and old_path != new_path:
                    # 调用迁移方法将笔记文件从旧路径迁移到新路径
                    migrated_folder_path = self.parent_tool.migrate_project_notes(
                        self.project, self.project['name'], old_path, new_path
                    )
                    
                    if migrated_folder_path:
                        # 更新为实际迁移后的路径，并规范化
                        new_path = os.path.normpath(migrated_folder_path)
                        QMessageBox.information(self, "迁移成功", f"项目文件已从 '{old_path}' 迁移到 '{new_path}'")
                    else:
                        # 迁移失败，保持原路径
                        QMessageBox.warning(self, "迁移失败", "项目文件迁移失败，保持原路径")
                        return
                
                # 更新项目数据
                self.project['folder_path'] = new_path
                self.project['modified_time'] = datetime.now().isoformat()
                
                # 记录项目日志
                if self.parent_tool:
                    self.parent_tool.add_project_log(self.project['name'], "编辑项目路径", 
                                                    f"项目路径从 '{old_path}' 更新为 '{new_path}'", 
                                                    "操作")
                
                # 保存到父工具的数据中
                if self.parent_tool:
                    for i, project in enumerate(self.parent_tool.projects):
                        if project.get('name') == self.project.get('name'):
                            self.parent_tool.projects[i] = self.project
                            break
                    
                    # 保存数据到文件
                    self.parent_tool.save_data()
                    
                    # 刷新主界面
                    self.parent_tool.refresh_project_list()
                
                # 刷新当前对话框显示
                self.refresh_info_display()
                
                QMessageBox.information(self, "成功", f"项目路径已更新为:\n{new_path}")
                
        except Exception as e:
            QMessageBox.critical(self, "错误", f"更新项目路径失败: {str(e)}")
    
    def refresh_info_display(self):
          """刷新信息显示"""
          try:
              # 重新创建信息卡片
              new_info_card = self.create_info_card()
              
              # 找到并替换旧的信息卡片
              # 获取主布局
              main_layout = self.layout()
              if main_layout and main_layout.count() > 1:
                  # 获取内容布局（第二个项目）
                  content_layout = main_layout.itemAt(1).layout()
                  if content_layout and content_layout.count() > 0:
                      # 获取左侧widget
                      left_widget = content_layout.itemAt(0).widget()
                      if left_widget:
                          left_layout = left_widget.layout()
                          if left_layout and left_layout.count() > 0:
                              # 移除旧的信息卡片
                              old_card = left_layout.itemAt(0).widget()
                              if old_card:
                                  left_layout.removeWidget(old_card)
                                  old_card.deleteLater()
                              # 插入新的信息卡片
                              left_layout.insertWidget(0, new_info_card)
          except Exception as e:
              print(f"刷新显示失败: {str(e)}")
        
    def create_resource_card(self):
        """创建资源管理卡片"""
        card = ModernCard("项目资源")
        
        # 资源筛选和操作区域
        filter_layout = QHBoxLayout()
        
        # 搜索框
        search_label = QLabel("搜索:")
        search_label.setStyleSheet("font-weight: bold; color: #333;")
        
        self.search_edit = QLineEdit()
        self.search_edit.setPlaceholderText("输入关键词搜索资源...")
        self.search_edit.setStyleSheet("""
            QLineEdit {
                border: 1px solid #ddd;
                border-radius: 4px;
                padding: 5px 8px;
                font-size: 13px;
                background-color: white;
                min-width: 200px;
            }
            QLineEdit:focus {
                border: 2px solid #2196F3;
            }
        """)
        self.search_edit.textChanged.connect(self.on_search_text_changed)
        
        # 清除搜索按钮
        clear_search_btn = QPushButton("✕")
        clear_search_btn.setFixedSize(24, 24)
        clear_search_btn.setStyleSheet("""
            QPushButton {
                border: 1px solid #ddd;
                border-radius: 12px;
                background-color: #f5f5f5;
                color: #666;
                font-size: 12px;
            }
            QPushButton:hover {
                background-color: #e0e0e0;
                color: #333;
            }
        """)
        clear_search_btn.clicked.connect(self.clear_search)
        clear_search_btn.setToolTip("清除搜索")
        
        # 资源类型筛选
        filter_label = QLabel("筛选类型:")
        filter_label.setStyleSheet("font-weight: bold; color: #333;")
        
        self.type_filter_combo = QComboBox()
        self.type_filter_combo.addItem("全部类型")
        # 添加资源类型（参考资料、灵感火花、产出成品）
        if hasattr(self.parent_tool, 'resource_categories'):
            for category in self.parent_tool.resource_categories:
                self.type_filter_combo.addItem(category)
        
        self.type_filter_combo.setStyleSheet("""
            QComboBox {
                border: 1px solid #ddd;
                border-radius: 4px;
                padding: 5px 8px;
                font-size: 13px;
                background-color: white;
                min-width: 120px;
            }
            QComboBox::drop-down {
                border: none;
                width: 20px;
            }
            QComboBox::down-arrow {
                image: none;
                border-left: 3px solid transparent;
                border-right: 3px solid transparent;
                border-top: 3px solid #666;
                margin-right: 3px;
            }
            QComboBox QAbstractItemView {
                border: 1px solid #ddd;
                background-color: white;
                selection-background-color: #e3f2fd;
            }
        """)
        self.type_filter_combo.currentTextChanged.connect(self.on_type_filter_changed)
        
        filter_layout.addWidget(search_label)
        filter_layout.addWidget(self.search_edit)
        filter_layout.addWidget(clear_search_btn)
        filter_layout.addWidget(QLabel("|"))  # 分隔符
        filter_layout.addWidget(filter_label)
        filter_layout.addWidget(self.type_filter_combo)
        filter_layout.addStretch()
        
        # 资源操作按钮
        add_btn = ModernButton("+ 添加资源", "primary")
        add_btn.clicked.connect(self.add_resource)
        remove_btn = ModernButton("- 移除资源", "danger")
        remove_btn.clicked.connect(self.remove_resource)
        
        # 创建文件按钮
        create_file_btn = ModernButton("📝 创建文件", "success")
        create_file_btn.clicked.connect(self.create_file_in_project)
        create_file_btn.setToolTip("在项目文件夹中创建新文件，并自动添加为项目资源")
        
        # 设置成品文件夹按钮
        set_product_folder_btn = ModernButton("📦 设置成品文件夹", "warning")
        set_product_folder_btn.clicked.connect(self.set_product_folder)
        set_product_folder_btn.setToolTip("选择一个文件夹，将其设置为成品文件夹，该文件夹下的所有文件都将标记为产出成品")
        
        # 清除无效资源按钮
        clear_invalid_btn = ModernButton("🧹 清除无效资源", "secondary")
        clear_invalid_btn.clicked.connect(self.clear_invalid_resources)
        clear_invalid_btn.setToolTip("清除所有文件路径不存在的无效资源")
        
        filter_layout.addWidget(add_btn)
        filter_layout.addWidget(remove_btn)
        filter_layout.addWidget(create_file_btn)
        filter_layout.addWidget(set_product_folder_btn)
        filter_layout.addWidget(clear_invalid_btn)
        
        card.addLayout(filter_layout)
        
        # 资源树形视图
        self.resource_tree = ModernTreeWidget()
        self.resource_tree.setHeaderLabels(["资源名称", "修改时间", "描述", "标签", "文件路径"])
        self.resource_tree.itemDoubleClicked.connect(self.open_resource_file)
        self.resource_tree.itemClicked.connect(self.handle_tree_item_click)
        self.resource_tree.setColumnWidth(0, 300)
        self.resource_tree.setColumnWidth(1, 150)
        self.resource_tree.setColumnWidth(2, 250)  # 描述列宽度
        self.resource_tree.setColumnWidth(3, 200)  # 标签列宽度
        self.resource_tree.setColumnWidth(4, 250)  # 资源ID列宽度
        
        # 禁用内联编辑功能，防止意外触发编辑导致文件复制问题
        self.resource_tree.setEditTriggers(QTreeWidget.NoEditTriggers)
        
        # 设置右键菜单
        self.resource_tree.setContextMenuPolicy(Qt.CustomContextMenu)
        self.resource_tree.customContextMenuRequested.connect(self.show_resource_context_menu)
        
        # 确保右键菜单在所有项目上都能正常工作
        self.resource_tree.setSelectionMode(QTreeWidget.ExtendedSelection)
        
        card.addWidget(self.resource_tree)
        
        # 加载资源
        self.load_resources()
        
      
        
        return card
        
    def dragEnterEvent(self, event):
        """处理拖拽进入事件"""
        # 只接受文件拖拽
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
            # 显示拖拽状态
            self.setStyleSheet("""
                QDialog {
                    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                        stop:0 #e3f2fd, stop:1 #bbdefb);
                    border: 2px dashed #2196F3;
                }
            """)
    
    def dragLeaveEvent(self, event):
        """处理拖拽离开事件"""
        # 恢复正常样式
        self.setStyleSheet("""
            QDialog {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #f8f9fa, stop:1 #e9ecef);
            }
        """)
        event.accept()
    
    def dropEvent(self, event):
        """处理拖拽释放事件"""
        # 恢复正常样式
        self.setStyleSheet("""
            QDialog {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #f8f9fa, stop:1 #e9ecef);
            }
        """)
        
        # 获取拖拽的文件URL
        urls = event.mimeData().urls()
        if urls:
            paths = [url.toLocalFile() for url in urls]
            
            # 分离文件和文件夹
            files = []
            folders = []
            
            for path in paths:
                if os.path.isfile(path):
                    files.append(path)
                elif os.path.isdir(path):
                    folders.append(path)
            
            # 遍历文件夹，收集所有文件
            for folder_path in folders:
                folder_files = self.collect_files_from_folder(folder_path)
                files.extend(folder_files)
            
            # 如果没有找到任何文件
            if not files:
                QMessageBox.information(self, "提示", "拖拽的文件夹中没有找到任何文件")
                event.acceptProposedAction()
                return
            
            # 如果是多个文件，使用批量添加对话框
            if len(files) > 1:
                dialog = BatchAddResourceDialog(self, self.parent_tool.resource_categories, files, None, self.parent_tool.resource_types)
                if dialog.exec_() == QDialog.Accepted:
                    self.handle_batch_resources(dialog.batch_resources_data)
            else:
                # 单个文件，使用普通添加对话框
                dialog = AddResourceDialog(self, self.parent_tool.resource_categories, self.parent_tool.resource_types)
                dialog.set_file_path(files[0])
                if dialog.exec_() == QDialog.Accepted:
                    self.handle_single_resource(dialog.get_resource_data())
        
        event.acceptProposedAction()
    
    def collect_files_from_folder(self, folder_path):
        """递归收集文件夹中的所有文件"""
        files = []
        try:
            for root, dirs, filenames in os.walk(folder_path):
                for filename in filenames:
                    file_path = os.path.join(root, filename)
                    # 跳过隐藏文件和系统文件
                    if not filename.startswith('.') and not filename.startswith('~'):
                        files.append(file_path)
        except Exception as e:
            logging.error(f"遍历文件夹失败: {e}")
            QMessageBox.warning(self, "错误", f"遍历文件夹失败: {str(e)}")
        
        return files
    
    def handle_batch_resources(self, batch_resources_data):
        """处理批量添加的资源"""
        if 'resources' not in self.project:
            self.project['resources'] = []
        
        added_count = 0
        duplicate_count = 0
        
        for resource_data in batch_resources_data:
            resource_name = resource_data.get('name', '')
            resource_path = resource_data.get('path', '')
            
            # 检查重复（通过名称或路径）
            is_duplicate = False
            normalized_resource_path = os.path.normpath(resource_path) if resource_path else ''
            for existing_resource in self.project['resources']:
                existing_path = os.path.normpath(existing_resource.get('path', ''))
                if (existing_resource.get('name') == resource_name and resource_name) or \
                   (existing_path == normalized_resource_path and normalized_resource_path):
                    duplicate_count += 1
                    is_duplicate = True
                    break
            
            if not is_duplicate:
                self.project['resources'].append(resource_data)
                added_count +=1
        
        self.parent_tool.update_project_modified_time(self.project['name'], save_immediately=False)
        self.parent_tool.save_data()
        self.parent_tool.refresh_project_list()
        
        # 显示批量添加结果
        message = f"✅ 成功添加 {added_count} 个资源到项目 '{self.project['name']}'"
        if duplicate_count > 0:
            message += f"，跳过 {duplicate_count} 个重复资源"
        self.parent_tool.status_bar.showMessage(message)
        
        # 刷新资源列表
        self.load_resources()
    
    def handle_single_resource(self, resource_data):
        """处理单个添加的资源"""
        if 'resources' not in self.project:
            self.project['resources'] = []
        
        resource_name = resource_data.get('name', '')
        resource_path = resource_data.get('path', '')
        
        # 检查重复（通过名称或路径）
        normalized_resource_path = os.path.normpath(resource_path) if resource_path else ''
        for existing_resource in self.project['resources']:
            existing_path = os.path.normpath(existing_resource.get('path', ''))
            if (existing_resource.get('name') == resource_name and resource_name) or \
               (existing_path == normalized_resource_path and normalized_resource_path):
                QMessageBox.warning(self, "重复资源", 
                                  f"资源 '{resource_name}' 已存在于项目中，无法重复添加。")
                return
        
        # 添加资源
        self.project['resources'].append(resource_data)
        self.parent_tool.update_project_modified_time(self.project['name'], save_immediately=False)
        self.parent_tool.save_data()
        self.parent_tool.refresh_project_list()
        
        # 显示状态栏消息
        message = f"✅ 资源 '{resource_data['name']}' 已添加到项目 '{self.project['name']}'"
        self.parent_tool.status_bar.showMessage(message)
        
        # 刷新资源列表
        self.load_resources()
        
    def get_recently_opened_resource(self):
        """从项目笔记中获取最近打开的资源名称"""
        try:
            # 获取项目文件夹路径
            folder_path = self.project.get('folder_path', '')
            if not folder_path or not os.path.exists(folder_path):
                return None
            
            # 构建笔记文件路径
            project_name = self.project['name']
            safe_name = "".join(c for c in project_name if c.isalnum() or c in (' ', '-', '_', '（', '）', '(', ')')).strip()
            if not safe_name:
                safe_name = "新项目"
            notes_file = os.path.join(folder_path, f"{safe_name}_笔记.md")
            
            # 如果笔记文件不存在，返回None
            if not os.path.exists(notes_file):
                return None
            
            # 读取笔记文件内容
            with open(notes_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 查找最近打开的资源记录
            recent_marker = "🔖 [最近打开]"
            lines = content.split('\n')
            for line in lines:
                if recent_marker in line:
                    # 提取资源名称
                    # 格式: - **时间戳** 🔖 [最近打开] 打开资源: 资源名称
                    parts = line.split('打开资源:')
                    if len(parts) > 1:
                        resource_name = parts[1].strip()
                        return resource_name
            
            return None
        except Exception as e:
            logging.error(f"获取最近打开资源失败: {e}")
            return None
    
    def load_resources(self):
        """加载项目资源（异步分批处理）"""
        # 使用setUpdatesEnabled(False)来提高性能
        self.resource_tree.setUpdatesEnabled(False)
        self.resource_tree.clear()
        
        # 使用类属性中的最近打开的资源名称，而不是每次都重新获取
        recently_opened_resource = getattr(self, 'recently_opened_resource', None)
        
        if 'resources' in self.project:
            # 获取当前筛选类型（如果type_filter_combo还未创建，使用默认值）
            filter_type = self.type_filter_combo.currentText() if hasattr(self, 'type_filter_combo') else "全部类型"
            
            # 获取搜索关键词（如果search_edit还未创建，使用空字符串）
            search_text = self.search_edit.text().strip().lower() if hasattr(self, 'search_edit') else ""
            
            # 初始化异步处理相关变量
            self.resources_to_process = []
            self.processed_resources = []
            self.resources_need_save = False
            
            # 预处理资源列表，进行筛选但不计算tags
            for resource in self.project['resources']:
                resource_path = resource.get('path', '')
                resource_type = resource.get('type', '')
                
                # 类型筛选
                if filter_type != "全部类型" and resource_type != filter_type:
                    continue
                
                # 搜索筛选
                if search_text:
                    # 在资源名称、描述、路径中搜索关键词
                    resource_name = resource.get('name', '').lower()
                    resource_desc = resource.get('description', '').lower()
                    resource_path_lower = resource_path.lower()
                    resource_type_lower = resource_type.lower()
                    
                    if (search_text in resource_name or 
                        search_text in resource_desc or 
                        search_text in resource_path_lower or 
                        search_text in resource_type_lower):
                        self.resources_to_process.append(resource)
                else:
                    self.resources_to_process.append(resource)
            
            # 如果资源数量较少，直接同步处理
            if len(self.resources_to_process) <= 100:
                self._process_resources_sync()
            else:
                # 资源数量较多，使用异步分批处理
                self._start_async_resource_processing()
            
    def _process_resources_sync(self):
        """同步处理资源（用于少量资源）"""
        recently_opened_resource = getattr(self, 'recently_opened_resource', None)
        
        # 处理所有资源的tags
        for resource in self.resources_to_process:
            self._process_single_resource(resource)
        
        # 如果有资源需要保存，统一保存一次
        if self.resources_need_save:
            self.parent_tool.save_data()
        
        # 显示资源
        self._display_resources(self.resources_to_process, recently_opened_resource)
        
        # 重新启用更新并展开所有项
        self.resource_tree.setUpdatesEnabled(True)
        self.resource_tree.expandAll()
    
    def _start_async_resource_processing(self):
        """开始异步分批处理资源"""
        # 显示加载提示
        loading_item = QTreeWidgetItem(["⏳ 正在加载资源，请稍候...", "", "", "", "", ""])
        self.resource_tree.addTopLevelItem(loading_item)
        self.resource_tree.setUpdatesEnabled(True)
        
        # 初始化处理状态
        self.current_batch_index = 0
        self.batch_size = 50  # 每批处理50个资源
        self.processed_resources = []
        
        # 创建定时器进行分批处理
        if not hasattr(self, 'resource_processing_timer'):
            self.resource_processing_timer = QTimer()
            self.resource_processing_timer.timeout.connect(self._process_next_batch)
        
        # 开始处理
        self.resource_processing_timer.start(10)  # 每10毫秒处理一批
    
    def _process_next_batch(self):
        """处理下一批资源"""
        start_index = self.current_batch_index * self.batch_size
        end_index = min(start_index + self.batch_size, len(self.resources_to_process))
        
        # 处理当前批次的资源
        for i in range(start_index, end_index):
            resource = self.resources_to_process[i]
            self._process_single_resource(resource)
            self.processed_resources.append(resource)
        
        self.current_batch_index += 1
        
        # 更新进度提示
        progress = min(100, int((len(self.processed_resources) / len(self.resources_to_process)) * 100))
        if self.resource_tree.topLevelItemCount() > 0:
            loading_item = self.resource_tree.topLevelItem(0)
            loading_item.setText(0, f"⏳ 正在加载资源... {progress}% ({len(self.processed_resources)}/{len(self.resources_to_process)})")
        
        # 检查是否处理完成
        if len(self.processed_resources) >= len(self.resources_to_process):
            self._finish_async_processing()
    
    def _finish_async_processing(self):
        """完成异步处理"""
        # 停止定时器
        self.resource_processing_timer.stop()
        
        # 如果有资源需要保存，统一保存一次
        if self.resources_need_save:
            self.parent_tool.save_data()
        
        # 清除加载提示并显示资源
        self.resource_tree.setUpdatesEnabled(False)
        self.resource_tree.clear()
        
        recently_opened_resource = getattr(self, 'recently_opened_resource', None)
        self._display_resources(self.processed_resources, recently_opened_resource)
        
        # 重新启用更新并展开所有项
        self.resource_tree.setUpdatesEnabled(True)
        self.resource_tree.expandAll()
        
        # 显示完成消息
        if hasattr(self.parent_tool, 'status_bar'):
            self.parent_tool.status_bar.showMessage(f"✅ 已加载 {len(self.processed_resources)} 个资源", 2000)
    
    def refresh_from_parent(self):
        """从父工具刷新项目数据并重新加载资源"""
        try:
            if self.project and self.parent_tool:
                # 重新从数据文件加载最新数据，确保获取到最新的项目资源信息
                self.parent_tool.load_data()
                
                project_name = self.project.get('name')
                if project_name:
                    # 在父工具的项目列表中查找最新的项目数据
                    for latest_project in self.parent_tool.projects:
                        if latest_project.get('name') == project_name:
                            # 使用最新的项目数据，确保资源信息是最新的
                            self.project = latest_project.copy()
                            break
                    
                    # 重新从markdown文件加载项目数据（笔记和清单）
                    self.load_from_markdown_file()
                    
                    # 重新加载资源
                    if hasattr(self, 'load_resources'):
                        self.load_resources()
        except Exception as e:
            print(f"刷新项目详情对话框数据时出错：{str(e)}")
            self.parent_tool.status_bar.showMessage(f"✅ 已加载 {len(self.processed_resources)} 个资源")
    
    def _process_single_resource(self, resource):
        """处理单个资源的tags"""
        # 检查资源是否有tags字段
        tags = resource.get('tags', '')
        
        # 如果没有tags，说明这是第一次加载，需要计算文件类型并存储
        if not tags:
            resource_path = resource.get('path', '')
            file_ext = os.path.splitext(resource_path)[1].lower()
            calculated_file_type = self.get_file_type_display(file_ext)
            
            # 将计算出的文件类型存储到资源的tags字段中
            resource['tags'] = calculated_file_type
            tags = calculated_file_type
            
            # 标记需要保存数据
            self.resources_need_save = True
        
        # 直接使用tags字段，不再使用缓存字段
    
    def _display_resources(self, resources, recently_opened_resource):
        """显示资源列表"""
        # 统一按文件夹分组显示所有资源
        folder_groups = {}  # 用于存储所有资源的文件夹分组
        
        for resource in resources:
            # 获取文件所在文件夹路径
            folder_path = os.path.dirname(resource['path'])
            folder_name = os.path.basename(folder_path) if folder_path else '根目录'
            
            if folder_name not in folder_groups:
                folder_groups[folder_name] = []
            folder_groups[folder_name].append(resource)
        
        # 显示所有资源（按文件夹归类）
        for folder_name, resources in folder_groups.items():
            # 获取文件夹的实际路径
            folder_path = ""
            if resources:
                first_resource_path = resources[0]['path']
                folder_path = os.path.dirname(first_resource_path)
            
            # 检查是否为成品文件夹
            is_product_folder = self.is_product_folder(folder_path)
            
            # 获取文件夹描述
            folder_desc = self.get_folder_description(folder_path)
            
            # 根据是否为成品文件夹选择不同的图标
            folder_icon = "📦" if is_product_folder else "📂"
            
            # 构建文件夹显示文本
            folder_display_text = f"{folder_icon} {folder_name} ({len(resources)}) 📁"
            
            # 创建文件夹项，将描述显示在描述列中
            folder_item = QTreeWidgetItem([folder_display_text, "", folder_desc, "", ""])
            folder_item.setExpanded(True)
            
            # 存储文件夹路径到节点数据中
            folder_item.setData(0, Qt.UserRole, folder_path)
            folder_item.setData(1, Qt.UserRole, "folder")  # 标记为文件夹类型
            
            # 设置文件夹节点的工具提示
            tooltip_text = f"文件夹: {folder_path}\n点击📁图标打开文件夹\n右键点击可刷新此文件夹下的所有文件"
            if folder_desc:
                tooltip_text += f"\n描述: {folder_desc}"
            folder_item.setToolTip(0, tooltip_text)
            
            self.resource_tree.addTopLevelItem(folder_item)
            
            # 按修改时间排序资源（最新的在前）
            resources_with_time = []
            for resource in resources:
                file_time = self.get_file_modification_time(resource['path'])
                resources_with_time.append((resource, file_time))
            
            # 按时间戳排序（最新的在前）
            resources_with_time.sort(key=lambda x: x[1], reverse=True)
            
            # 添加资源
            for resource, file_timestamp in resources_with_time:
                # 获取文件图标
                file_icon = self.get_file_icon(resource['path'])
                
                # 获取文件时间信息
                file_time_info = self.get_file_time_info(resource['path'])
                
                # 判断是否为最近修改（24小时内）
                is_recent = self.is_recently_modified(file_timestamp)
                recent_indicator = " 🔥" if is_recent else ""
                
                # 判断是否为最近打开的资源
                is_recently_opened = recently_opened_resource and resource['name'] == recently_opened_resource
                recently_opened_indicator = " 🔖" if is_recently_opened else ""
                
                # 创建主资源项 - 只显示文件名和基本信息
                display_name = f"{file_icon} {resource['name']}{recent_indicator}{recently_opened_indicator}"
                description = resource.get('description', '')                
                tags = resource.get('tags', '')
                resource_item = QTreeWidgetItem([display_name, file_time_info, description, tags, resource['path']])
                resource_item.setData(0, Qt.UserRole, resource['path'])
                
                # 设置最近修改文件的样式
                if is_recent:
                    font = resource_item.font(0)
                    font.setBold(True)
                    resource_item.setFont(0, font)
                    resource_item.setForeground(0, QColor("#FF5722"))  # 橙红色
                
                # 设置最近打开资源的样式
                if is_recently_opened:
                    font = resource_item.font(0)
                    font.setBold(True)
                    resource_item.setFont(0, font)
                    # 如果同时是最近修改和最近打开，使用紫色；否则使用蓝色
                    color = "#9C27B0" if is_recent else "#2196F3"  # 紫色或蓝色
                    resource_item.setForeground(0, QColor(color))
                
                # 创建分类信息子项（使用缓存的信息）
                self.create_classification_item_cached(resource_item, resource)
                
                # 设置工具提示
                resource_type = resource.get('type', '')
                tooltip = f"路径: {resource['path']}"
                if resource_type:
                    tooltip += f"\n资源类型: {resource_type}"
                if description:
                    tooltip += f"\n描述: {description}"

                tooltip += f"\n修改时间: {file_time_info}"
                if is_recently_opened:
                    tooltip += "\n🔖 最近打开的资源"
                if is_recent:
                    tooltip += "\n🔥 最近修改的文件"
                tooltip += "\n双击打开文件"
                resource_item.setToolTip(0, tooltip)
                
                folder_item.addChild(resource_item)
    
    def create_classification_item(self, parent_item, resource):
        """为资源创建分类信息子项 - 现代化标签显示"""
        # 直接使用tags字段作为文件类型信息
        file_type = resource.get('tags', '')
        
        # 获取资源类型
        resource_type = resource.get('type', '未分类')
        
        # 获取其他可能的分类信息
        tags = resource.get('tags', '')
        status = resource.get('status', '')
        
        # 创建现代化的标签显示
        tag_items = []
        
        # 文件类型标签
        if file_type:
            tag_items.append(f"📄 {file_type}")
        
        # 资源类型标签
        if resource_type and resource_type != '未分类':
            tag_items.append(f"🏷️ {resource_type}")
        
        # 状态标签
        if status:
            tag_items.append(f"📊 {status}")
        
        # 如果有标签信息，创建美观的标签行
        if tag_items:
            # 第一行：主要标签信息
            main_tags = tag_items[:3]  # 最多显示3个主要标签
            classification_text = "    " + "  •  ".join(main_tags)
            classification_item = QTreeWidgetItem([classification_text, "", "", "", "", ""])
            
            # 设置主标签行的样式
            classification_item.setForeground(0, QColor("#4A90E2"))  # 蓝色文字
            font = classification_item.font(0)
            font.setPointSize(font.pointSize() - 1)  # 稍小的字体
            font.setBold(True)  # 粗体
            classification_item.setFont(0, font)
            
            # 设置分类项不可选择但保持右键菜单功能
            classification_item.setFlags(classification_item.flags() & ~Qt.ItemIsSelectable)
            
            parent_item.addChild(classification_item)
            
            # 如果有更多标签，创建第二行
            if len(tag_items) > 3:
                extra_tags = tag_items[3:]
                extra_text = "    " + "  •  ".join(extra_tags)
                extra_item = QTreeWidgetItem([extra_text, "", "", "", "", ""])
                
                # 设置额外标签行的样式
                extra_item.setForeground(0, QColor("#7B68EE"))  # 紫色文字
                extra_font = extra_item.font(0)
                extra_font.setPointSize(extra_font.pointSize() - 1)
                extra_font.setItalic(True)
                extra_item.setFont(0, extra_font)
                
                extra_item.setFlags(extra_item.flags() & ~Qt.ItemIsSelectable)
                parent_item.addChild(extra_item)
    
    def create_classification_item_cached(self, parent_item, resource):
        """为资源创建分类信息子项 - 现代化标签显示"""
        # 直接使用tags字段作为文件类型信息
        file_type = resource.get('tags', '')
        
        # 获取资源类型
        resource_type = resource.get('type', '未分类')
        
        # 获取其他可能的分类信息
        tags = resource.get('tags', '')
        status = resource.get('status', '')
        
        # 创建现代化的标签显示
        tag_items = []
        
        # 文件类型标签
        if file_type:
            tag_items.append(f"📄 {file_type}")
        
        # 资源类型标签
        if resource_type and resource_type != '未分类':
            tag_items.append(f"🏷️ {resource_type}")
        
        # 状态标签
        if status:
            tag_items.append(f"📊 {status}")
        
        # 如果有标签信息，创建美观的标签行
        if tag_items:
            # 第一行：主要标签信息
            main_tags = tag_items[:3]  # 最多显示3个主要标签
            classification_text = "    " + "  •  ".join(main_tags)
            classification_item = QTreeWidgetItem([classification_text, "", "", "", "", ""])
            
            # 设置主标签行的样式
            classification_item.setForeground(0, QColor("#4A90E2"))  # 蓝色文字
            font = classification_item.font(0)
            font.setPointSize(font.pointSize() - 1)  # 稍小的字体
            font.setBold(True)  # 粗体
            classification_item.setFont(0, font)
            
            # 设置分类项不可选择但保持右键菜单功能
            classification_item.setFlags(classification_item.flags() & ~Qt.ItemIsSelectable)
            
            parent_item.addChild(classification_item)
            
            # 如果有更多标签，创建第二行
            if len(tag_items) > 3:
                extra_tags = tag_items[3:]
                extra_text = "    " + "  •  ".join(extra_tags)
                extra_item = QTreeWidgetItem([extra_text, "", "", "", "", ""])
                
                # 设置额外标签行的样式
                extra_item.setForeground(0, QColor("#7B68EE"))  # 紫色文字
                extra_font = extra_item.font(0)
                extra_font.setPointSize(extra_font.pointSize() - 1)
                extra_font.setItalic(True)
                extra_item.setFont(0, extra_font)
                
                extra_item.setFlags(extra_item.flags() & ~Qt.ItemIsSelectable)
                parent_item.addChild(extra_item)
            
            # 设置分类项跨越所有列（需要确保父项已添加到树控件中）
            tree_widget = parent_item.treeWidget()
            if tree_widget is not None:
                # 设置主标签行跨列
                main_index = parent_item.indexOfChild(classification_item)
                tree_widget.setFirstColumnSpanned(main_index, parent_item, True)
                
                # 如果有额外标签行，也设置跨列
                if len(tag_items) > 3:
                    extra_index = parent_item.indexOfChild(extra_item)
                    tree_widget.setFirstColumnSpanned(extra_index, parent_item, True)
    
    def get_file_type_display(self, file_ext):
        """根据文件扩展名获取文件类型显示名称（从资源类型配置中获取）"""
        # 首先从资源类型配置中查找
        for type_name, type_info in self.parent_tool.resource_types.items():
            extensions = type_info.get('extensions', [])
            extension_display_names = type_info.get('extension_display_names', {})
            if file_ext in extensions:
                # 如果在extensions中找到匹配，优先使用extension_display_names中的显示名称
                if file_ext in extension_display_names:
                    result = extension_display_names[file_ext]
                else:
                    # 如果没有对应的显示名称，使用资源类型名称
                    result = type_name
                return result
        
        # 如果在资源类型配置中没有找到，使用默认的扩展映射表
        default_file_type_map = {
            '.json': 'JSON数据',
            '.xml': 'XML文档',
            '.xls': 'Excel表格',
            '.xlsx': 'Excel表格',
            '.ppt': 'PowerPoint',
            '.pptx': 'PowerPoint',
            '.jpg': '图片文件',
            '.jpeg': '图片文件',
            '.png': '图片文件',
            '.gif': '图片文件',
            '.svg': '矢量图',
            '.mp3': '音频文件',
            '.wav': '音频文件',
            '.zip': '压缩文件',
            '.rar': '压缩文件',
            '.7z': '压缩文件',
            '.exe': '可执行文件',
            '.dll': '动态链接库',
            '.so': '共享库',
            '.jar': 'Java包',
            '.war': 'Web应用包',
            '.sql': 'SQL脚本',
            '.log': '日志文件',
            '.ini': '配置文件',
            '.cfg': '配置文件',
            '.conf': '配置文件',
            '.yaml': 'YAML配置',
            '.yml': 'YAML配置',
            '.toml': 'TOML配置',
        }
        
        result = default_file_type_map.get(file_ext, '其他文件')
        return result
    
    def is_product_folder(self, folder_path):
        """判断文件夹是否为成品文件夹"""
        if not folder_path or 'resources' not in self.project:
            return False
        
        # 标准化路径进行比较
        normalized_folder_path = os.path.normpath(folder_path)
        
        # 检查该文件夹下是否有类型为'产出成品'的文件
        for resource in self.project['resources']:
            resource_path = resource.get('path', '')
            resource_type = resource.get('type', '')
            
            # 如果是文件资源且类型为产出成品，并且文件在该文件夹下
            if (os.path.isfile(resource_path) and 
                resource_type == '产出成品'):
                # 检查文件是否在该文件夹下（包括子文件夹）
                resource_dir = os.path.normpath(os.path.dirname(resource_path))
                if resource_dir.startswith(normalized_folder_path):
                    return True
        
        return False
    
    def on_type_filter_changed(self, filter_type):
        """处理资源类型筛选变化"""
        self.load_resources()
    
    def on_search_text_changed(self, text):
        """处理搜索文本变化"""
        self.load_resources()
    
    def clear_search(self):
        """清除搜索框内容"""
        self.search_edit.clear()
    
    def set_product_folder(self):
        """设置成品文件夹"""
        folder_path = QFileDialog.getExistingDirectory(
            self, 
            "选择成品文件夹", 
            "", 
            QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks
        )
        
        if folder_path:
            folder_path = os.path.normpath(folder_path)
            # 检查文件夹是否已经在资源中
            if 'resources' not in self.project:
                self.project['resources'] = []
            
            # 移除可能存在的文件夹资源项（只保留文件）
            self.project['resources'] = [r for r in self.project['resources'] 
                                       if not (r.get('path') == folder_path and os.path.isdir(r.get('path', '')))]
            
            # 将该文件夹下的所有文件标记为产出成品
            try:
                files_added = 0
                files_updated = 0
                for root, dirs, files in os.walk(folder_path):
                    for file_name in files:
                        file_path = os.path.join(root, file_name)
                        # 跳过隐藏文件
                        if not file_name.startswith('.'):
                            # 检查文件是否已存在
                            file_exists = False
                            for resource in self.project['resources']:
                                if resource.get('path') == file_path:
                                    # 更新现有文件的类型
                                    resource['type'] = '产出成品'
                                    resource['description'] = f'来自成品文件夹: {os.path.basename(folder_path)}'
                                    file_exists = True
                                    files_updated += 1
                                    break
                            
                            if not file_exists:
                                # 添加新文件
                                file_resource = {
                                    'name': file_name,
                                    'path': file_path,
                                    'type': '产出成品',
                                    'description': f'来自成品文件夹: {os.path.basename(folder_path)}',
                                    'added_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                                }
                                self.project['resources'].append(file_resource)
                                files_added += 1
                
                # 构建消息
                message_parts = []
                if files_added > 0:
                    message_parts.append(f"添加了 {files_added} 个新文件")
                if files_updated > 0:
                    message_parts.append(f"更新了 {files_updated} 个现有文件")
                
                if message_parts:
                    message = f"已将成品文件夹 '{os.path.basename(folder_path)}' 下的文件设置为产出成品：" + "，".join(message_parts)
                else:
                    message = f"成品文件夹 '{os.path.basename(folder_path)}' 下没有找到可添加的文件"
                    
            except Exception as e:
                QMessageBox.warning(self, "警告", f"遍历文件夹时出错: {str(e)}")
                return
            
            # 保存项目数据
            self.parent_tool.update_project_modified_time(self.project['name'], save_immediately=False)
            self.parent_tool.save_data()
            self.parent_tool.refresh_project_list()
            
            # 刷新资源列表
            self.load_resources()
            
            # 显示成功消息
            QMessageBox.information(self, "设置成功", message)
            self.parent_tool.status_bar.showMessage(f"✅ {message}")
    
    def show_resource_context_menu(self, position):
        """显示资源树的右键菜单"""
        item = self.resource_tree.itemAt(position)
        
        menu = QMenu(self)
        
        if item:
            # 检查是否是文件夹节点
            is_folder = item.data(1, Qt.UserRole) == "folder"
            
            if is_folder:
                # 文件夹右键菜单
                open_folder_action = menu.addAction("📂 打开文件夹")
                folder_path = item.data(0, Qt.UserRole)
                open_folder_action.triggered.connect(lambda: self.open_folder(folder_path))
                
                menu.addSeparator()
                
                # 添加文件夹描述选项
                add_desc_action = menu.addAction("📝 添加文件夹描述")
                add_desc_action.triggered.connect(lambda: self.add_folder_description(item))
                
                menu.addSeparator()
                
                refresh_action = menu.addAction("🔄 刷新文件夹")
                refresh_action.triggered.connect(lambda: self.refresh_folder_files(item))
                
                import_action = menu.addAction("📁 导入文件夹下所有文件")
                import_action.triggered.connect(lambda: self.import_folder_files(item))
                
                menu.addSeparator()
                
                # 添加移除整个文件夹的选项
                remove_folder_action = menu.addAction("🗑️ 移除整个文件夹")
                remove_folder_action.triggered.connect(lambda: self.remove_entire_folder(item))
                
                menu.addSeparator()
            else:
                # 文件右键菜单
                open_action = menu.addAction("📂 打开文件")
                open_action.triggered.connect(lambda: self.open_resource_file(item, 0))
                
                open_folder_action = menu.addAction("📁 打开所在文件夹")
                file_path = item.data(0, Qt.UserRole)
                open_folder_action.triggered.connect(lambda: self.open_containing_folder(file_path))
                

                
                menu.addSeparator()
                
                # 添加修改资源类型的选项
                edit_type_action = menu.addAction("🏷️ 修改资源类型")
                edit_type_action.triggered.connect(lambda: self.edit_resource_type(item))
                
                menu.addSeparator()
                
                # 添加文件操作菜单
                rename_action = menu.addAction("✏️ 重命名文件")
                rename_action.triggered.connect(lambda: self.rename_resource_file(item))
                
                copy_action = menu.addAction("📋 复制文件")
                copy_action.triggered.connect(lambda: self.copy_resource_file(item))
                
                delete_file_action = menu.addAction("🗑️ 删除文件")
                delete_file_action.triggered.connect(lambda: self.delete_resource_file(item))
                
                menu.addSeparator()
                
                # 添加重新载入资源选项
                reload_action = menu.addAction("🔄 重新载入资源")
                reload_action.triggered.connect(lambda: self.reload_resource(item))
                
                menu.addSeparator()
                
                delete_action = menu.addAction("❌ 从资源中移除")
                delete_action.triggered.connect(lambda: self.delete_resource_from_tree(item))
                
                menu.addSeparator()
        
        # 通用菜单项（无论是否选中项目都显示）
        refresh_all_action = menu.addAction("🔄 刷新所有资源")
        refresh_all_action.triggered.connect(self.refresh_resources)
        
        add_resource_action = menu.addAction("➕ 添加资源")
        add_resource_action.triggered.connect(self.add_resource)
        
        # 显示菜单
        menu.exec_(self.resource_tree.mapToGlobal(position))
    
    def edit_resource_type(self, item):
        """编辑资源类型"""
        if not item:
            return
            
        # 获取文件路径
        file_path = item.data(0, Qt.UserRole)
        if not file_path:
            return
            
        # 查找对应的资源
        target_resource = None
        for resource in self.project.get('resources', []):
            if resource['path'] == file_path:
                target_resource = resource
                break
                
        if not target_resource:
            QMessageBox.warning(self, "错误", "找不到对应的资源")
            return
            
        # 创建编辑对话框
        dialog = AddResourceDialog(self, self.parent_tool.resource_categories, self.parent_tool.resource_types)
        
        # 预填充现有数据
        dialog.name_edit.setText(target_resource.get('name', ''))
        dialog.path_edit.setText(target_resource.get('path', ''))
        dialog.desc_edit.setPlainText(target_resource.get('description', ''))
        dialog.tags_edit.setText(target_resource.get('tags', ''))
        
        # 设置当前类型
        current_type = target_resource.get('type', '')
        if current_type:
            type_index = dialog.type_combo.findText(current_type)
            if type_index >= 0:
                dialog.type_combo.setCurrentIndex(type_index)
        
        # 设置对话框标题
        dialog.setWindowTitle("修改资源类型")
        
        # 禁用名称和路径编辑（只允许修改类型和描述）
        dialog.name_edit.setReadOnly(True)
        dialog.path_edit.setReadOnly(True)
        dialog.browse_btn.setEnabled(False)
        
        if dialog.exec_() == QDialog.Accepted:
            # 获取新的数据
            new_data = dialog.get_resource_data()
            
            # 更新资源数据
            target_resource['type'] = new_data.get('type', '')
            target_resource['description'] = new_data.get('description', '')
            target_resource['tags'] = new_data.get('tags', '')
            
            # 记录项目日志
            self.parent_tool.add_project_log(self.project['name'], "修改资源类型", 
                                            f"修改资源 '{target_resource['name']}' 的类型为: {new_data.get('type', '未分类')}", 
                                            "资源")
            
            # 保存数据
            self.parent_tool.update_project_modified_time(self.project['name'], save_immediately=False)
            self.parent_tool.save_data()
            self.parent_tool.refresh_project_list()
            
            # 刷新资源列表
            self.load_resources()
            # 更新tab标题中的数量
            self.update_tab_counts()
            
            # 显示成功消息
            message = f"✅ 资源 '{target_resource['name']}' 的类型已更新为: {new_data.get('type', '未分类')}"
            self.parent_tool.status_bar.showMessage(message)
    
    def open_containing_folder(self, file_path):
        """打开文件所在文件夹"""
        if not file_path or not os.path.exists(file_path):
            QMessageBox.warning(self, "警告", "文件路径无效或文件不存在")
            return
            
        folder_path = os.path.dirname(file_path)
        try:
            if sys.platform.startswith('win'):
                os.startfile(folder_path)
            elif sys.platform.startswith('darwin'):  # macOS
                subprocess.run(['open', folder_path])
            else:  # Linux
                subprocess.run(['xdg-open', folder_path])
        except Exception as e:
            QMessageBox.warning(self, "打开失败", f"无法打开文件夹:\n{str(e)}")
    

    

    
    def rename_resource_file(self, item):
        """重命名资源文件"""
        if not item:
            return
            
        # 获取文件路径
        file_path = item.data(0, Qt.UserRole)
        if not file_path or not os.path.exists(file_path):
            QMessageBox.warning(self, "警告", "文件路径无效或文件不存在")
            return
            
        # 获取当前文件名和扩展名
        current_name = os.path.basename(file_path)
        name_without_ext, ext = os.path.splitext(current_name)
        
        # 弹出输入对话框
        new_name, ok = QInputDialog.getText(
            self, "重命名文件", 
            f"请输入新的文件名（不含扩展名）:\n当前文件名: {current_name}", 
            QLineEdit.Normal, name_without_ext
        )
        
        if not ok or not new_name.strip():
            return
            
        new_name = new_name.strip()
        new_file_name = new_name + ext
        new_file_path = os.path.join(os.path.dirname(file_path), new_file_name)
        
        # 检查新文件名是否已存在
        if os.path.exists(new_file_path):
            QMessageBox.warning(self, "重命名失败", f"文件名 '{new_file_name}' 已存在")
            return
            
        try:
            # 重命名文件
            os.rename(file_path, new_file_path)
            
            # 更新资源数据中的路径和名称
            for resource in self.project.get('resources', []):
                if resource.get('path') == file_path:
                    resource['path'] = new_file_path
                    resource['name'] = new_file_name
                    break
            
            # 记录项目日志
            self.parent_tool.add_project_log(self.project['name'], "重命名文件", 
                                            f"将文件 '{current_name}' 重命名为 '{new_file_name}'", 
                                            "资源")
            
            # 保存数据（异步处理，避免阻塞UI）
            self.parent_tool.update_project_modified_time(self.project['name'], save_immediately=False)
            self.parent_tool.save_data()
            
            # 只刷新资源列表，不刷新整个项目列表
            self.load_resources()
            # 更新tab标题中的数量
            self.update_tab_counts()
            
            # 显示成功消息
            message = f"✅ 文件已重命名为: {new_file_name}"
            self.parent_tool.status_bar.showMessage(message)
            
            # 使用定时器延迟显示消息框，避免阻塞
            QTimer.singleShot(100, lambda: QMessageBox.information(self, "重命名成功", message))
            
        except Exception as e:
            QMessageBox.critical(self, "重命名失败", f"重命名文件时出错:\n{str(e)}")
    
    def copy_resource_file(self, item):
        """复制资源文件"""
        if not item:
            return
            
        # 获取文件路径
        file_path = item.data(0, Qt.UserRole)
        if not file_path or not os.path.exists(file_path):
            QMessageBox.warning(self, "警告", "文件路径无效或文件不存在")
            return
            
        # 选择目标文件夹
        target_folder = QFileDialog.getExistingDirectory(
            self, "选择复制目标文件夹", os.path.dirname(file_path)
        )
        
        if not target_folder:
            return
            
        target_folder = os.path.normpath(target_folder)
        # 获取文件名
        file_name = os.path.basename(file_path)
        target_path = os.path.join(target_folder, file_name)
        
        # 如果目标文件已存在，询问是否覆盖
        if os.path.exists(target_path):
            reply = QMessageBox.question(
                self, "文件已存在", 
                f"目标位置已存在文件 '{file_name}'，是否覆盖？",
                QMessageBox.Yes | QMessageBox.No
            )
            if reply != QMessageBox.Yes:
                return
        
        try:
            # 复制文件
            import shutil
            shutil.copy2(file_path, target_path)
            
            # 询问是否将复制的文件添加到资源中
            reply = QMessageBox.question(
                self, "添加到资源", 
                f"文件已复制到:\n{target_path}\n\n是否将复制的文件添加到项目资源中？",
                QMessageBox.Yes | QMessageBox.No
            )
            
            if reply == QMessageBox.Yes:
                # 获取原资源信息
                original_resource = None
                for resource in self.project.get('resources', []):
                    if resource.get('path') == file_path:
                        original_resource = resource
                        break
                
                if original_resource:
                    # 创建新资源
                    new_resource = {
                        'name': file_name,
                        'path': target_path,
                        'type': original_resource.get('type', '参考资料'),
                        'description': f"复制自: {original_resource.get('description', '')}",
                        'added_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    }
                    
                    # 添加到资源列表
                    if 'resources' not in self.project:
                        self.project['resources'] = []
                    self.project['resources'].append(new_resource)
                    
                    # 记录项目日志
                    self.parent_tool.add_project_log(self.project['name'], "复制文件", 
                                                    f"复制文件 '{file_name}' 到 '{target_folder}' 并添加到资源", 
                                                    "资源")
                    
                    # 保存数据（异步处理，避免阻塞UI）
                    self.parent_tool.update_project_modified_time(self.project['name'], save_immediately=False)
                    self.parent_tool.save_data()
                    
                    # 只刷新资源列表，不刷新整个项目列表
                    self.load_resources()
                    # 更新tab标题中的数量
                    self.update_tab_counts()
            
            # 显示成功消息
            message = f"✅ 文件已复制到: {target_folder}"
            self.parent_tool.status_bar.showMessage(message)
            
            # 使用定时器延迟显示消息框，避免阻塞
            QTimer.singleShot(100, lambda: QMessageBox.information(self, "复制成功", message))
            
        except Exception as e:
            QMessageBox.critical(self, "复制失败", f"复制文件时出错:\n{str(e)}")
    
    def reload_resource(self, item):
        """重新载入资源"""
        if not item:
            return
            
        # 获取文件路径
        file_path = item.data(0, Qt.UserRole)
        if not file_path:
            QMessageBox.warning(self, "警告", "无法获取文件路径")
            return
            
        # 查找对应的资源
        target_resource = None
        for resource in self.project.get('resources', []):
            if resource['path'] == file_path:
                target_resource = resource
                break
                
        if not target_resource:
            QMessageBox.warning(self, "错误", "找不到对应的资源")
            return
            
        # 确认对话框
        reply = QMessageBox.question(
            self, "确认重新载入", 
            f"确定要重新载入资源 '{target_resource['name']}' 吗？\n\n这将移除当前资源并重新添加，可能会重置部分资源信息。",
            QMessageBox.Yes | QMessageBox.No
        )
        
        if reply != QMessageBox.Yes:
            return
            
        try:
            # 保存原始资源信息
            original_name = target_resource.get('name', '')
            original_path = target_resource.get('path', '')
            original_type = target_resource.get('type', '参考资料')
            original_description = target_resource.get('description', '')
            original_tags = target_resource.get('tags', '')
            
            # 从资源列表中移除
            self.project['resources'].remove(target_resource)
            
            # 重新添加资源（从文件路径重新提取完整文件名）
            new_file_name = os.path.basename(original_path)  # 从路径提取完整文件名（包含扩展名）
            new_resource = {
                'name': new_file_name,  # 使用从路径提取的完整文件名
                'path': original_path,
                'type': original_type,
                'description': original_description,
                'tags': original_tags,
                'added_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            
            # 添加到资源列表
            self.project['resources'].append(new_resource)
            
            # 记录项目日志
            self.parent_tool.add_project_log(
                self.project['name'], 
                "重新载入资源", 
                f"重新载入资源 '{new_file_name}'", 
                "资源"
            )
            
            # 保存数据
            self.parent_tool.update_project_modified_time(self.project['name'], save_immediately=False)
            self.parent_tool.save_data()
            self.parent_tool.refresh_project_list()
            
            # 刷新资源列表
            self.load_resources()
            # 更新tab标题中的数量
            self.update_tab_counts()
            
            # 显示成功消息
            message = f"✅ 资源 '{new_file_name}' 已重新载入"
            self.parent_tool.status_bar.showMessage(message)
            QMessageBox.information(self, "重新载入成功", message)
            
        except Exception as e:
            QMessageBox.critical(self, "重新载入失败", f"重新载入资源时出错:\n{str(e)}")
    
    def delete_resource_file(self, item):
        """删除资源文件"""
        if not item:
            return
            
        # 获取文件路径
        file_path = item.data(0, Qt.UserRole)
        if not file_path or not os.path.exists(file_path):
            QMessageBox.warning(self, "警告", "文件路径无效或文件不存在")
            return
            
        file_name = os.path.basename(file_path)
        
        # 确认删除
        reply = QMessageBox.question(
            self, "确认删除文件", 
            f"确定要删除文件吗？\n\n文件路径: {file_path}\n\n⚠️ 此操作将永久删除文件，无法恢复！",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No  # 默认选择"否"
        )
        
        if reply != QMessageBox.Yes:
            return
            
        try:
            # 删除文件
            os.remove(file_path)
            
            # 从资源列表中移除
            if 'resources' in self.project:
                self.project['resources'] = [
                    r for r in self.project['resources'] 
                    if r.get('path') != file_path
                ]
            
            # 记录项目日志
            self.parent_tool.add_project_log(self.project['name'], "删除文件", 
                                            f"删除文件 '{file_name}'", 
                                            "资源")
            
            # 保存数据（异步处理，避免阻塞UI）
            self.parent_tool.update_project_modified_time(self.project['name'], save_immediately=False)
            self.parent_tool.save_data()
            
            # 只刷新资源列表，不刷新整个项目列表
            self.load_resources()
            # 更新tab标题中的数量
            self.update_tab_counts()
            
            # 显示成功消息
            message = f"✅ 文件 '{file_name}' 已删除"
            self.parent_tool.status_bar.showMessage(message)
            
            # 使用定时器延迟显示消息框，避免阻塞
            QTimer.singleShot(100, lambda: QMessageBox.information(self, "删除成功", message))
            
        except Exception as e:
            QMessageBox.critical(self, "删除失败", f"删除文件时出错:\n{str(e)}")
    
    def handle_tree_item_click(self, item, column):
        """处理树形项目点击事件"""
        try:
            # 只处理第一列（资源名称列）的点击
            if column == 0:
                item_type = item.data(1, Qt.UserRole)
                if item_type == "folder":
                    # 获取点击位置
                    cursor_pos = QCursor.pos()
                    tree_pos = self.resource_tree.mapFromGlobal(cursor_pos)
                    item_rect = self.resource_tree.visualItemRect(item)
                    
                    # 检查是否点击了📁图标区域（假设图标在文本末尾）
                    item_text = item.text(0)
                    if "📁" in item_text:
                        # 计算📁图标的大概位置（文本末尾附近）
                        text_width = self.resource_tree.fontMetrics().width(item_text.replace("📁", ""))
                        icon_start_x = item_rect.x() + text_width - 20  # 图标大概位置
                        icon_end_x = item_rect.x() + text_width + 20
                        
                        # 如果点击位置在📁图标区域内
                        if icon_start_x <= tree_pos.x() <= icon_end_x:
                            folder_path = item.data(0, Qt.UserRole)
                            if folder_path and os.path.exists(folder_path):
                                # 打开文件夹
                                if sys.platform.startswith('win'):
                                    os.startfile(folder_path)
                                elif sys.platform.startswith('darwin'):  # macOS
                                    subprocess.run(['open', folder_path])
                                else:  # Linux
                                    subprocess.run(['xdg-open', folder_path])
                            else:
                                QMessageBox.warning(self, "警告", f"文件夹不存在: {folder_path}")
        except Exception as e:
            print(f"处理点击事件失败: {str(e)}")
    
    def refresh_folder_files(self, folder_item):
        """刷新指定文件夹下的文件"""
        folder_path = folder_item.data(0, Qt.UserRole)
        if not folder_path or not os.path.exists(folder_path):
            QMessageBox.warning(self, "警告", "文件夹路径无效或不存在")
            return
        
        # 重新加载资源列表
        self.load_resources()
        
        # 显示刷新成功消息
        folder_name = os.path.basename(folder_path)
        message = f"✅ 已刷新文件夹 '{folder_name}' 下的资源"
        self.parent_tool.status_bar.showMessage(message)
    
    def import_folder_files(self, folder_item):
        """导入指定文件夹下的所有文件"""
        folder_path = folder_item.data(0, Qt.UserRole)
        if not folder_path or not os.path.exists(folder_path):
            QMessageBox.warning(self, "警告", "文件夹路径无效或不存在")
            return
        
        # 获取文件夹下的所有文件
        try:
            all_files = []
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    # 过滤掉隐藏文件和系统文件
                    if not file.startswith('.') and os.path.isfile(file_path):
                        all_files.append(file_path)
            
            if not all_files:
                QMessageBox.information(self, "提示", "该文件夹下没有找到可导入的文件")
                return
            
            # 确认导入
            folder_name = os.path.basename(folder_path)
            reply = QMessageBox.question(self, "确认导入", 
                                       f"确定要导入文件夹 '{folder_name}' 下的 {len(all_files)} 个文件吗？",
                                       QMessageBox.Yes | QMessageBox.No)
            
            if reply != QMessageBox.Yes:
                return
            
            # 批量添加文件
            if 'resources' not in self.project:
                self.project['resources'] = []
            
            added_count = 0
            duplicate_count = 0
            
            for file_path in all_files:
                file_name = os.path.basename(file_path)
                
                # 规范化文件路径以避免路径格式差异导致的重复检测失败
                normalized_file_path = os.path.normpath(file_path)
                
                # 检查是否已存在
                is_duplicate = False
                for existing_resource in self.project['resources']:
                    existing_path = os.path.normpath(existing_resource.get('path', ''))
                    if existing_path == normalized_file_path:
                        duplicate_count += 1
                        is_duplicate = True
                        break
                
                if not is_duplicate:
                    # 创建资源数据
                    resource_data = {
                        'name': file_name,
                        'path': file_path,
                        'type': '',  # 可以根据文件扩展名自动判断类型
                        'description': ''
                    }
                    
                    self.project['resources'].append(resource_data)
                    added_count += 1
            
            # 保存数据并刷新
            self.parent_tool.update_project_modified_time(self.project['name'], save_immediately=False)
            self.parent_tool.save_data()
            self.parent_tool.refresh_project_list()
            self.load_resources()
            
            # 显示结果
            message = f"✅ 成功导入 {added_count} 个文件到项目 '{self.project['name']}'"
            if duplicate_count > 0:
                message += f"，跳过 {duplicate_count} 个重复文件"
            
            self.parent_tool.status_bar.showMessage(message)
            QMessageBox.information(self, "导入完成", message)
            
        except Exception as e:
            QMessageBox.critical(self, "导入失败", f"导入文件时发生错误：\n{str(e)}")
        
    def get_file_icon(self, file_path):
        """根据文件扩展名获取图标"""
        if not os.path.exists(file_path):
            return "❌"
        
        _, ext = os.path.splitext(file_path.lower())
        icon_map = {
            '.pdf': '📄',
            '.doc': '📝', '.docx': '📝',
            '.txt': '📃', '.md': '📃',
            '.py': '🐍', '.js': '📜', '.html': '🌐', '.css': '🎨',
            '.mp4': '🎬', '.avi': '🎬', '.mkv': '🎬', '.mov': '🎬',
            '.jpg': '🖼️', '.png': '🖼️', '.gif': '🖼️',
            '.zip': '📦', '.rar': '📦',
            '.exe': '⚙️',
            '.url': '🔗'
        }
        return icon_map.get(ext, '📄')
    
    def get_file_time_info(self, file_path):
        """获取文件时间信息"""
        try:
            if os.path.exists(file_path):
                mtime = os.path.getmtime(file_path)
                return datetime.fromtimestamp(mtime).strftime('%Y-%m-%d %H:%M')
            else:
                return "文件不存在"
        except:
            return "未知时间"
    
    def get_file_modification_time(self, file_path):
        """获取文件修改时间戳"""
        try:
            if os.path.exists(file_path):
                return os.path.getmtime(file_path)
            else:
                return 0
        except:
            return 0
    
    def is_recently_modified(self, timestamp):
        """判断文件是否在24小时内修改过"""
        if timestamp == 0:
            return False
        current_time = datetime.now().timestamp()
        return (current_time - timestamp) < 86400  # 24小时 = 86400秒
    
    def open_resource_file(self, item, column):
        """双击打开资源文件"""
        file_path = item.data(0, Qt.UserRole)
        display_name = item.text(0)
        
        # 从项目资源中找到真正的资源名称
        real_resource_name = None
        for resource in self.project.get('resources', []):
            if resource.get('path') == file_path:
                real_resource_name = resource.get('name')
                break
        
        # 如果找不到真正的资源名称，使用显示名称去除装饰符号
        if not real_resource_name:
            # 移除图标和装饰符号，提取文件名
            import re
            clean_name = re.sub(r'[📄📁📂📦🔥🔖]|\s+', ' ', display_name).strip()
            real_resource_name = clean_name
        
        if file_path and os.path.exists(file_path):
            try:
                # 记录最近打开的资源到项目笔记
                self.record_recently_opened_resource(real_resource_name, file_path)
                
                # 打开文件
                if sys.platform.startswith('win'):
                    os.startfile(file_path)
                elif sys.platform.startswith('darwin'):  # macOS
                    subprocess.run(['open', file_path])
                else:  # Linux
                    subprocess.run(['xdg-open', file_path])
                    
                # 刷新资源列表，以显示最近打开的资源标记
                self.load_resources()
                    
                # 更新状态栏消息
                self.parent_tool.status_bar.showMessage(f"📂 已打开资源: {real_resource_name}")
                
            except Exception as e:
                QMessageBox.warning(self, "打开失败", f"无法打开文件:\n{str(e)}")
        else:
            # 文件不存在，弹出重新链接对话框
            self.relink_resource(item, real_resource_name, file_path)
    
    def relink_resource(self, item, resource_name, old_file_path):
        """重新链接失效的资源文件"""
        dialog = RelinkResourceDialog(self, resource_name, old_file_path)
        if dialog.exec_() == QDialog.Accepted:
            new_file_path = dialog.get_new_file_path()
            if new_file_path and os.path.exists(new_file_path):
                # 更新当前项目数据中的文件路径
                resource_updated = False
                for resource in self.project.get('resources', []):
                    if resource.get('path') == old_file_path:
                        resource['path'] = new_file_path
                        resource_updated = True
                        break
                
                # 同步更新父工具中的项目数据
                if resource_updated:
                    project_name = self.project.get('name')
                    for parent_project in self.parent_tool.projects:
                        if parent_project.get('name') == project_name:
                            for parent_resource in parent_project.get('resources', []):
                                if parent_resource.get('path') == old_file_path:
                                    parent_resource['path'] = new_file_path
                                    break
                            break
                
                # 保存数据
                self.parent_tool.update_project_modified_time(self.project['name'], save_immediately=False)
                self.parent_tool.save_data()
                
                # 刷新资源列表
                self.load_resources()
                
                # 更新状态栏消息
                self.parent_tool.status_bar.showMessage(f"✅ 已重新链接资源: {resource_name}")
                
                # 询问是否立即打开文件
                reply = QMessageBox.question(self, "重新链接成功", 
                                            f"资源 '{resource_name}' 已成功重新链接到:\n{new_file_path}\n\n是否立即打开该文件？",
                                            QMessageBox.Yes | QMessageBox.No)
                if reply == QMessageBox.Yes:
                    try:
                        # 记录最近打开的资源到项目笔记
                        self.record_recently_opened_resource(resource_name, new_file_path)
                        
                        # 打开文件
                        if sys.platform.startswith('win'):
                            os.startfile(new_file_path)
                        elif sys.platform.startswith('darwin'):  # macOS
                            subprocess.run(['open', new_file_path])
                        else:  # Linux
                            subprocess.run(['xdg-open', new_file_path])
                            
                        # 刷新资源列表
                        self.load_resources()
                        
                    except Exception as e:
                        QMessageBox.warning(self, "打开失败", f"无法打开文件:\n{str(e)}")
            else:
                QMessageBox.warning(self, "重新链接失败", "选择的文件路径无效或文件不存在")
    
    def record_recently_opened_resource(self, resource_name, file_path):
        """记录最近打开的资源到项目笔记中"""
        try:
            # 更新类属性，以便界面立即显示最近打开的资源
            self.recently_opened_resource = resource_name
            
            # 获取项目文件夹路径
            folder_path = self.project.get('folder_path', '')
            if not folder_path or not os.path.exists(folder_path):
                return
            
            # 构建笔记文件路径
            project_name = self.project['name']
            safe_name = "".join(c for c in project_name if c.isalnum() or c in (' ', '-', '_', '（', '）', '(', ')')).strip()
            if not safe_name:
                safe_name = "新项目"
            notes_file = os.path.join(folder_path, f"{safe_name}_笔记.md")
            
            # 如果笔记文件不存在，创建基础结构
            if not os.path.exists(notes_file):
                self.parent_tool.create_project_notes_file(project_name, notes_file)
            
            # 读取现有内容
            with open(notes_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 创建最近打开资源的日志条目（带特殊标识）
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            recent_marker = "🔖 [最近打开]"
            log_entry = f"- **{timestamp}** {recent_marker} 打开资源: {resource_name}\n"
            
            # 查找或创建项目日志部分
            log_section_marker = "## 项目日志\n"
            if log_section_marker in content:
                # 移除之前的最近打开记录（只保留一个）
                lines = content.split('\n')
                filtered_lines = []
                for line in lines:
                    if recent_marker not in line:
                        filtered_lines.append(line)
                content = '\n'.join(filtered_lines)
                
                # 在现有日志部分的开头插入新的最近打开记录
                parts = content.split(log_section_marker, 1)
                if len(parts) == 2:
                    before_log = parts[0] + log_section_marker
                    after_log = parts[1]
                    content = before_log + "\n" + log_entry + after_log
                else:
                    # 如果分割失败，在文件末尾添加
                    content += "\n" + log_section_marker + "\n" + log_entry
            else:
                # 在文件末尾添加日志部分
                content += "\n" + log_section_marker + "\n" + log_entry
            
            # 写回文件
            with open(notes_file, 'w', encoding='utf-8') as f:
                f.write(content)
                
        except Exception as e:
            logging.error(f"记录最近打开资源失败: {e}")
    
    def add_resource(self):
        """添加资源"""
        dialog = AddResourceDialog(self, self.parent_tool.resource_categories, self.parent_tool.resource_types)
        if dialog.exec_() == QDialog.Accepted:
            if 'resources' not in self.project:
                self.project['resources'] = []
            
            # 检查是否是批量添加
            if hasattr(dialog, 'batch_resources_data') and dialog.batch_resources_data:
                # 批量添加资源
                added_count = 0
                duplicate_count = 0
                
                for resource_data in dialog.batch_resources_data:
                    resource_name = resource_data.get('name', '')
                    resource_path = resource_data.get('path', '')
                    
                    # 检查重复（通过名称或路径）
                    is_duplicate = False
                    normalized_resource_path = os.path.normpath(resource_path) if resource_path else ''
                    for existing_resource in self.project['resources']:
                        existing_path = os.path.normpath(existing_resource.get('path', ''))
                        if (existing_resource.get('name') == resource_name and resource_name) or \
                           (existing_path == normalized_resource_path and normalized_resource_path):
                            duplicate_count += 1
                            is_duplicate = True
                            break
                    
                    if not is_duplicate:
                        self.project['resources'].append(resource_data)
                        added_count += 1
                
                # 记录项目日志
                if added_count > 0:
                    self.parent_tool.add_project_log(self.project['name'], "批量添加资源", 
                                                    f"批量添加 {added_count} 个资源", 
                                                    "资源")
                
                # 更新资源总数字段
                self.project['resource_count'] = len(self.project['resources'])
                
                self.parent_tool.update_project_modified_time(self.project['name'], save_immediately=False)
                self.parent_tool.save_data()
                self.parent_tool.refresh_project_list()
                
                # 显示批量添加结果
                message = f"✅ 成功添加 {added_count} 个资源到项目 '{self.project['name']}'"                
                if duplicate_count > 0:
                    message += f"，跳过 {duplicate_count} 个重复资源"
                self.parent_tool.status_bar.showMessage(message)
                
                # 显示toast提示
                try:
                    toast = QLabel(message, self)
                    toast.setStyleSheet("""
                        QLabel {
                            background-color: rgba(0, 0, 0, 0.7);
                            color: white;
                            padding: 10px 20px;
                            border-radius: 4px;
                            font-size: 14px;
                        }
                    """)
                    toast.adjustSize()
                    
                    # 计算位置（居中显示）
                    x = (self.width() - toast.width()) // 2
                    y = self.height() - toast.height() - 40  # 底部上方40像素
                    toast.move(x, y)
                    
                    # 显示提示
                    toast.show()
                    
                    # 设置定时器在指定时间后隐藏并删除提示
                    QTimer.singleShot(2000, lambda: (toast.hide(), toast.deleteLater()))
                except Exception as e:
                    print(f"显示Toast提示失败: {str(e)}")
            else:
                # 单个资源添加
                resource_data = dialog.get_resource_data()
                resource_name = resource_data.get('name', '')
                resource_path = resource_data.get('path', '')
                
                # 检查重复（通过名称或路径）
                normalized_resource_path = os.path.normpath(resource_path) if resource_path else ''
                for existing_resource in self.project['resources']:
                    existing_path = os.path.normpath(existing_resource.get('path', ''))
                    if (existing_resource.get('name') == resource_name and resource_name) or \
                       (existing_path == normalized_resource_path and normalized_resource_path):
                        QMessageBox.warning(self, "重复资源", 
                                          f"资源 '{resource_name}' 已存在于项目中，无法重复添加。")
                        return
                
                # 添加资源
                self.project['resources'].append(resource_data)
                
                # 记录项目日志
                self.parent_tool.add_project_log(self.project['name'], "添加资源", 
                                                f"添加资源: {resource_data['name']}", 
                                                "资源")
                
                # 更新资源总数字段
                self.project['resource_count'] = len(self.project['resources'])
                
                self.parent_tool.update_project_modified_time(self.project['name'], save_immediately=False)
                self.parent_tool.save_data()
                self.parent_tool.refresh_project_list()
                
                # 显示状态栏消息
                message = f"✅ 资源 '{resource_data['name']}' 已添加到项目 '{self.project['name']}'"                
                self.parent_tool.status_bar.showMessage(message)
                
                # 显示toast提示
                try:
                    toast = QLabel(message, self)
                    toast.setStyleSheet("""
                        QLabel {
                            background-color: rgba(0, 0, 0, 0.7);
                            color: white;
                            padding: 10px 20px;
                            border-radius: 4px;
                            font-size: 14px;
                        }
                    """)
                    toast.adjustSize()
                    
                    # 计算位置（居中显示）
                    x = (self.width() - toast.width()) // 2
                    y = self.height() - toast.height() - 40  # 底部上方40像素
                    toast.move(x, y)
                    
                    # 显示提示
                    toast.show()
                    
                    # 设置定时器在指定时间后隐藏并删除提示
                    QTimer.singleShot(2000, lambda: (toast.hide(), toast.deleteLater()))
                except Exception as e:
                    print(f"显示Toast提示失败: {str(e)}")
            
            # 刷新资源列表
            self.load_resources()
            # 更新tab标题中的数量
            self.update_tab_counts()
    
    def create_file_in_project(self):
        """在项目文件夹中创建新文件"""
        try:
            # 检查项目是否有文件夹路径
            folder_path = self.project.get('folder_path', '')
            if not folder_path:
                QMessageBox.warning(self, "警告", "项目没有设置文件夹路径，无法创建文件。")
                return
            
            # 检查文件夹是否存在
            if not os.path.exists(folder_path):
                reply = QMessageBox.question(self, "文件夹不存在", 
                                            f"项目文件夹 '{folder_path}' 不存在，是否创建？",
                                            QMessageBox.Yes | QMessageBox.No)
                if reply == QMessageBox.Yes:
                    try:
                        os.makedirs(folder_path, exist_ok=True)
                    except Exception as e:
                        QMessageBox.critical(self, "错误", f"创建文件夹失败：{str(e)}")
                        return
                else:
                    return
            
            # 导入CreateTool类
            try:
                from create_tool import CreateTool
            except ImportError:
                QMessageBox.critical(self, "错误", "无法导入创作助手工具，请确保create_tool.py文件存在。")
                return
            
            # 创建CreateTool实例
            create_tool = CreateTool()
            
            # 设置路径集合配置
            collection_name = "知识项目集合"  # 统一的集合名称
            
            # 确保配置结构存在
            if 'pathCollections' not in create_tool.config:
                create_tool.config['pathCollections'] = {'collections': {}}
            if 'collections' not in create_tool.config['pathCollections']:
                create_tool.config['pathCollections']['collections'] = {}
            
            # 获取或创建知识项目集合
            if collection_name not in create_tool.config['pathCollections']['collections']:
                create_tool.config['pathCollections']['collections'][collection_name] = {
                    'paths': [],
                    'creation_time': datetime.now().isoformat()
                }
            
            # 获取现有的路径集合
            existing_paths = create_tool.config['pathCollections']['collections'][collection_name].get('paths', [])
            
            # 检查当前项目路径是否已在集合中
            if folder_path not in existing_paths:
                existing_paths.append(folder_path)
                create_tool.config['pathCollections']['collections'][collection_name]['paths'] = existing_paths
            
            # 保存配置
            create_tool.save_config()
            
            # 设置当前选中的集合和路径
            if hasattr(create_tool, 'collection_combo') and create_tool.collection_combo:
                # 清空并重新添加集合选项
                create_tool.collection_combo.clear()
                create_tool.collection_combo.addItem("选择集合...")
                collections = create_tool.config.get('pathCollections', {}).get('collections', {})
                for collection_name_item in collections.keys():
                    create_tool.collection_combo.addItem(collection_name_item)
                
                # 设置知识项目集合为选中状态
                index = create_tool.collection_combo.findText(collection_name)
                if index >= 0:
                    create_tool.collection_combo.setCurrentIndex(index)
                    
                    # 更新路径下拉框
                    if hasattr(create_tool, 'update_paths'):
                        create_tool.update_paths(collection_name)
                    
                    # 设置默认路径为当前项目路径
                    if hasattr(create_tool, 'path_combo') and create_tool.path_combo:
                        path_index = create_tool.path_combo.findText(folder_path)
                        if path_index >= 0:
                            create_tool.path_combo.setCurrentIndex(path_index)
                            # 主动触发文件树更新
                            if hasattr(create_tool, 'update_file_tree'):
                                create_tool.update_file_tree(folder_path)
                            # 如果没有update_file_tree方法，尝试触发on_path_changed
                            elif hasattr(create_tool, 'on_path_changed'):
                                create_tool.on_path_changed(folder_path)
            
            # 连接文件创建成功的信号
            create_tool.file_created.connect(lambda file_path: self.on_file_created(file_path))
            
            # 记录项目日志
            self.parent_tool.add_project_log(self.project['name'], "打开创作助手", 
                                            f"打开创作助手工具，项目路径：{folder_path}", 
                                            "操作")
            
            # 显示创作助手工具，确保在前台显示
            # 使用最佳实践：show() + raise_() + activateWindow() + WindowStaysOnTopHint
            create_tool.setWindowFlags(create_tool.windowFlags() | Qt.WindowStaysOnTopHint)
            create_tool.show()
            create_tool.raise_()
            create_tool.activateWindow()
            
            # 使用QTimer确保窗口获得焦点并再次触发文件树更新
            def final_setup():
                create_tool.raise_()
                create_tool.activateWindow()
                create_tool.setWindowFlags(create_tool.windowFlags() & ~Qt.WindowStaysOnTopHint)
                create_tool.show()
                # 再次确保文件树更新
                if hasattr(create_tool, 'update_file_tree'):
                    create_tool.update_file_tree(folder_path)
                elif hasattr(create_tool, 'refresh_file_tree'):
                    create_tool.refresh_file_tree()
            
            QTimer.singleShot(100, final_setup)
            
            # 现在有了文件创建回调，文件创建后会自动添加到项目资源中
            # 使用状态栏消息代替弹窗提示
            self.parent_tool.status_bar.showMessage(f"📝 创作助手已打开，创建文件后将自动添加到项目资源中")
            
        except Exception as e:
            QMessageBox.critical(self, "错误", f"打开创作助手失败：{str(e)}")
            logging.error(f"打开创作助手失败: {e}")
    
    def on_file_created(self, file_path):
        """文件创建成功的回调函数"""
        try:
            if not file_path or not os.path.exists(file_path):
                return
            
            # 获取文件信息
            file_name = os.path.basename(file_path)
            file_ext = os.path.splitext(file_path)[1].lower()
            
            # 确定资源类型（默认为空）
            resource_type = ''
            
            # 创建资源数据
            resource_data = {
                'name': file_name,
                'path': file_path,
                'type': resource_type,
                'category': '默认',
                'description': f'通过创作助手创建的文件',
                'tags': [],
                'created_time': datetime.now().isoformat(),
                'modified_time': datetime.now().isoformat(),
                'added_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            
            # 检查是否已存在
            if 'resources' not in self.project:
                self.project['resources'] = []
            
            # 检查重复
            normalized_file_path = os.path.normpath(file_path)
            for existing_resource in self.project['resources']:
                existing_path = os.path.normpath(existing_resource.get('path', ''))
                if existing_path == normalized_file_path:
                    # 文件已存在于项目资源中
                    return
            
            # 添加到项目资源
            self.project['resources'].append(resource_data)
            
            # 更新资源总数字段
            self.project['resource_count'] = len(self.project['resources'])
            
            # 记录项目日志
            self.parent_tool.add_project_log(self.project['name'], "创建文件", 
                                            f"通过创作助手创建文件：{file_name}", 
                                            "文件")
            
            # 保存数据
            self.parent_tool.update_project_modified_time(self.project['name'], save_immediately=False)
            self.parent_tool.save_data()
            self.parent_tool.refresh_project_list()
            
            # 刷新资源列表
            self.load_resources()
            self.update_tab_counts()
            
            # 显示成功消息
            message = f"✅ 文件 '{file_name}' 已创建并添加到项目资源中"
            self.parent_tool.status_bar.showMessage(message)
            
        except Exception as e:
            logging.error(f"文件创建回调处理失败: {e}")
    
    def remove_resource(self):
        """移除资源"""
        if 'resources' not in self.project or not self.project['resources']:
            QMessageBox.warning(self, "警告", "当前项目没有资源")
            return
        
        # 显示资源选择对话框
        resource_names = [res['name'] for res in self.project['resources']]
        resource_name, ok = QInputDialog.getItem(self, "选择资源", "请选择要移除的资源:", resource_names, 0, False)
        if not ok:
            return
        
        reply = QMessageBox.question(self, "确认移除", 
                                   f"确定要移除资源 '{resource_name}' 吗？",
                                   QMessageBox.Yes | QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            # 找到并移除资源
            for i, resource in enumerate(self.project['resources']):
                if resource['name'] == resource_name:
                    del self.project['resources'][i]
                    break
            
            # 更新资源总数字段
            self.project['resource_count'] = len(self.project['resources'])
            
            # 记录项目日志
            self.parent_tool.add_project_log(self.project['name'], "移除资源", 
                                            f"移除资源: {resource_name}", 
                                            "资源")
            
            self.parent_tool.update_project_modified_time(self.project['name'], save_immediately=False)
            self.parent_tool.save_data()
            self.parent_tool.refresh_project_list()
            # 重新加载资源树，这会自动清理空的类型文件夹
            self.load_resources()
            # 更新tab标题中的数量
            self.update_tab_counts()
            
            # 显示成功消息
            self.parent_tool.status_bar.showMessage(f"✅ 资源 '{resource_name}' 已从项目中移除")
    
    def clear_invalid_resources(self):
        """清除所有无效资源（文件路径不存在的资源）"""
        if 'resources' not in self.project or not self.project['resources']:
            QMessageBox.information(self, "提示", "当前项目没有资源")
            return
        
        # 检查所有资源，找出无效资源
        invalid_resources = []
        for resource in self.project['resources']:
            resource_path = resource.get('path', '')
            if not resource_path or not os.path.exists(resource_path):
                invalid_resources.append(resource)
        
        # 如果没有无效资源
        if not invalid_resources:
            QMessageBox.information(self, "提示", "当前项目没有无效资源")
            return
        
        # 显示确认对话框
        invalid_count = len(invalid_resources)
        total_count = len(self.project['resources'])
        message = f"检测到 {invalid_count} 个无效资源（文件路径不存在）\n\n"
        message += f"总资源数: {total_count}\n"
        message += f"无效资源数: {invalid_count}\n\n"
        message += "确定要清除所有无效资源吗？"
        
        reply = QMessageBox.question(self, "确认清除", 
                                   message,
                                   QMessageBox.Yes | QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            # 在父工具的项目列表中找到对应的项目并更新
            project_name = self.project['name']
            for parent_project in self.parent_tool.projects:
                if parent_project.get('name') == project_name:
                    # 更新父工具中的项目资源列表
                    parent_project['resources'] = [
                        resource for resource in parent_project.get('resources', [])
                        if resource.get('path', '') and os.path.exists(resource.get('path', ''))
                    ]
                    # 更新资源总数字段
                    parent_project['resource_count'] = len(parent_project['resources'])
                    break
            
            # 同步更新当前对话框的项目数据
            self.project['resources'] = [
                resource for resource in self.project['resources']
                if resource.get('path', '') and os.path.exists(resource.get('path', ''))
            ]
            self.project['resource_count'] = len(self.project['resources'])
            
            # 记录项目日志
            log_message = f"清除了 {invalid_count} 个无效资源"
            self.parent_tool.add_project_log(self.project['name'], "清除无效资源", 
                                            log_message, 
                                            "资源")
            
            # 更新项目修改时间并保存数据
            self.parent_tool.update_project_modified_time(self.project['name'], save_immediately=False)
            self.parent_tool.save_data(create_backup=True)
            self.parent_tool.refresh_project_list()
            
            # 刷新资源树
            self.load_resources()
            # 更新tab标题中的数量
            self.update_tab_counts()
            
            # 在状态栏显示成功消息（移除弹窗）
            self.parent_tool.status_bar.showMessage(f"✅ 已清除 {invalid_count} 个无效资源", 5000)
    
    def delete_resource_from_tree(self, item):
        """从树视图中删除资源"""
        if not item:
            return
            
        # 获取文件路径
        file_path = item.data(0, Qt.UserRole)
        if not file_path:
            return
            
        # 获取资源名称
        item_text = item.text(0)
        # 去除图标和最近修改标记
        resource_name = item_text.split(' ', 1)[1].split(' 🔥', 1)[0] if ' ' in item_text else item_text
        
        reply = QMessageBox.question(self, "确认删除", 
                                   f"确定要删除资源 '{resource_name}' 吗？",
                                   QMessageBox.Yes | QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            # 找到并移除资源
            for i, resource in enumerate(self.project['resources']):
                if resource['path'] == file_path:
                    del self.project['resources'][i]
                    
                    # 更新资源总数字段
                    self.project['resource_count'] = len(self.project['resources'])
                    
                    # 记录项目日志
                    self.parent_tool.add_project_log(self.project['name'], "删除资源", 
                                                    f"删除资源: {resource_name}", 
                                                    "资源")
                    
                    # 更新项目修改时间并保存数据
                    self.parent_tool.update_project_modified_time(self.project['name'], save_immediately=False)
                    self.parent_tool.save_data(create_backup=True)  # 删除资源时创建备份
                    self.parent_tool.refresh_project_list()
                    
                    # 刷新资源树
                    self.load_resources()
                    # 更新tab标题中的数量
                    self.update_tab_counts()
                    
                    # 显示成功消息
                    self.parent_tool.status_bar.showMessage(f"✅ 资源 '{resource_name}' 已从项目 '{self.project['name']}' 中删除")
                    return
            
            # 如果没有找到资源
            QMessageBox.warning(self, "删除失败", "找不到要删除的资源")
    
    def remove_entire_folder(self, folder_item):
        """移除整个文件夹及其所有文件"""
        if not folder_item:
            return
            
        # 获取文件夹路径和名称
        folder_path = folder_item.data(0, Qt.UserRole)
        folder_text = folder_item.text(0)
        
        # 提取文件夹名称（去除图标和文件数量信息）
        import re
        folder_name_match = re.search(r'📂\s*([^(]+)', folder_text)
        folder_name = folder_name_match.group(1).strip() if folder_name_match else "未知文件夹"
        
        # 统计该文件夹下的文件数量
        files_to_remove = []
        if 'resources' in self.project:
            for resource in self.project['resources']:
                resource_folder = os.path.dirname(resource['path'])
                resource_folder_name = os.path.basename(resource_folder) if resource_folder else '根目录'
                
                # 如果资源属于当前文件夹
                if resource_folder_name == folder_name or (folder_name == '根目录' and not resource_folder):
                    files_to_remove.append(resource)
        
        if not files_to_remove:
            QMessageBox.information(self, "提示", f"文件夹 '{folder_name}' 下没有找到任何资源")
            return
        
        # 确认删除
        reply = QMessageBox.question(self, "确认删除", 
                                   f"确定要移除文件夹 '{folder_name}' 及其下的 {len(files_to_remove)} 个文件吗？\n\n" +
                                   "这将从项目中移除以下文件：\n" +
                                   "\n".join([f"• {os.path.basename(f['path'])}" for f in files_to_remove[:10]]) +
                                   (f"\n... 还有 {len(files_to_remove) - 10} 个文件" if len(files_to_remove) > 10 else ""),
                                   QMessageBox.Yes | QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            # 移除所有文件
            removed_count = 0
            for resource_to_remove in files_to_remove:
                for i, resource in enumerate(self.project['resources']):
                    if resource['path'] == resource_to_remove['path']:
                        del self.project['resources'][i]
                        removed_count += 1
                        break
            
            # 更新资源总数字段
            self.project['resource_count'] = len(self.project['resources'])
            
            # 更新项目修改时间并保存数据
            self.parent_tool.update_project_modified_time(self.project['name'], save_immediately=False)
            self.parent_tool.save_data(create_backup=True)  # 移除整个文件夹时创建备份
            self.parent_tool.refresh_project_list()
            
            # 刷新资源树
            self.load_resources()
            # 更新tab标题中的数量
            self.update_tab_counts()
            
            # 显示成功消息
            message = f"✅ 已从项目 '{self.project['name']}' 中移除文件夹 '{folder_name}' 及其下的 {removed_count} 个文件"
            self.parent_tool.status_bar.showMessage(message)
            QMessageBox.information(self, "删除完成", message)
    
    def add_folder_description(self, folder_item):
        """添加或编辑文件夹描述"""
        if not folder_item:
            return
            
        # 获取文件夹路径
        folder_path = folder_item.data(0, Qt.UserRole)
        if not folder_path or not os.path.exists(folder_path):
            QMessageBox.warning(self, "警告", "文件夹路径无效或不存在")
            return
            
        folder_name = os.path.basename(folder_path)
        
        # 获取当前描述（如果存在）
        current_desc = self.get_folder_description(folder_path)
        
        # 弹出输入对话框
        desc, ok = QInputDialog.getText(
            self, "文件夹描述", 
            f"请输入文件夹 '{folder_name}' 的描述:", 
            QLineEdit.Normal, current_desc
        )
        
        if ok:
            # 保存文件夹描述
            self.save_folder_description(folder_path, desc.strip())
            
            # 刷新资源列表以显示新的描述
            self.load_resources()
            
            # 显示成功消息
            if desc.strip():
                message = f"✅ 已为文件夹 '{folder_name}' 添加描述"
            else:
                message = f"✅ 已清除文件夹 '{folder_name}' 的描述"
            self.parent_tool.status_bar.showMessage(message)
    
    def get_folder_description(self, folder_path):
        """获取文件夹描述"""
        if not hasattr(self.project, 'folder_descriptions'):
            if 'folder_descriptions' not in self.project:
                self.project['folder_descriptions'] = {}
        
        return self.project.get('folder_descriptions', {}).get(folder_path, '')
    
    def save_folder_description(self, folder_path, description):
        """保存文件夹描述"""
        if 'folder_descriptions' not in self.project:
            self.project['folder_descriptions'] = {}
        
        if description:
            self.project['folder_descriptions'][folder_path] = description
        else:
            # 如果描述为空，删除该条目
            self.project['folder_descriptions'].pop(folder_path, None)
        
        # 记录项目日志
        folder_name = os.path.basename(folder_path)
        if description:
            self.parent_tool.add_project_log(self.project['name'], "添加文件夹描述", 
                                            f"为文件夹 '{folder_name}' 添加描述: {description}", 
                                            "操作")
        else:
            self.parent_tool.add_project_log(self.project['name'], "清除文件夹描述", 
                                            f"清除文件夹 '{folder_name}' 的描述", 
                                            "操作")
        
        # 保存数据
        self.parent_tool.update_project_modified_time(self.project['name'], save_immediately=False)
        self.parent_tool.save_data()
        self.parent_tool.refresh_project_list()
    
    def open_folder(self, folder_path):
        """在文件资源管理器中打开文件夹"""
        if not folder_path or not os.path.exists(folder_path):
            QMessageBox.warning(self, "警告", "文件夹路径无效或不存在")
            return
            
        try:
            import platform
            system = platform.system()
            
            if system == "Windows":
                os.startfile(folder_path)
            elif system == "Darwin":  # macOS
                subprocess.run(["open", folder_path])
            else:  # Linux
                subprocess.run(["xdg-open", folder_path])
                
            # 显示成功消息
            folder_name = os.path.basename(folder_path)
            message = f"✅ 已打开文件夹 '{folder_name}'"
            self.parent_tool.status_bar.showMessage(message)
            
        except Exception as e:
            QMessageBox.critical(self, "错误", f"无法打开文件夹: {str(e)}")
    
    def update_resource_groups_after_drop(self):
        """拖放后更新资源分组，并移动实际文件"""
        # 获取当前树视图中的所有资源项
        resources_data = []
        file_moves = []  # 记录需要移动的文件
        
        # 遍历所有顶级项（文件夹）
        for i in range(self.resource_tree.topLevelItemCount()):
            group_item = self.resource_tree.topLevelItem(i)
            group_name = group_item.text(0).split(' (')[0].strip()
            
            # 获取文件夹名称（去除📂图标）
            folder_name = group_name[2:].strip() if group_name.startswith('📂') else group_name
            
            # 遍历该组下的所有资源
            for j in range(group_item.childCount()):
                resource_item = group_item.child(j)
                file_path = resource_item.data(0, Qt.UserRole)
                
                if file_path and os.path.exists(file_path):
                    # 查找原始资源数据
                    for resource in self.project['resources']:
                        if resource['path'] == file_path:
                            # 创建资源数据副本
                            resource_data = resource.copy()
                            original_path = resource['path']
                            
                            # 保留原始资源类型
                            resource_type = resource.get('type', '')
                            resource_data['type'] = resource_type
                            
                            # 检查文件是否需要移动到新文件夹
                            if folder_name != '根目录':
                                # 获取当前文件所在文件夹
                                current_folder = os.path.dirname(original_path)
                                current_folder_name = os.path.basename(current_folder)
                                
                                # 如果当前文件夹名与目标文件夹名不同，需要移动文件
                                if current_folder_name != folder_name:
                                    # 查找目标文件夹路径
                                    parent_folder = os.path.dirname(current_folder)
                                    target_folder = os.path.join(parent_folder, folder_name)
                                    
                                    # 确保目标文件夹存在
                                    if not os.path.exists(target_folder):
                                        try:
                                            os.makedirs(target_folder, exist_ok=True)
                                        except Exception as e:
                                            QMessageBox.warning(self, "创建文件夹失败", 
                                                              f"无法创建文件夹 '{target_folder}':\n{str(e)}")
                                            continue
                                    
                                    # 构建目标文件路径
                                    file_name = os.path.basename(original_path)
                                    target_path = os.path.join(target_folder, file_name)
                                    
                                    # 记录需要移动的文件
                                    file_moves.append((original_path, target_path, resource_data))
                                    
                                    # 更新资源路径
                                    resource_data['path'] = target_path
                            
                            resources_data.append(resource_data)
                            break
        
        # 执行文件移动操作
        moved_files = 0
        for src_path, dst_path, resource_data in file_moves:
            try:
                # 检查目标文件是否已存在
                if os.path.exists(dst_path):
                    # 生成唯一文件名
                    base_name, ext = os.path.splitext(os.path.basename(dst_path))
                    counter = 1
                    while os.path.exists(dst_path):
                        new_name = f"{base_name}_{counter}{ext}"
                        dst_path = os.path.join(os.path.dirname(dst_path), new_name)
                        counter += 1
                    
                    # 更新资源路径
                    resource_data['path'] = dst_path
                
                # 移动文件
                shutil.move(src_path, dst_path)
                moved_files += 1
            except Exception as e:
                QMessageBox.warning(self, "移动文件失败", 
                                  f"无法移动文件 '{src_path}' 到 '{dst_path}':\n{str(e)}")
        
        # 更新项目资源数据
        if resources_data:
            self.project['resources'] = resources_data
            self.parent_tool.update_project_modified_time(self.project['name'], save_immediately=False)
            self.parent_tool.save_data()
            self.parent_tool.refresh_project_list()  # 刷新整个项目列表
            
            # 显示成功消息
            message = f"✅ 项目 '{self.project['name']}' 的资源分组已更新"
            if moved_files > 0:
                message += f"，{moved_files} 个文件已移动到对应文件夹"
            self.parent_tool.status_bar.showMessage(message)
            
            # 刷新资源树
            self.load_resources()
    
    def refresh_resources(self):
        """刷新资源"""
        self.load_resources()


class ResourceTypeConfigDialog(QDialog):
    """资源文件类型配置对话框"""
    
    def __init__(self, parent=None, resource_types=None):
        super().__init__(parent)
        self.resource_types = resource_types.copy() if resource_types else {}
        self.init_ui()
    
    def init_ui(self):
        """初始化UI"""
        self.setWindowTitle("资源文件类型配置")
        width, height = get_optimal_dialog_size(800, 600)
        self.setFixedSize(width, height)
        center_window(self)
        
        # 设置对话框样式
        self.setStyleSheet("""
            QDialog {
                background-color: #f8f9fa;
            }
        """)
        
        main_layout = QVBoxLayout(self)
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(0, 0, 0, 0)
        
        # 创建内容区域
        content_widget = QFrame()
        content_widget.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 12px;
                margin: 20px;
            }
        """)
        
        content_layout = QVBoxLayout(content_widget)
        content_layout.setSpacing(20)
        content_layout.setContentsMargins(28, 28, 28, 28)
        
        # 标题
        title_label = QLabel("⚙️ 资源文件类型配置")
        title_label.setStyleSheet("""
            QLabel {
                font-size: 20px;
                font-weight: bold;
                color: #1a1a1a;
                margin-bottom: 10px;
            }
        """)
        content_layout.addWidget(title_label)
        
        # 说明文字
        desc_label = QLabel("配置不同文件类型资源的默认路径和支持的文件扩展名")
        desc_label.setStyleSheet("""
            QLabel {
                font-size: 14px;
                color: #666;
                margin-bottom: 10px;
            }
        """)
        content_layout.addWidget(desc_label)
        
        # 资源类型表格
        self.type_table = QTableWidget()
        self.type_table.setColumnCount(3)
        self.type_table.setHorizontalHeaderLabels(["类型名称", "默认路径", "支持扩展名"])
        
        # 设置列宽
        header = self.type_table.horizontalHeader()
        header.setStretchLastSection(False)
        self.type_table.setColumnWidth(0, 120)  # 类型名称列
        self.type_table.setColumnWidth(1, 200)  # 默认路径列
        self.type_table.setColumnWidth(2, 400)  # 支持扩展名列（增加宽度）
        
        # 设置表格样式
        self.type_table.setStyleSheet("""
            QTableWidget {
                border: 2px solid #e0e0e0;
                border-radius: 8px;
                background-color: white;
                gridline-color: #f0f0f0;
                selection-background-color: #e3f2fd;
            }
            QTableWidget::item {
                padding: 8px;
                border-bottom: 1px solid #f0f0f0;
                text-align: left;
            }
            QTableWidget::item:selected {
                background-color: #e3f2fd;
                color: #1976d2;
            }
            QHeaderView::section {
                background-color: #f5f5f5;
                padding: 10px;
                border: none;
                border-bottom: 2px solid #e0e0e0;
                font-weight: bold;
                text-align: left;
            }
        """)
        
        # 设置表格行高
        self.type_table.verticalHeader().setDefaultSectionSize(40)
        self.type_table.verticalHeader().setVisible(False)
        
        # 设置选择模式
        self.type_table.setSelectionBehavior(QTableWidget.SelectRows)
        self.type_table.setSelectionMode(QTableWidget.SingleSelection)
        
        # 允许编辑单元格
        self.type_table.setEditTriggers(QTableWidget.DoubleClicked | QTableWidget.EditKeyPressed)
        
        # 连接单元格编辑完成信号
        self.type_table.cellChanged.connect(self.on_cell_changed)
        
        self.load_type_table()
        content_layout.addWidget(self.type_table)
        
        # 操作按钮
        button_layout = QHBoxLayout()
        button_layout.setSpacing(12)
        
        add_btn = QPushButton("添加类型")
        add_btn.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 6px;
                padding: 8px 16px;
                font-size: 14px;
                font-weight: 500;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        add_btn.clicked.connect(self.add_type)
        
        edit_btn = QPushButton("编辑类型")
        edit_btn.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;
                color: white;
                border: none;
                border-radius: 6px;
                padding: 8px 16px;
                font-size: 14px;
                font-weight: 500;
            }
            QPushButton:hover {
                background-color: #1976D2;
            }
        """)
        edit_btn.clicked.connect(self.edit_type)
        
        delete_btn = QPushButton("删除类型")
        delete_btn.setStyleSheet("""
            QPushButton {
                background-color: #f44336;
                color: white;
                border: none;
                border-radius: 6px;
                padding: 8px 16px;
                font-size: 14px;
                font-weight: 500;
            }
            QPushButton:hover {
                background-color: #d32f2f;
            }
        """)
        delete_btn.clicked.connect(self.delete_type)
        
        button_layout.addWidget(add_btn)
        button_layout.addWidget(edit_btn)
        button_layout.addWidget(delete_btn)
        button_layout.addStretch()
        
        content_layout.addLayout(button_layout)
        
        # 底部按钮
        bottom_layout = QHBoxLayout()
        bottom_layout.setSpacing(12)
        
        cancel_btn = QPushButton("取消")
        cancel_btn.setStyleSheet("""
            QPushButton {
                background-color: #f5f5f5;
                color: #666;
                border: 1px solid #ddd;
                border-radius: 6px;
                padding: 10px 20px;
                font-size: 14px;
                font-weight: 500;
            }
            QPushButton:hover {
                background-color: #e9e9e9;
                border-color: #ccc;
            }
        """)
        cancel_btn.clicked.connect(self.reject)
        
        save_btn = QPushButton("保存")
        save_btn.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 6px;
                padding: 10px 20px;
                font-size: 14px;
                font-weight: 500;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        save_btn.clicked.connect(self.accept)
        
        bottom_layout.addStretch()
        bottom_layout.addWidget(cancel_btn)
        bottom_layout.addWidget(save_btn)
        
        content_layout.addLayout(bottom_layout)
        main_layout.addWidget(content_widget)
    
    def load_type_table(self):
        """加载类型表格"""
        self.type_table.setRowCount(len(self.resource_types))
        
        for row, (type_name, type_config) in enumerate(self.resource_types.items()):
            # 类型名称
            name_item = QTableWidgetItem(type_name)
            self.type_table.setItem(row, 0, name_item)
            
            # 默认路径
            path_item = QTableWidgetItem(type_config.get('path', ''))
            self.type_table.setItem(row, 1, path_item)
            
            # 支持扩展名
            extensions = ', '.join(type_config.get('extensions', []))
            ext_item = QTableWidgetItem(extensions)
            self.type_table.setItem(row, 2, ext_item)
    
    def add_type(self):
        """添加类型"""
        # 创建添加对话框
        add_dialog = QDialog(self)
        add_dialog.setWindowTitle("添加资源类型")
        width, height = get_optimal_dialog_size(500, 400)
        add_dialog.setFixedSize(width, height)
        center_window(add_dialog)
        add_dialog.setStyleSheet("""
            QDialog {
                background-color: #f8f9fa;
            }
        """)
        
        layout = QVBoxLayout(add_dialog)
        layout.setSpacing(15)
        layout.setContentsMargins(20, 20, 20, 20)
        
        # 类型名称
        name_label = QLabel("类型名称:")
        name_label.setStyleSheet("font-weight: bold; color: #333;")
        name_edit = QLineEdit()
        name_edit.setStyleSheet("""
            QLineEdit {
                padding: 8px;
                border: 2px solid #ddd;
                border-radius: 4px;
                font-size: 14px;
            }
            QLineEdit:focus {
                border-color: #4CAF50;
            }
        """)
        name_edit.setPlaceholderText("例如: 电子书、视频、文档等")
        
        # 默认路径
        path_label = QLabel("默认路径:")
        path_label.setStyleSheet("font-weight: bold; color: #333;")
        path_edit = QLineEdit()
        path_edit.setStyleSheet("""
            QLineEdit {
                padding: 8px;
                border: 2px solid #ddd;
                border-radius: 4px;
                font-size: 14px;
            }
            QLineEdit:focus {
                border-color: #4CAF50;
            }
        """)
        path_edit.setPlaceholderText("例如: D:/Documents/Books")
        
        # 支持扩展名
        ext_label = QLabel("支持的扩展名 (用逗号分隔):")
        ext_label.setStyleSheet("font-weight: bold; color: #333;")
        ext_edit = QLineEdit()
        ext_edit.setStyleSheet("""
            QLineEdit {
                padding: 8px;
                border: 2px solid #ddd;
                border-radius: 4px;
                font-size: 14px;
            }
            QLineEdit:focus {
                border-color: #4CAF50;
            }
        """)
        ext_edit.setPlaceholderText("例如: .pdf, .epub, .mobi, .azw")
        
        # 按钮
        button_layout = QHBoxLayout()
        cancel_btn = QPushButton("取消")
        cancel_btn.setStyleSheet("""
            QPushButton {
                background-color: #f5f5f5;
                color: #666;
                border: 1px solid #ddd;
                border-radius: 6px;
                padding: 8px 16px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #e9e9e9;
            }
        """)
        
        add_btn = QPushButton("添加")
        add_btn.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 6px;
                padding: 8px 16px;
                font-size: 14px;
                font-weight: 500;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        
        button_layout.addStretch()
        button_layout.addWidget(cancel_btn)
        button_layout.addWidget(add_btn)
        
        # 添加到布局
        layout.addWidget(name_label)
        layout.addWidget(name_edit)
        layout.addWidget(path_label)
        layout.addWidget(path_edit)
        layout.addWidget(ext_label)
        layout.addWidget(ext_edit)
        layout.addStretch()
        layout.addLayout(button_layout)
        
        # 连接信号
        cancel_btn.clicked.connect(add_dialog.reject)
        
        def add_new_type():
            type_name = name_edit.text().strip()
            if not type_name:
                QMessageBox.warning(add_dialog, "警告", "请输入类型名称！")
                return
            
            if type_name in self.resource_types:
                QMessageBox.warning(add_dialog, "警告", "该类型已存在！")
                return
            
            new_path = path_edit.text().strip()
            new_ext = ext_edit.text().strip()
            
            if new_ext:
                extensions = [ext.strip() for ext in new_ext.split(',') if ext.strip()]
            else:
                extensions = []
            
            self.resource_types[type_name] = {'path': new_path, 'extensions': extensions}
            self.load_type_table()
            add_dialog.accept()
        
        add_btn.clicked.connect(add_new_type)
        
        # 显示对话框
        add_dialog.exec_()
    
    def edit_type(self):
        """编辑类型"""
        current_row = self.type_table.currentRow()
        if current_row < 0:
            QMessageBox.warning(self, "警告", "请选择要编辑的类型！")
            return
        
        type_name = self.type_table.item(current_row, 0).text()
        path = self.type_table.item(current_row, 1).text()
        extensions_text = self.type_table.item(current_row, 2).text()
        
        # 创建编辑对话框
        edit_dialog = QDialog(self)
        edit_dialog.setWindowTitle(f"编辑资源类型 - {type_name}")
        width, height = get_optimal_dialog_size(500, 400)
        edit_dialog.setFixedSize(width, height)
        center_window(edit_dialog)
        edit_dialog.setStyleSheet("""
            QDialog {
                background-color: #f8f9fa;
            }
        """)
        
        layout = QVBoxLayout(edit_dialog)
        layout.setSpacing(15)
        layout.setContentsMargins(20, 20, 20, 20)
        
        # 类型名称（只读）
        name_label = QLabel("类型名称:")
        name_label.setStyleSheet("font-weight: bold; color: #333;")
        name_display = QLabel(type_name)
        name_display.setStyleSheet("""
            QLabel {
                background-color: #f0f0f0;
                padding: 8px;
                border-radius: 4px;
                color: #666;
            }
        """)
        
        # 默认路径
        path_label = QLabel("默认路径:")
        path_label.setStyleSheet("font-weight: bold; color: #333;")
        path_edit = QLineEdit(path)
        path_edit.setStyleSheet("""
            QLineEdit {
                padding: 8px;
                border: 2px solid #ddd;
                border-radius: 4px;
                font-size: 14px;
            }
            QLineEdit:focus {
                border-color: #2196F3;
            }
        """)
        
        # 支持扩展名
        ext_label = QLabel("支持的扩展名 (用逗号分隔):")
        ext_label.setStyleSheet("font-weight: bold; color: #333;")
        ext_edit = QLineEdit(extensions_text)
        ext_edit.setStyleSheet("""
            QLineEdit {
                padding: 8px;
                border: 2px solid #ddd;
                border-radius: 4px;
                font-size: 14px;
            }
            QLineEdit:focus {
                border-color: #2196F3;
            }
        """)
        ext_edit.setPlaceholderText("例如: .pdf, .doc, .docx, .txt")
        
        # 按钮
        button_layout = QHBoxLayout()
        cancel_btn = QPushButton("取消")
        cancel_btn.setStyleSheet("""
            QPushButton {
                background-color: #f5f5f5;
                color: #666;
                border: 1px solid #ddd;
                border-radius: 6px;
                padding: 8px 16px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #e9e9e9;
            }
        """)
        
        save_btn = QPushButton("保存")
        save_btn.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;
                color: white;
                border: none;
                border-radius: 6px;
                padding: 8px 16px;
                font-size: 14px;
                font-weight: 500;
            }
            QPushButton:hover {
                background-color: #1976D2;
            }
        """)
        
        button_layout.addStretch()
        button_layout.addWidget(cancel_btn)
        button_layout.addWidget(save_btn)
        
        # 添加到布局
        layout.addWidget(name_label)
        layout.addWidget(name_display)
        layout.addWidget(path_label)
        layout.addWidget(path_edit)
        layout.addWidget(ext_label)
        layout.addWidget(ext_edit)
        layout.addStretch()
        layout.addLayout(button_layout)
        
        # 连接信号
        cancel_btn.clicked.connect(edit_dialog.reject)
        
        def save_changes():
            new_path = path_edit.text().strip()
            new_ext = ext_edit.text().strip()
            
            if new_ext:
                extensions = [ext.strip() for ext in new_ext.split(',') if ext.strip()]
            else:
                extensions = []
            
            self.resource_types[type_name] = {'path': new_path, 'extensions': extensions}
            self.load_type_table()
            edit_dialog.accept()
        
        save_btn.clicked.connect(save_changes)
        
        # 显示对话框
        edit_dialog.exec_()
    
    def delete_type(self):
        """删除类型"""
        current_row = self.type_table.currentRow()
        if current_row < 0:
            QMessageBox.warning(self, "警告", "请选择要删除的类型！")
            return
        
        type_name = self.type_table.item(current_row, 0).text()
        reply = QMessageBox.question(self, "确认删除", f"确定要删除类型 '{type_name}' 吗？")
        if reply == QMessageBox.Yes:
            del self.resource_types[type_name]
            self.load_type_table()
    
    def on_cell_changed(self, row, column):
        """处理单元格内容变更"""
        # 获取当前行的类型名称
        type_name = self.type_table.item(row, 0).text()
        
        # 如果类型名称不在资源类型中，可能是加载表格时的操作，忽略
        if type_name not in self.resource_types:
            return
        
        # 根据列号更新相应的配置
        if column == 1:  # 默认路径
            path = self.type_table.item(row, column).text().strip()
            self.resource_types[type_name]['path'] = path
        elif column == 2:  # 支持扩展名
            extensions_text = self.type_table.item(row, column).text().strip()
            if extensions_text:
                extensions = [ext.strip() for ext in extensions_text.split(',') if ext.strip()]
            else:
                extensions = []
            self.resource_types[type_name]['extensions'] = extensions
    
    def get_resource_types(self):
        """获取资源类型配置"""
        return self.resource_types


class AddResourceDialog(QDialog):
    """添加资源对话框"""
    
    def __init__(self, parent=None, resource_categories=None, resource_types=None):
        super().__init__(parent)
        self.resource_categories = resource_categories or []
        self.resource_types = resource_types or {}
        self.file_info_label = None
        self.init_ui()
        self.setAcceptDrops(True)  # 启用拖拽功能
        
        # 用于窗口拖动的变量
        self.dragging = False
        self.drag_position = None
    
    def init_ui(self):
        """初始化UI"""
        self.setWindowTitle("添加资源")
        
        # 不使用固定大小，让布局系统自动计算
        width, height = get_optimal_dialog_size(750, 480)
        self.setMinimumSize(width, height)
        self.setMaximumSize(16777215, 16777215)  # 不限制最大大小
        center_window(self)
        
        # 设置对话框样式
        self.setStyleSheet("""
            QDialog {
                background-color: #f8f9fa;
            }
        """)
        
        main_layout = QVBoxLayout(self)
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(0, 0, 0, 0)
        
        # 创建内容区域，减少边距
        content_widget = QFrame()
        content_widget.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 8px;
                margin: 10px;
            }
        """)
        
        content_layout = QVBoxLayout(content_widget)
        content_layout.setSpacing(12)  # 减少组件间距
        content_layout.setContentsMargins(16, 16, 16, 16)  # 减少内边距
        
        # 标题，减少字体大小和边距
        title_label = QLabel("📁 添加资源")
        title_label.setStyleSheet("""
            QLabel {
                font-size: 16px;
                font-weight: bold;
                color: #1a1a1a;
                margin-bottom: 5px;
            }
        """)
        content_layout.addWidget(title_label)
        
        # 添加模式选择，减少间距
        mode_layout = QHBoxLayout()
        mode_layout.setSpacing(10)
        
        self.mode_independent = QCheckBox("独立选择文件")
        self.mode_type_based = QCheckBox("从资源类型选择")
        
        # 设置默认选中独立模式
        self.mode_independent.setChecked(True)
        
        # 设置样式，优化尺寸
        checkbox_style = """
            QCheckBox {
                font-size: 13px;
                font-weight: 500;
                color: #333;
                spacing: 6px;
            }
            QCheckBox::indicator {
                width: 16px;
                height: 16px;
                border-radius: 8px;
                border: 2px solid #ddd;
            }
            QCheckBox::indicator:checked {
                background-color: #007bff;
                border-color: #007bff;
            }
        """
        self.mode_independent.setStyleSheet(checkbox_style)
        self.mode_type_based.setStyleSheet(checkbox_style)
        
        # 连接信号，实现单选效果
        self.mode_independent.toggled.connect(self.on_mode_changed)
        self.mode_type_based.toggled.connect(self.on_mode_changed)
        
        mode_layout.addWidget(QLabel("选择模式："))
        mode_layout.addWidget(self.mode_independent)
        mode_layout.addWidget(self.mode_type_based)
        mode_layout.addStretch()
        
        content_layout.addLayout(mode_layout)
        
        # 创建主要内容区域（左右布局），减少间距
        main_content_layout = QHBoxLayout()
        main_content_layout.setSpacing(12)
        
        # 左侧面板（文件列表，仅在资源类型模式下显示），减少内边距
        self.left_panel = QFrame()
        self.left_panel.setStyleSheet("""
            QFrame {
                background-color: #f8f9fa;
                border: 1px solid #e9ecef;
                border-radius: 6px;
                padding: 10px;
            }
        """)
        self.left_panel.setVisible(False)  # 默认隐藏
        
        left_layout = QVBoxLayout(self.left_panel)
        left_layout.setSpacing(8)
        
        # 文件列表标题和搜索框
        title_search_layout = QVBoxLayout()
        
        self.file_list_title = QLabel("文件列表")
        self.file_list_title.setStyleSheet("""
            QLabel {
                font-size: 14px;
                font-weight: 600;
                color: #333;
                margin-bottom: 3px;
            }
        """)
        title_search_layout.addWidget(self.file_list_title)
        
        # 搜索框，优化尺寸
        self.file_search_box = QLineEdit()
        self.file_search_box.setPlaceholderText("🔍 搜索文件...")
        self.file_search_box.setStyleSheet("""
            QLineEdit {
                border: 1px solid #ddd;
                border-radius: 4px;
                padding: 5px 8px;
                font-size: 12px;
                background-color: white;
            }
            QLineEdit:focus {
                border-color: #2196F3;
                outline: none;
            }
        """)
        self.file_search_box.textChanged.connect(self.filter_file_list)
        title_search_layout.addWidget(self.file_search_box)
        
        left_layout.addLayout(title_search_layout)
        
        # 文件列表
        self.file_list = QListWidget()
        self.all_files = []  # 存储所有文件数据
        self.current_page = 0
        self.files_per_page = 50  # 每页显示50个文件
        self.file_list.setStyleSheet("""
            QListWidget {
                border: 1px solid #ddd;
                border-radius: 6px;
                background-color: white;
                selection-background-color: #e3f2fd;
                font-size: 12px;
                min-height: 240px;
            }
            QListWidget::item {
                padding: 4px 6px;
                border-bottom: 1px solid #f0f0f0;
                min-height: 20px;
            }
            QListWidget::item:hover {
                background-color: #f5f5f5;
            }
            QListWidget::item:selected {
                background-color: #e3f2fd;
                color: #1976d2;
            }
        """)
        self.file_list.itemClicked.connect(self.on_file_selected)
        left_layout.addWidget(self.file_list)
        
        # 分页控制
        pagination_layout = QHBoxLayout()
        
        self.prev_page_btn = QPushButton("◀ 上一页")
        self.prev_page_btn.setStyleSheet("""
            QPushButton {
                background-color: #f5f5f5;
                border: 1px solid #ddd;
                border-radius: 4px;
                padding: 4px 8px;
                font-size: 11px;
            }
            QPushButton:hover {
                background-color: #e0e0e0;
            }
            QPushButton:disabled {
                color: #999;
                background-color: #f9f9f9;
            }
        """)
        self.prev_page_btn.clicked.connect(self.prev_page)
        self.prev_page_btn.setEnabled(False)
        
        self.page_info_label = QLabel("第1页")
        self.page_info_label.setStyleSheet("""
            QLabel {
                font-size: 11px;
                color: #666;
                padding: 4px 8px;
            }
        """)
        self.page_info_label.setAlignment(Qt.AlignCenter)
        
        self.next_page_btn = QPushButton("下一页 ▶")
        self.next_page_btn.setStyleSheet("""
            QPushButton {
                background-color: #f5f5f5;
                border: 1px solid #ddd;
                border-radius: 4px;
                padding: 4px 8px;
                font-size: 11px;
            }
            QPushButton:hover {
                background-color: #e0e0e0;
            }
            QPushButton:disabled {
                color: #999;
                background-color: #f9f9f9;
            }
        """)
        self.next_page_btn.clicked.connect(self.next_page)
        self.next_page_btn.setEnabled(False)
        
        pagination_layout.addWidget(self.prev_page_btn)
        pagination_layout.addWidget(self.page_info_label)
        pagination_layout.addWidget(self.next_page_btn)
        
        left_layout.addLayout(pagination_layout)
        
        main_content_layout.addWidget(self.left_panel, 2)  # 增加左侧面板权重到2
        
        # 右侧面板（表单），减少间距
        right_panel = QFrame()
        right_layout = QVBoxLayout(right_panel)
        right_layout.setSpacing(10)
        
        # 资源名称（自动使用文件名，不允许用户输入）
        name_group = self.create_input_group("资源名称", "将自动使用文件名")
        self.name_edit = name_group['input']
        self.name_edit.setReadOnly(True)  # 设置为只读
        self.name_edit.setStyleSheet("""
            QLineEdit {
                border: 2px solid #e0e0e0;
                border-radius: 8px;
                padding: 12px 16px;
                font-size: 14px;
                background-color: #f0f0f0;
                color: #666666;
            }
        """)
        right_layout.addLayout(name_group['layout'])
        

        
        # 资源类型
        # 确保 resource_categories 是列表格式
        if isinstance(self.resource_categories, dict):
            categories_list = list(self.resource_categories.keys())
        elif isinstance(self.resource_categories, list):
            categories_list = self.resource_categories
        else:
            categories_list = []
        
        type_options = ["无类型"] + categories_list
        type_group = self.create_combo_group("资源类型", type_options)
        self.type_combo = type_group['combo']
        right_layout.addLayout(type_group['layout'])
        
        # 资源路径（仅在独立模式下显示）
        self.path_group_widget = QFrame()
        path_group_layout = QVBoxLayout(self.path_group_widget)
        path_group_layout.setContentsMargins(0, 0, 0, 0)
        
        path_group = self.create_path_group("资源路径")
        self.path_edit = path_group['input']
        self.browse_btn = path_group['button']
        path_group_layout.addLayout(path_group['layout'])
        
        # 文件信息预览
        self.file_info_label = QLabel("💡 提示：可以直接拖拽文件到此对话框，或点击浏览按钮选择文件")
        self.file_info_label.setStyleSheet("""
            QLabel {
                background-color: #f0f8ff;
                border: 1px solid #e1f5fe;
                border-radius: 6px;
                padding: 12px;
                font-size: 13px;
                color: #0277bd;
                margin: 5px 0;
            }
        """)
        self.file_info_label.setWordWrap(True)
        path_group_layout.addWidget(self.file_info_label)
        
        right_layout.addWidget(self.path_group_widget)
        
        # 资源标签
        tags_group = self.create_input_group("资源标签", "#标签1, #标签2（可选）")
        self.tags_edit = tags_group['input']
        right_layout.addLayout(tags_group['layout'])
        
        # 描述
        desc_group = self.create_textarea_group("描述", "请输入资源描述（可选）")
        self.desc_edit = desc_group['textarea']
        right_layout.addLayout(desc_group['layout'])
        
        # 添加右侧面板到主内容布局
        main_content_layout.addWidget(right_panel, 1)
        content_layout.addLayout(main_content_layout)
        
        # 按钮区域，优化样式
        button_layout = QHBoxLayout()
        button_layout.setSpacing(8)
        
        cancel_btn = QPushButton("取消")
        cancel_btn.setStyleSheet("""
            QPushButton {
                background-color: #f5f5f5;
                color: #666;
                border: 1px solid #ddd;
                border-radius: 5px;
                padding: 8px 16px;
                font-size: 13px;
                font-weight: 500;
                min-width: 60px;
            }
            QPushButton:hover {
                background-color: #e9e9e9;
                border-color: #ccc;
            }
        """)
        cancel_btn.clicked.connect(self.reject)
        
        add_btn = QPushButton("添加")
        add_btn.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 8px 16px;
                font-size: 13px;
                font-weight: 500;
                min-width: 60px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        add_btn.clicked.connect(self.accept_resource)
        
        button_layout.addStretch()
        button_layout.addWidget(cancel_btn)
        button_layout.addWidget(add_btn)
        
        content_layout.addLayout(button_layout)
        main_layout.addWidget(content_widget)
        
        # 连接信号
        self.browse_btn.clicked.connect(self.browse_file)
        self.path_edit.textChanged.connect(self.on_path_changed)
        self.type_combo.currentTextChanged.connect(self.on_type_changed)
        # 资源名称现在是只读的，不需要连接textChanged信号
        self.mode_independent.toggled.connect(self.on_mode_changed)
        self.mode_type_based.toggled.connect(self.on_mode_changed)
        self.file_list.itemClicked.connect(self.on_file_selected)
        
        # 初始化模式 - 延迟执行确保UI完全构建完成
        QTimer.singleShot(0, self._init_mode)
        
        # 确保窗口正确显示
        self.show()
        self.raise_()
        self.activateWindow()
    
    def _init_mode(self):
        """初始化模式状态"""
        self.mode_independent.setChecked(True)
        self.mode_type_based.setChecked(False)
        
        self.left_panel.hide()
        self.path_group_widget.show()
        self.file_info_label.setText("💡 提示：可以直接拖拽文件到此对话框，或点击浏览按钮选择文件")
        
        self.layout().update()
        for widget in self.findChildren(QWidget):
            if hasattr(widget, 'layout') and widget.layout():
                widget.layout().update()
        
        self.update()
    
    def create_input_group(self, label_text, placeholder):
        """创建输入框组"""
        layout = QVBoxLayout()
        layout.setSpacing(5)  # 减少间距
        
        label = QLabel(label_text)
        label.setStyleSheet("""
            QLabel {
                font-size: 13px;
                font-weight: 600;
                color: #333;
                margin: 0;
            }
        """)
        layout.addWidget(label)
        
        input_edit = QLineEdit()
        input_edit.setPlaceholderText(placeholder)
        input_edit.setStyleSheet("""
            QLineEdit {
                border: 2px solid #e0e0e0;
                border-radius: 6px;
                padding: 8px 12px;
                font-size: 13px;
                background-color: #fafafa;
            }
            QLineEdit:focus {
                border-color: #4CAF50;
                background-color: white;
            }
            QLineEdit:hover {
                border-color: #d0d0d0;
                background-color: white;
            }
        """)
        layout.addWidget(input_edit)
        
        return {'layout': layout, 'input': input_edit}
    
    def create_combo_group(self, label_text, items):
        """创建下拉框组"""
        layout = QVBoxLayout()
        layout.setSpacing(5)  # 减少间距
        
        label = QLabel(label_text)
        label.setStyleSheet("""
            QLabel {
                font-size: 13px;
                font-weight: 600;
                color: #333;
                margin: 0;
            }
        """)
        layout.addWidget(label)
        
        combo = QComboBox()
        combo.addItems(items)
        combo.setStyleSheet("""
            QComboBox {
                border: 2px solid #e0e0e0;
                border-radius: 6px;
                padding: 8px 12px;
                font-size: 13px;
                background-color: #fafafa;
            }
            QComboBox:focus {
                border-color: #4CAF50;
                background-color: white;
            }
            QComboBox:hover {
                border-color: #d0d0d0;
                background-color: white;
            }
            QComboBox::drop-down {
                border: none;
                width: 25px;
            }
            QComboBox::down-arrow {
                image: none;
                border-left: 4px solid transparent;
                border-right: 4px solid transparent;
                border-top: 4px solid #666;
                margin-right: 8px;
            }
        """)
        layout.addWidget(combo)
        
        return {'layout': layout, 'combo': combo}
    
    def create_path_group(self, label_text):
        """创建路径选择组"""
        layout = QVBoxLayout()
        layout.setSpacing(5)  # 减少间距
        
        label = QLabel(label_text)
        label.setStyleSheet("""
            QLabel {
                font-size: 13px;
                font-weight: 600;
                color: #333;
                margin: 0;
            }
        """)
        layout.addWidget(label)
        
        path_layout = QHBoxLayout()
        path_layout.setSpacing(6)  # 减少间距
        
        path_edit = QLineEdit()
        path_edit.setPlaceholderText("请选择文件路径")
        path_edit.setStyleSheet("""
            QLineEdit {
                border: 2px solid #e0e0e0;
                border-radius: 6px;
                padding: 8px 12px;
                font-size: 13px;
                background-color: #fafafa;
            }
            QLineEdit:focus {
                border-color: #4CAF50;
                background-color: white;
            }
            QLineEdit:hover {
                border-color: #d0d0d0;
                background-color: white;
            }
        """)
        
        browse_btn = QPushButton("浏览")
        browse_btn.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 8px 12px;
                font-size: 13px;
                font-weight: 500;
                min-width: 50px;
            }
            QPushButton:hover {
                background-color: #1976D2;
            }
        """)
        
        path_layout.addWidget(path_edit)
        path_layout.addWidget(browse_btn)
        layout.addLayout(path_layout)
        
        return {'layout': layout, 'input': path_edit, 'button': browse_btn}
    
    def create_textarea_group(self, label_text, placeholder):
        """创建文本域组"""
        layout = QVBoxLayout()
        layout.setSpacing(5)  # 减少间距
        
        label = QLabel(label_text)
        label.setStyleSheet("""
            QLabel {
                font-size: 13px;
                font-weight: 600;
                color: #333;
                margin: 0;
            }
        """)
        layout.addWidget(label)
        
        textarea = QTextEdit()
        textarea.setPlaceholderText(placeholder)
        textarea.setMaximumHeight(65)  # 减少高度
        textarea.setStyleSheet("""
            QTextEdit {
                border: 2px solid #e0e0e0;
                border-radius: 6px;
                padding: 8px 12px;
                font-size: 13px;
                background-color: #fafafa;
            }}
            QTextEdit:focus {{
                border-color: {c['success']};
                background-color: {c['surface']};
            }}
            QTextEdit:hover {{
                border-color: {c['border_hover']};
                background-color: {c['surface']};
            }}
        """)
        layout.addWidget(textarea)
        
        return {'layout': layout, 'textarea': textarea}
    

    
    def browse_file(self):
        """浏览文件"""
        # 根据当前选择的资源类型设置文件过滤器
        current_type = self.type_combo.currentText()
        file_filter = "所有文件 (*.*)"
        
        if current_type in self.resource_types:
            extensions = self.resource_types[current_type].get('extensions', [])
            if extensions:
                ext_filter = " ".join([f"*{ext}" for ext in extensions])
                file_filter = f"{current_type}文件 ({ext_filter});;所有文件 (*.*)"
        
        file_path, _ = QFileDialog.getOpenFileName(
            self, 
            "选择资源文件", 
            self.resource_types.get(current_type, {}).get('path', ''), 
            file_filter
        )
        if file_path:
            self.set_file_path(file_path)
    
    def set_file_path(self, file_path):
        """设置文件路径并更新相关信息"""
        self.path_edit.setText(file_path)
        
        # 自动设置资源名称为完整文件名（包含扩展名）
        file_name = os.path.basename(file_path)
        self.name_edit.setText(file_name)
        
        # 智能推荐资源类型
        self.suggest_resource_type(file_path)
        
        # 更新文件信息显示
        self.update_file_info(file_path)
        

    
    def suggest_resource_type(self, file_path):
        """根据文件扩展名智能推荐资源类型"""
        file_ext = os.path.splitext(file_path)[1].lower()
        
        for type_name, type_info in self.resource_types.items():
            extensions = type_info.get('extensions', [])
            if file_ext in extensions:
                # 找到匹配的类型，设置为当前选择
                index = self.type_combo.findText(type_name)
                if index >= 0:
                    self.type_combo.setCurrentIndex(index)
                break
    
    def update_file_info(self, file_path):
        """更新文件信息显示"""
        if os.path.exists(file_path):
            try:
                file_size = os.path.getsize(file_path)
                size_str = self.format_file_size(file_size)
                file_name = os.path.basename(file_path)
                
                info_text = f"📄 文件：{file_name}\n📏 大小：{size_str}\n📁 路径：{file_path}"
                self.file_info_label.setText(info_text)
                self.file_info_label.setStyleSheet("""
                    QLabel {
                        background-color: #f0fff0;
                        border: 1px solid #c8e6c9;
                        border-radius: 6px;
                        padding: 12px;
                        font-size: 13px;
                        color: #2e7d32;
                        margin: 5px 0;
                    }
                """)
            except Exception as e:
                self.file_info_label.setText(f"⚠️ 文件信息读取失败：{str(e)}")
                self.file_info_label.setStyleSheet("""
                    QLabel {
                        background-color: #fff3e0;
                        border: 1px solid #ffcc02;
                        border-radius: 6px;
                        padding: 12px;
                        font-size: 13px;
                        color: #f57c00;
                        margin: 5px 0;
                    }
                """)
        else:
            self.file_info_label.setText("❌ 文件不存在或路径无效")
            self.file_info_label.setStyleSheet("""
                QLabel {
                    background-color: #ffebee;
                    border: 1px solid #ef5350;
                    border-radius: 6px;
                    padding: 12px;
                    font-size: 13px;
                    color: #c62828;
                    margin: 5px 0;
                }
            """)
    
    def format_file_size(self, size_bytes):
        """格式化文件大小"""
        if size_bytes == 0:
            return "0 B"
        size_names = ["B", "KB", "MB", "GB", "TB"]
        import math
        i = int(math.floor(math.log(size_bytes, 1024)))
        p = math.pow(1024, i)
        s = round(size_bytes / p, 2)
        return f"{s} {size_names[i]}"
    
    def on_path_changed(self, text):
        """路径输入框内容变化时的处理"""
        path = text.strip()
        
        # 清除之前的错误状态
        self.clear_input_error(self.path_edit)
        
        if path:
            if os.path.exists(path):
                if os.path.isfile(path):
                    # 自动设置资源名称为完整文件名（包含扩展名）
                    name = os.path.basename(path)
                    self.name_edit.setText(name)
                    
                    # 智能推荐资源类型
                    suggested_type = self.suggest_resource_type(path)
                    if suggested_type:
                        index = self.type_combo.findText(suggested_type)
                        if index >= 0:
                            self.type_combo.setCurrentIndex(index)
                    
                    # 更新文件信息
                    self.update_file_info(path)
                    

                    
                    # 验证文件类型匹配
                    self.validate_file_type()
                else:
                    # 选择的是文件夹
                    self.show_input_error(self.path_edit, "请选择文件，不支持文件夹")
                    self.file_info_label.setText("❌ 不支持文件夹，请选择文件")
                    self.file_info_label.setStyleSheet("""
                        QLabel {
                            color: #dc3545;
                            background: #f8d7da;
                            border: 2px solid #f5c6cb;
                            border-radius: 8px;
                            padding: 15px;
                            text-align: center;
                        }
                    """)
            else:
                # 文件不存在
                self.show_input_error(self.path_edit, "文件不存在")
                self.file_info_label.setText("❌ 文件不存在，请重新选择")
                self.file_info_label.setStyleSheet("""
                    QLabel {
                        color: #dc3545;
                        background: #f8d7da;
                        border: 2px solid #f5c6cb;
                        border-radius: 8px;
                        padding: 15px;
                        text-align: center;
                    }
                """)
        else:
            # 路径为空
            self.file_info_label.setText("💡 提示：可以直接拖拽文件到此对话框，或点击浏览按钮选择文件")
            self.file_info_label.setStyleSheet("""
                QLabel {
                    background-color: #f0f8ff;
                    border: 1px solid #e1f5fe;
                    border-radius: 6px;
                    padding: 12px;
                    font-size: 13px;
                    color: #0277bd;
                    margin: 5px 0;
                }
            """)
    
    def on_type_changed(self, type_name):
        """资源类型变化时的处理"""
        if type_name in self.resource_types:
            type_info = self.resource_types[type_name]
            extensions = type_info.get('extensions', [])
            if extensions:
                ext_text = ", ".join(extensions)
                self.type_combo.setToolTip(f"支持的扩展名：{ext_text}")
            else:
                self.type_combo.setToolTip("")
            
            # 验证当前文件是否匹配新选择的类型
            self.validate_file_type()
            
            # 如果是类型选择模式，更新文件列表
            if hasattr(self, 'mode_type_based') and self.mode_type_based.isChecked():
                self.update_file_list()
        else:
            self.type_combo.setToolTip("")
    
    def mousePressEvent(self, event):
        """鼠标按下事件，用于实现窗口拖动"""
        if event.button() == Qt.LeftButton:
            # 记录拖动起始位置
            self.dragging = True
            self.drag_position = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()
    
    def mouseMoveEvent(self, event):
        """鼠标移动事件，用于实现窗口拖动"""
        if event.buttons() & Qt.LeftButton and self.dragging:
            # 移动窗口但不调整大小
            self.move(event.globalPos() - self.drag_position)
            event.accept()
    
    def mouseReleaseEvent(self, event):
        """鼠标释放事件，用于结束窗口拖动"""
        if event.button() == Qt.LeftButton:
            self.dragging = False
            event.accept()
    

    

    
    def dragEnterEvent(self, event):
        """拖拽进入事件"""
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()
    
    def dropEvent(self, event):
        """拖拽放下事件"""
        files = [u.toLocalFile() for u in event.mimeData().urls()]
        if files:
            # 收集所有有效文件
            valid_files = []
            
            for file_path in files:
                if os.path.isfile(file_path):
                    # 如果是文件，直接添加
                    valid_files.append(file_path)
                elif os.path.isdir(file_path):
                    # 如果是文件夹，遍历所有子文件夹中的文件
                    for root, dirs, folder_files in os.walk(file_path):
                        for file in folder_files:
                            full_path = os.path.join(root, file)
                            if os.path.isfile(full_path):
                                valid_files.append(full_path)
            
            if not valid_files:
                QMessageBox.warning(self, "警告", "未找到有效文件！")
                return
            
            if len(valid_files) == 1:
                # 单个文件，使用原有逻辑
                self.set_file_path(valid_files[0])
            else:
               
                
                # 打开批量添加对话框
                self.handle_batch_files(valid_files)
    
    def handle_batch_files(self, file_paths):
        """处理批量文件拖拽"""
        # 创建批量添加对话框
        batch_dialog = BatchAddResourceDialog(self, self.resource_categories, file_paths, None, self.resource_types)
        if batch_dialog.exec_() == QDialog.Accepted:
            # 获取批量添加的资源数据
            resources_data = batch_dialog.get_resources_data()
            if resources_data:
                # 关闭当前对话框并返回批量数据
                self.batch_resources_data = resources_data
                self.accept()
            else:
                QMessageBox.warning(self, "警告", "没有选择任何资源！")
                return
    
    def accept_resource(self):
        """验证并接受资源添加"""
        # 资源名称现在是自动设置的，不需要验证
        
        # 验证文件路径
        path = self.path_edit.text().strip()
        if not path:
            self.show_validation_error("请选择资源文件！", self.path_edit)
            return
        
        if not os.path.exists(path):
            self.show_validation_error("选择的文件不存在，请重新选择！", self.path_edit)
            return
        
        if not os.path.isfile(path):
            self.show_validation_error("请选择文件，不支持文件夹！", self.path_edit)
            return
        
        # 验证资源类型
        resource_type = self.type_combo.currentText()
        if resource_type in self.resource_types:
            extensions = self.resource_types[resource_type].get('extensions', [])
            if extensions:
                file_ext = os.path.splitext(path)[1].lower()
                if file_ext not in extensions:
                    ext_text = ", ".join(extensions)
                    reply = QMessageBox.question(
                        self, 
                        "类型不匹配", 
                        f"文件扩展名 '{file_ext}' 与所选类型 '{resource_type}' 不匹配。\n"
                        f"该类型支持的扩展名：{ext_text}\n\n"
                        f"是否仍要继续添加？",
                        QMessageBox.Yes | QMessageBox.No
                    )
                    if reply == QMessageBox.No:
                        return
        
        self.accept()
    
    def show_validation_error(self, message, focus_widget=None):
        """显示验证错误并聚焦到相关控件"""
        QMessageBox.warning(self, "输入验证", message)
        if focus_widget:
            focus_widget.setFocus()
            if hasattr(focus_widget, 'selectAll'):
                focus_widget.selectAll()
    
    def show_input_error(self, widget, tooltip_text):
        """显示输入错误状态"""
        widget.setStyleSheet("""
            QLineEdit {
                border: 2px solid #dc3545;
                background-color: #f8d7da;
                border-radius: 4px;
                padding: 8px;
            }
        """)
        widget.setToolTip(tooltip_text)
    
    def clear_input_error(self, widget):
        """清除输入错误状态"""
        widget.setStyleSheet("""
            QLineEdit {
                border: 1px solid #ddd;
                background-color: white;
                border-radius: 4px;
                padding: 8px;
            }
            QLineEdit:focus {
                border: 2px solid #007bff;
                outline: none;
            }
        """)
        widget.setToolTip("")
    
    def validate_file_type(self):
        """验证文件类型匹配"""
        path = self.path_edit.text().strip()
        resource_type = self.type_combo.currentText()
        
        if not path or not os.path.exists(path) or resource_type not in self.resource_types:
            return
        
        extensions = self.resource_types[resource_type].get('extensions', [])
        if extensions:
            file_ext = os.path.splitext(path)[1].lower()
            if file_ext not in extensions:
                # 显示类型不匹配警告
                ext_text = ", ".join(extensions)
                warning_text = f"⚠️ 文件类型可能不匹配\n当前：{file_ext or '无扩展名'}\n期望：{ext_text}"
                self.type_combo.setToolTip(warning_text)
                self.type_combo.setStyleSheet("""
                    QComboBox {
                        border: 2px solid #ffc107;
                        background-color: #fff3cd;
                        border-radius: 4px;
                        padding: 8px;
                    }
                """)
            else:
                # 类型匹配，清除警告
                self.type_combo.setToolTip(f"支持的扩展名：{', '.join(extensions)}")
                self.type_combo.setStyleSheet("""
                    QComboBox {
                        border: 1px solid #ddd;
                        background-color: white;
                        border-radius: 4px;
                        padding: 8px;
                    }
                    QComboBox:focus {
                        border: 2px solid #007bff;
                    }
                """)
    
    def on_name_changed(self, text):
        """资源名称变化时的处理"""
        name = text.strip()
        
        # 清除之前的错误状态
        self.clear_input_error(self.name_edit)
        
        if name:
            # 检查名称长度
            if len(name) > 100:
                self.show_input_error(self.name_edit, "资源名称不能超过100个字符")
            # 检查特殊字符
            elif any(char in name for char in ['/', '\\', ':', '*', '?', '"', '<', '>', '|']):
                self.show_input_error(self.name_edit, "资源名称不能包含特殊字符：/ \\ : * ? \" < > |")
            else:
                # 名称有效，应用正常样式
                self.name_edit.setStyleSheet("""
                    QLineEdit {
                        border: 2px solid #28a745;
                        background-color: #d4edda;
                        border-radius: 4px;
                        padding: 8px;
                    }
                """)
                self.name_edit.setToolTip("✓ 资源名称有效")
        else:
            # 名称为空，恢复默认样式
            self.name_edit.setStyleSheet("""
                QLineEdit {
                    border: 1px solid #ddd;
                    background-color: white;
                    border-radius: 4px;
                    padding: 8px;
                }
                QLineEdit:focus {
                    border: 2px solid #007bff;
                    outline: none;
                }
            """)
            self.name_edit.setToolTip("")
    
    def on_mode_changed(self):
        """处理模式切换"""
        sender = self.sender()
        
        # 实现单选效果
        if sender == self.mode_independent and self.mode_independent.isChecked():
            self.mode_type_based.setChecked(False)
        elif sender == self.mode_type_based and self.mode_type_based.isChecked():
            self.mode_independent.setChecked(False)
        
        # 确保至少有一个被选中
        if not self.mode_independent.isChecked() and not self.mode_type_based.isChecked():
            if sender == self.mode_independent:
                self.mode_type_based.setChecked(True)
            else:
                self.mode_independent.setChecked(True)
        
        if self.mode_independent.isChecked():
            # 独立选择文件模式
            self.left_panel.hide()
            self.path_group_widget.show()
            self.file_info_label.setText("💡 提示：可以直接拖拽文件到此对话框，或点击浏览按钮选择文件")
        else:
            # 从资源类型选择模式
            self.left_panel.show()
            self.path_group_widget.hide()
            # 使用QTimer延迟执行文件列表更新，避免阻塞UI
            QTimer.singleShot(50, self.update_file_list)
        
        # 仅更新内部布局，不调整窗口大小
        self.update()
    
    def update_file_list(self):
        """更新文件列表"""
        self.file_list.clear()
        
        current_type = self.type_combo.currentText()
        if not current_type or current_type not in self.resource_types:
            return
        
        # 显示加载提示
        loading_item = QListWidgetItem("🔄 正在搜索文件...")
        loading_item.setFlags(Qt.NoItemFlags)
        loading_item.setForeground(QColor('#666'))
        self.file_list.addItem(loading_item)
        
        # 获取当前资源类型的文件扩展名
        type_config = self.resource_types[current_type]
        extensions = type_config.get('extensions', [])
        
        # 使用QTimer分批处理文件搜索，避免阻塞UI
        QTimer.singleShot(10, lambda: self._search_files_async(extensions))
    
    def _search_files_async(self, extensions):
        """异步搜索文件"""
        try:
            # 获取当前资源类型的配置
            current_type = self.type_combo.currentText()
            type_config = self.resource_types.get(current_type, {})
            type_path = type_config.get('path', '')
            
            files_found = []
            file_count = 0
            max_files = 500  # 限制最大文件数量，避免性能问题
            
            # 如果资源类型有配置路径，则从该路径搜索
            if type_path and os.path.exists(type_path):
                search_dir = type_path
                # 忽略的目录列表
                ignore_dirs = {'.git', '__pycache__', 'node_modules', '.vscode', '.idea', 
                              'build', 'dist', '.pytest_cache', 'venv', 'env', '.env'}
                
                for root, dirs, files in os.walk(search_dir):
                    # 跳过隐藏目录和常见的忽略目录
                    dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ignore_dirs]
                    
                    for file in files:
                        if file_count >= max_files:
                            break
                            
                        if any(file.lower().endswith(ext.lower()) for ext in extensions):
                            file_path = os.path.join(root, file)
                            try:
                                # 获取文件大小
                                file_size = os.path.getsize(file_path)
                                file_size_str = self.format_file_size(file_size)
                                rel_path = os.path.relpath(file_path, search_dir)
                                files_found.append((file, rel_path, file_path, file_size_str))
                                file_count += 1
                            except OSError:
                                # 如果无法获取文件信息，跳过该文件
                                continue
                    
                    if file_count >= max_files:
                        break
            else:
                # 如果没有配置路径，则搜索项目目录
                project_dir = os.getcwd()
                ignore_dirs = {'.git', '__pycache__', 'node_modules', '.vscode', '.idea', 
                              'build', 'dist', '.pytest_cache', 'venv', 'env', '.env'}
                
                for root, dirs, files in os.walk(project_dir):
                    dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ignore_dirs]
                    
                    for file in files:
                        if file_count >= max_files:
                            break
                            
                        if any(file.lower().endswith(ext.lower()) for ext in extensions):
                            file_path = os.path.join(root, file)
                            try:
                                file_size = os.path.getsize(file_path)
                                file_size_str = self.format_file_size(file_size)
                                rel_path = os.path.relpath(file_path, project_dir)
                                files_found.append((file, rel_path, file_path, file_size_str))
                                file_count += 1
                            except OSError:
                                continue
                    
                    if file_count >= max_files:
                        break
            
            # 按文件名排序
            files_found.sort(key=lambda x: x[0].lower())
            
            # 存储所有文件数据
            self.all_files = files_found
            self.original_all_files = files_found.copy()  # 保存原始文件列表
            self.current_page = 0
            
            # 显示第一页
            self.display_current_page()
            
            if not files_found:
                self.file_list.clear()
                if type_path and not os.path.exists(type_path):
                    item = QListWidgetItem(f"❌ 资源类型路径不存在: {type_path}")
                    item.setFlags(Qt.NoItemFlags)
                    item.setForeground(QColor('#f44336'))
                else:
                    item = QListWidgetItem("未找到相关文件")
                    item.setFlags(Qt.NoItemFlags)
                    item.setForeground(QColor('#999'))
                self.file_list.addItem(item)
                self.update_pagination_buttons()
            elif file_count >= max_files:
                # 在文件列表底部添加提示
                self.file_list.addItem(QListWidgetItem(""))
                item = QListWidgetItem(f"⚠️ 找到{file_count}+个文件，使用搜索框过滤结果")
                item.setFlags(Qt.NoItemFlags)
                item.setForeground(QColor('#ff9800'))
                self.file_list.addItem(item)
                
        except Exception as e:
            # 错误处理
            self.file_list.clear()
            error_item = QListWidgetItem(f"❌ 搜索文件时出错: {str(e)}")
            error_item.setFlags(Qt.NoItemFlags)
            error_item.setForeground(QColor('#f44336'))
            self.file_list.addItem(error_item)
    
    def display_current_page(self):
        """显示当前页的文件"""
        self.file_list.clear()
        
        # 获取当前页的文件
        start_idx = self.current_page * self.files_per_page
        end_idx = start_idx + self.files_per_page
        current_files = self.all_files[start_idx:end_idx]
        
        # 添加到列表
        for file_name, rel_path, full_path, file_size_str in current_files:
            item = QListWidgetItem()
            # 紧凑显示：文件名 | 大小 | 路径
            display_path = rel_path if len(rel_path) <= 40 else "..." + rel_path[-37:]
            item.setText(f"📄 {file_name} | 📊 {file_size_str} | 📁 {display_path}")
            item.setData(Qt.UserRole, full_path)
            item.setToolTip(f"文件名: {file_name}\n文件大小: {file_size_str}\n完整路径: {full_path}")
            self.file_list.addItem(item)
        
        self.update_pagination_buttons()
    
    def update_pagination_buttons(self):
        """更新分页按钮状态"""
        total_pages = (len(self.all_files) + self.files_per_page - 1) // self.files_per_page
        
        self.prev_page_btn.setEnabled(self.current_page > 0)
        self.next_page_btn.setEnabled(self.current_page < total_pages - 1)
        
        if total_pages > 0:
            self.page_info_label.setText(f"第{self.current_page + 1}页 / 共{total_pages}页 ({len(self.all_files)}个文件)")
        else:
            self.page_info_label.setText("无文件")
    
    def prev_page(self):
        """上一页"""
        if self.current_page > 0:
            self.current_page -= 1
            self.display_current_page()
    
    def next_page(self):
        """下一页"""
        total_pages = (len(self.all_files) + self.files_per_page - 1) // self.files_per_page
        if self.current_page < total_pages - 1:
            self.current_page += 1
            self.display_current_page()
    
    def filter_file_list(self):
        """根据搜索框内容过滤文件列表"""
        search_text = self.file_search_box.text().lower().strip()
        
        # 如果还没有原始文件列表，先保存
        if not hasattr(self, 'original_all_files'):
            self.original_all_files = self.all_files.copy()
        
        if not search_text:
            # 如果搜索框为空，恢复显示所有文件
            self.all_files = self.original_all_files.copy()
            self.current_page = 0
            self.display_current_page()
            return
        
        # 过滤文件
        filtered_files = []
        for file_name, rel_path, full_path, file_size_str in self.original_all_files:
            if (search_text in file_name.lower() or 
                search_text in rel_path.lower() or
                search_text in file_size_str.lower()):
                filtered_files.append((file_name, rel_path, full_path, file_size_str))
        
        # 更新当前显示的文件列表
        self.all_files = filtered_files
        self.current_page = 0
        self.display_current_page()
    
    def on_file_selected(self):
        """处理文件选择"""
        current_item = self.file_list.currentItem()
        if current_item and current_item.data(Qt.UserRole):
            file_path = current_item.data(Qt.UserRole)
            self.set_file_path(file_path)
    
    def get_resource_data(self):
        """获取资源数据（包含ID）"""
        selected_type = self.type_combo.currentText()
        resource_type = "" if selected_type == "无类型" else selected_type
        
        return {
            'name': self.name_edit.text().strip(),
            'type': resource_type,
            'path': self.path_edit.text().strip(),
            'description': self.desc_edit.toPlainText().strip(),
            'tags': self.tags_edit.text().strip(),
            'added_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }


class BatchAddResourceDialog(QDialog):
    """批量添加资源对话框"""
    
    def __init__(self, parent=None, resource_categories=None, file_paths=None, project_id=None, resource_types=None):
        super().__init__(parent)
        self.file_paths = file_paths or []
        self.resource_categories = resource_categories or []
        self.resource_types = resource_types or {}
        self.project_id = project_id
        self.batch_resources_data = []  # 用于存储批量添加的资源数据
        
        # 统计文件夹信息
        self.folder_stats = {}
        for file_path in self.file_paths:
            folder = os.path.dirname(file_path)
            if folder in self.folder_stats:
                self.folder_stats[folder] += 1
            else:
                self.folder_stats[folder] = 1
        
        # 用于窗口拖动的变量
        self.dragging = False
        self.drag_position = None
        
        self.init_ui()
    
    def mousePressEvent(self, event):
        """鼠标按下事件，用于实现窗口拖动"""
        if event.button() == Qt.LeftButton:
            # 记录拖动起始位置
            self.dragging = True
            self.drag_position = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()
    
    def mouseMoveEvent(self, event):
        """鼠标移动事件，用于实现窗口拖动"""
        if event.buttons() & Qt.LeftButton and self.dragging:
            # 移动窗口但不调整大小
            self.move(event.globalPos() - self.drag_position)
            event.accept()
    
    def mouseReleaseEvent(self, event):
        """鼠标释放事件，用于结束窗口拖动"""
        if event.button() == Qt.LeftButton:
            self.dragging = False
            event.accept()
    

    
    def init_ui(self):
        """初始化UI"""
        self.setWindowTitle(f"批量添加资源 ({len(self.file_paths)}个文件)")
        width, height = get_optimal_dialog_size(1000, 750)
        self.setFixedSize(width, height)
        center_window(self)
        self.setWindowFlags(self.windowFlags() | Qt.MSWindowsFixedSizeDialogHint)
        
        # 设置对话框样式
        self.setStyleSheet("""
            QDialog {
                background-color: #f8f9fa;
            }
        """)
        
        main_layout = QVBoxLayout(self)
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(0, 0, 0, 0)
        
        # 创建内容区域
        content_widget = QFrame()
        content_widget.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 12px;
                margin: 15px;
            }
        """)
        
        content_layout = QVBoxLayout(content_widget)
        content_layout.setSpacing(10)
        content_layout.setContentsMargins(20, 15, 20, 20)
        
        # 创建顶部信息区域（标题和文件夹信息的水平布局）
        top_info_layout = QHBoxLayout()
        top_info_layout.setSpacing(15)
        
        # 标题和资源数量显示在左侧
        title_info_layout = QVBoxLayout()
        title_info_layout.setSpacing(5)
        
        # 标题
        title_label = QLabel(f"📁 批量添加资源 ({len(self.file_paths)}个文件)")
        title_label.setStyleSheet("""
            QLabel {
                font-size: 18px;
                font-weight: bold;
                color: #1a1a1a;
            }
        """)
        title_info_layout.addWidget(title_label)
        
        # 添加资源数量显示
        self.resource_count_label = QLabel(f"将添加 {len(self.file_paths)} 个资源（已自动匹配资源类型）")
        self.resource_count_label.setStyleSheet("""
            QLabel {
                font-size: 13px;
                font-weight: bold;
                color: #007bff;
            }
        """)
        title_info_layout.addWidget(self.resource_count_label)
        
        top_info_layout.addLayout(title_info_layout, 1)  # 左侧标题区域占比更大
        
        # 文件夹信息区域在右侧（如果有）
        if len(self.folder_stats) > 0:
            folder_info_frame = QFrame()
            folder_info_frame.setStyleSheet("""
                QFrame {
                    background-color: #e8f5e9;
                    border: 1px solid #c8e6c9;
                    border-radius: 8px;
                    padding: 8px;
                    max-height: 80px;
                }
            """)
            folder_info_layout = QVBoxLayout(folder_info_frame)
            folder_info_layout.setSpacing(2)
            folder_info_layout.setContentsMargins(8, 8, 8, 8)
            
            folder_info_title = QLabel(f"📂 文件来源 ({len(self.folder_stats)}个文件夹)")
            folder_info_title.setStyleSheet("""
                QLabel {
                    font-size: 13px;
                    font-weight: bold;
                    color: #2e7d32;
                }
            """)
            folder_info_layout.addWidget(folder_info_title)
            
            # 只显示前2个文件夹，如果超过2个则显示省略信息
            sorted_folders = sorted(self.folder_stats.items(), key=lambda x: x[1], reverse=True)
            for i, (folder, count) in enumerate(sorted_folders):
                if i < 2:
                    folder_text = QLabel(f"• {folder} ({count}个文件)")
                    folder_text.setStyleSheet("font-size: 11px; color: #333;")
                    folder_text.setWordWrap(True)
                    folder_info_layout.addWidget(folder_text)
            
            if len(sorted_folders) > 2:
                more_text = QLabel(f"...等{len(sorted_folders)-2}个文件夹")
                more_text.setStyleSheet("font-size: 11px; color: #666; font-style: italic;")
                folder_info_layout.addWidget(more_text)
            
            top_info_layout.addWidget(folder_info_frame)
        
        content_layout.addLayout(top_info_layout)
        
        # 文件表格
        self.file_table = QTableWidget()
        self.file_table.setColumnCount(5)
        self.file_table.setHorizontalHeaderLabels(["文件名", "资源名称", "资源类型", "描述", "选择"])
        content_layout.addWidget(self.file_table)
        
        # 确保表头可见
        self.file_table.horizontalHeader().setVisible(True)
        
        # 设置表格样式 - 与主页项目列表样式保持一致
        self.file_table.setStyleSheet("""
            QTableWidget {
                background-color: white;
                border: 1px solid #e0e0e0;
                border-radius: 4px;
                gridline-color: #f0f0f0;
                selection-background-color: #e3f2fd;
            }
            QTableWidget::item {
                padding: 12px 8px;
                border-bottom: 1px solid #f0f0f0;
                min-height: 40px;
            }
            QTableWidget::item:selected {
                background-color: #e3f2fd;
                color: #1976d2;
            }
        """)
        
        # 设置表头样式 - 与主页项目列表样式保持一致
        self.file_table.horizontalHeader().setStyleSheet("""
            QHeaderView::section {
                background-color: #f5f5f5;
                padding: 12px 8px;
                border: none;
                border-bottom: 2px solid #e0e0e0;
                font-weight: bold;
                min-height: 35px;
            }
            QHeaderView {
                font-size: 13px;
                font-weight: bold;
                color: #333;
            }
        """)
        
        # 设置表格属性 - 与主页项目列表一致
        self.file_table.setSelectionBehavior(QTableWidget.SelectRows)
        self.file_table.setAlternatingRowColors(True)
        self.file_table.verticalHeader().setVisible(False)
        
        # 设置列宽
        header = self.file_table.horizontalHeader()
        header.setStretchLastSection(False)
        header.setSectionResizeMode(0, QHeaderView.Fixed)  # 文件名
        header.setSectionResizeMode(1, QHeaderView.Stretch)  # 资源名称
        header.setSectionResizeMode(2, QHeaderView.Fixed)  # 资源类型
        header.setSectionResizeMode(3, QHeaderView.Stretch)  # 描述
        header.setSectionResizeMode(4, QHeaderView.Fixed)  # 操作
        
        self.file_table.setColumnWidth(0, 200)
        self.file_table.setColumnWidth(2, 120)
        self.file_table.setColumnWidth(4, 60)  # 减小选择列宽度
        
        # 设置默认行高
        self.file_table.verticalHeader().setDefaultSectionSize(60)
        
        # 设置表格占据更多垂直空间
        self.file_table.setMinimumHeight(500)
        
        # 填充文件列表
        self.populate_file_list()
        
        # 按钮区域 - 更紧凑的布局
        button_layout = QHBoxLayout()
        button_layout.setSpacing(8)
        button_layout.setContentsMargins(0, 5, 0, 0)
        
        # 全选/取消全选按钮组
        selection_buttons = QHBoxLayout()
        selection_buttons.setSpacing(5)
        
        select_all_btn = QPushButton("全选")
        select_all_btn.setStyleSheet("""
            QPushButton {
                background-color: #28a745;
                color: white;
                border: none;
                border-radius: 4px;
                padding: 6px 12px;
                font-size: 12px;
                font-weight: 500;
            }
            QPushButton:hover {
                background-color: #1e7e34;
            }
        """)
        select_all_btn.clicked.connect(self.select_all_files)
        selection_buttons.addWidget(select_all_btn)
        
        deselect_all_btn = QPushButton("取消全选")
        deselect_all_btn.setStyleSheet("""
            QPushButton {
                background-color: #ffc107;
                color: #212529;
                border: none;
                border-radius: 4px;
                padding: 6px 12px;
                font-size: 12px;
                font-weight: 500;
            }
            QPushButton:hover {
                background-color: #e0a800;
            }
        """)
        deselect_all_btn.clicked.connect(self.deselect_all_files)
        selection_buttons.addWidget(deselect_all_btn)
        
        button_layout.addLayout(selection_buttons)
        button_layout.addStretch()
        
        # 确定和取消按钮
        action_buttons = QHBoxLayout()
        action_buttons.setSpacing(8)
        
        ok_btn = QPushButton("添加选中的资源")
        ok_btn.setStyleSheet("""
            QPushButton {
                background-color: #007bff;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 8px 16px;
                font-size: 13px;
                font-weight: 600;
                min-width: 120px;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
        """)
        ok_btn.clicked.connect(self.accept_resources)
        action_buttons.addWidget(ok_btn)
        
        cancel_btn = QPushButton("取消")
        cancel_btn.setStyleSheet("""
            QPushButton {
                background-color: #6c757d;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 8px 16px;
                font-size: 13px;
                font-weight: 600;
                min-width: 80px;
            }
            QPushButton:hover {
                background-color: #545b62;
            }
        """)
        cancel_btn.clicked.connect(self.reject)
        action_buttons.addWidget(cancel_btn)
        
        button_layout.addLayout(action_buttons)
        content_layout.addLayout(button_layout)
        main_layout.addWidget(content_widget)
    
    def populate_file_list(self):
        """填充文件列表"""
        self.file_table.setRowCount(len(self.file_paths))
        
        for row, file_path in enumerate(self.file_paths):
            file_name = os.path.basename(file_path)
            folder_path = os.path.dirname(file_path)
            
            # 文件名（只读）
            file_name_item = QTableWidgetItem(file_name)
            file_name_item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
            file_name_item.setToolTip(f"完整路径: {file_path}\n文件夹: {folder_path}")
            self.file_table.setItem(row, 0, file_name_item)
            
            # 资源名称（可编辑，默认为完整文件名包含扩展名）
            resource_name = file_name  # 保留完整文件名包括扩展名
            name_item = QTableWidgetItem(resource_name)
            self.file_table.setItem(row, 1, name_item)
            
            # 资源类型下拉框
            type_combo = QComboBox()
            # 确保 resource_categories 是列表格式
            if isinstance(self.resource_categories, dict):
                categories_list = list(self.resource_categories.keys())
            elif isinstance(self.resource_categories, list):
                categories_list = self.resource_categories
            else:
                categories_list = []
            
            type_options = ["无类型"] + categories_list
            type_combo.addItems(type_options)
            
            # 根据文件扩展名自动匹配资源类型
            file_ext = os.path.splitext(file_path)[1].lower()
            matched = False
            for type_name, type_info in self.resource_types.items():
                extensions = type_info.get('extensions', [])
                if file_ext in extensions:
                    # 找到匹配的类型，设置为当前选择
                    index = type_combo.findText(type_name)
                    if index >= 0:
                        type_combo.setCurrentIndex(index)
                        matched = True
                        break
            type_combo.setStyleSheet("""
                QComboBox {
                    border: 1px solid #ddd;
                    border-radius: 4px;
                    padding: 2px 6px;
                    font-size: 10px;
                    background-color: white;
                    min-height: 16px;
                }
                QComboBox::drop-down {
                    border: none;
                    width: 18px;
                }
                QComboBox::down-arrow {
                    image: none;
                    border-left: 2px solid transparent;
                    border-right: 2px solid transparent;
                    border-top: 2px solid #666;
                    margin-right: 2px;
                }
                QComboBox QAbstractItemView {
                    border: 1px solid #ddd;
                    background-color: white;
                    selection-background-color: #e3f2fd;
                    font-size: 10px;
                }
            """)
            
            # 创建一个容器来放置类型下拉框
            type_widget = QWidget()
            type_widget.setStyleSheet("background-color: white;")
            type_layout = QHBoxLayout(type_widget)
            type_layout.addWidget(type_combo)
            type_layout.setAlignment(Qt.AlignCenter)
            type_layout.setContentsMargins(2, 2, 2, 2)
            
            self.file_table.setCellWidget(row, 2, type_widget)
            
            # 描述（可编辑）
            desc_item = QTableWidgetItem("")
            self.file_table.setItem(row, 3, desc_item)
            
            # 选择复选框
            checkbox = QCheckBox()
            checkbox.setChecked(True)  # 默认选中
            checkbox.setStyleSheet("""
                QCheckBox {
                    margin: 0px;
                }
                QCheckBox::indicator {
                    width: 16px;
                    height: 16px;
                }
            """)
            
            # 创建一个容器来居中复选框
            checkbox_widget = QWidget()
            checkbox_widget.setStyleSheet("background-color: white;")
            checkbox_layout = QHBoxLayout(checkbox_widget)
            checkbox_layout.addWidget(checkbox)
            checkbox_layout.setAlignment(Qt.AlignCenter)
            checkbox_layout.setContentsMargins(0, 0, 0, 0)
            checkbox_layout.setSpacing(0)
            
            self.file_table.setCellWidget(row, 4, checkbox_widget)
            
            # 设置行高与主页项目列表一致
            self.file_table.setRowHeight(row, 60)
    
    # 已移除 apply_type_to_all 方法，因为现在使用自动匹配资源类型
    
    def select_all_files(self):
        """全选所有文件"""
        for row in range(self.file_table.rowCount()):
            checkbox_widget = self.file_table.cellWidget(row, 4)
            if checkbox_widget:
                checkbox = checkbox_widget.findChild(QCheckBox)
                if checkbox:
                    checkbox.setChecked(True)
    
    def deselect_all_files(self):
        """取消全选所有文件"""
        for row in range(self.file_table.rowCount()):
            checkbox_widget = self.file_table.cellWidget(row, 4)
            if checkbox_widget:
                checkbox = checkbox_widget.findChild(QCheckBox)
                if checkbox:
                    checkbox.setChecked(False)
    
    def accept_resources(self):
        """接受选中的资源"""
        self.batch_resources_data = []
        
        for row in range(self.file_table.rowCount()):
            # 检查是否选中
            checkbox_widget = self.file_table.cellWidget(row, 4)
            checkbox = checkbox_widget.findChild(QCheckBox) if checkbox_widget else None
            
            if checkbox and checkbox.isChecked():
                # 获取资源数据
                file_path = self.file_paths[row]
                name_item = self.file_table.item(row, 1)
                type_combo = self.file_table.cellWidget(row, 2)
                desc_item = self.file_table.item(row, 3)
                
                resource_name = name_item.text().strip() if name_item else os.path.basename(file_path)  # 保留完整文件名包括扩展名
                # 修复：type_combo 是一个 QWidget 容器，需要先找到其中的 QComboBox
                combo_box = type_combo.findChild(QComboBox) if type_combo else None
                selected_type = combo_box.currentText() if combo_box else list(self.resource_types.keys())[0] if self.resource_types else "无类型"
                resource_type = "" if selected_type == "无类型" else selected_type
                description = desc_item.text().strip() if desc_item else ""
                
                # 验证资源名称
                if not resource_name:
                    QMessageBox.warning(self, "警告", f"第{row+1}行的资源名称不能为空！")
                    return
                
                # 不在这里生成ID，让统一的重复检查机制来处理ID生成
                resource_data = {
                    'name': resource_name,
                    'type': resource_type,
                    'path': file_path,
                    'description': description,
                    'added_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                }
                
                self.batch_resources_data.append(resource_data)
        
        if not self.batch_resources_data:
            QMessageBox.warning(self, "警告", "请至少选择一个文件！")
            return
        else:
            # 更新资源数量标签
            self.resource_count_label.setText(f"已选择 {len(self.batch_resources_data)} 个资源（已自动匹配资源类型）")
            self.resource_count_label.setStyleSheet("""
                QLabel {
                    font-size: 14px;
                    font-weight: bold;
                    color: #28a745;
                    padding: 5px 0;
                }
            """)
            
            # 只有在有选择资源的情况下才接受对话框
            self.accept()
    
    def get_resources_data(self):
        """获取批量资源数据"""
        return self.batch_resources_data

    def create_notes_card(self):
        """创建项目笔记卡片"""
        card = QVBoxLayout()
        
        # 顶部工具栏
        toolbar_layout = QHBoxLayout()
        
        notes_label = QLabel("📝 项目笔记")
        notes_label.setStyleSheet("""
            QLabel {
                font-size: 16px;
                font-weight: bold;
                color: #333;
            }
        """)
        
        # 视图切换按钮
        self.view_mode_btn = QPushButton("📅 时间轴视图")
        self.view_mode_btn.setStyleSheet("""
            QPushButton {
                background-color: #673AB7;
                color: white;
                border: none;
                border-radius: 6px;
                padding: 6px 12px;
                font-size: 12px;
                font-weight: 500;
            }
            QPushButton:hover {
                background-color: #5E35B1;
            }
        """)
        self.view_mode_btn.clicked.connect(self.toggle_view_mode)
        self.is_timeline_view = False
        
        # 待办事项开关
        self.todo_switch = QCheckBox("显示待办事项")
        self.todo_switch.setStyleSheet("""
            QCheckBox {
                font-size: 13px;
                color: #333;
            }
            QCheckBox::indicator {
                width: 18px;
                height: 18px;
            }
            QCheckBox::indicator:unchecked {
                border: 2px solid #ddd;
                background-color: white;
                border-radius: 3px;
            }
            QCheckBox::indicator:checked {
                border: 2px solid #4CAF50;
                background-color: #4CAF50;
                border-radius: 3px;
            }
        """)
        self.todo_switch.setChecked(False)  # 默认不显示待办事项
        self.todo_switch.stateChanged.connect(self.toggle_todo_visibility)
        
        toolbar_layout.addWidget(notes_label)
        toolbar_layout.addStretch()
        toolbar_layout.addWidget(self.todo_switch)
        toolbar_layout.addWidget(self.view_mode_btn)
        card.addLayout(toolbar_layout)
        
        # 创建堆叠布局来切换视图
        self.notes_stack = QTabWidget()
        self.notes_stack.setTabPosition(QTabWidget.North)
        self.notes_stack.setStyleSheet("""
            QTabWidget::pane {
                border: 1px solid #ddd;
                border-radius: 6px;
                background-color: white;
            }
            QTabWidget::tab-bar {
                alignment: center;
            }
            QTabBar::tab {
                background-color: #f5f5f5;
                color: #666;
                border: 1px solid #ddd;
                border-bottom: none;
                border-radius: 6px 6px 0 0;
                padding: 8px 16px;
                margin-right: 2px;
                font-size: 13px;
            }
            QTabBar::tab:selected {
                background-color: white;
                color: #333;
                border-bottom: 1px solid white;
            }
            QTabBar::tab:hover {
                background-color: #e8e8e8;
            }
        """)
        
        # 编辑视图
        edit_widget = QWidget()
        edit_layout = QVBoxLayout(edit_widget)
        
        # 笔记文本编辑器
        self.notes_text = QTextEdit()
        self.notes_text.setPlaceholderText("在这里记录项目笔记...")
        self.notes_text.setStyleSheet("""
            QTextEdit {
                border: 1px solid #ddd;
                border-radius: 6px;
                padding: 10px;
                font-size: 14px;
                background-color: white;
                min-height: 200px;
            }
            QTextEdit:focus {
                border-color: #2196F3;
            }
        """)
        edit_layout.addWidget(self.notes_text)
        
        # 时间轴视图
        timeline_widget = QWidget()
        timeline_layout = QVBoxLayout(timeline_widget)
        
        # 时间轴滚动区域
        self.timeline_scroll = QScrollArea()
        self.timeline_scroll.setWidgetResizable(True)
        self.timeline_scroll.setStyleSheet("""
            QScrollArea {
                border: none;
                background-color: #f8f9fa;
            }
        """)
        
        self.timeline_content = QWidget()
        self.timeline_layout = QVBoxLayout(self.timeline_content)
        self.timeline_layout.setSpacing(20)
        self.timeline_layout.setContentsMargins(20, 20, 20, 20)
        
        self.timeline_scroll.setWidget(self.timeline_content)
        timeline_layout.addWidget(self.timeline_scroll)
        
        # 添加选项卡
        self.notes_stack.addTab(edit_widget, "✏️ 编辑模式")
        self.notes_stack.addTab(timeline_widget, "📅 时间轴")
        
        card.addWidget(self.notes_stack)
        
        # 创建待办事项容器（可隐藏/显示）
        self.todo_widget = QWidget()
        todo_widget_layout = QVBoxLayout(self.todo_widget)
        todo_widget_layout.setContentsMargins(0, 0, 0, 0)
        todo_widget_layout.setSpacing(15)
        
        # 待办事项区域
        todo_label = QLabel("✅ 待办事项")
        todo_label.setStyleSheet("""
            QLabel {
                font-size: 16px;
                font-weight: bold;
                color: #333;
                margin-top: 20px;
                margin-bottom: 10px;
            }
        """)
        todo_widget_layout.addWidget(todo_label)
        
        # 添加待办事项输入框
        todo_input_layout = QHBoxLayout()
        self.todo_input = QLineEdit()
        self.todo_input.setPlaceholderText("输入新的待办事项...")
        self.todo_input.setStyleSheet("""
            QLineEdit {
                border: 1px solid #ddd;
                border-radius: 6px;
                padding: 8px 12px;
                font-size: 14px;
                background-color: white;
            }
            QLineEdit:focus {
                border-color: #2196F3;
            }
        """)
        self.todo_input.returnPressed.connect(self.add_todo_item)
        
        add_todo_btn = QPushButton("添加")
        add_todo_btn.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 6px;
                padding: 8px 16px;
                font-size: 14px;
                font-weight: 500;
                min-width: 60px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        add_todo_btn.clicked.connect(self.add_todo_item)
        
        todo_input_layout.addWidget(self.todo_input)
        todo_input_layout.addWidget(add_todo_btn)
        todo_widget_layout.addLayout(todo_input_layout)
        
        # 待办事项列表
        self.todo_list = QListWidget()
        self.todo_list.setStyleSheet("""
            QListWidget {
                border: 1px solid #ddd;
                border-radius: 6px;
                background-color: white;
                min-height: 150px;
            }
            QListWidget::item {
                padding: 8px;
                border-bottom: 1px solid #f0f0f0;
            }
            QListWidget::item:hover {
                background-color: #f5f5f5;
            }
            QListWidget::item:selected {
                background-color: #e3f2fd;
                color: #1976d2;
            }
        """)
        self.todo_list.itemDoubleClicked.connect(self.toggle_todo_item)
        todo_widget_layout.addWidget(self.todo_list)
        
        # 默认隐藏待办事项区域
        self.todo_widget.setVisible(False)
        edit_layout.addWidget(self.todo_widget)
        
        # 操作按钮
        button_layout = QHBoxLayout()
        
        save_btn = QPushButton("💾 保存笔记")
        save_btn.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;
                color: white;
                border: none;
                border-radius: 6px;
                padding: 10px 16px;
                font-size: 14px;
                font-weight: 500;
            }
            QPushButton:hover {
                background-color: #1976D2;
            }
        """)
        save_btn.clicked.connect(self.save_notes)
        
        open_file_btn = QPushButton("📂 打开笔记文件")
        open_file_btn.setStyleSheet("""
            QPushButton {
                background-color: #FF9800;
                color: white;
                border: none;
                border-radius: 6px;
                padding: 10px 16px;
                font-size: 14px;
                font-weight: 500;
            }
            QPushButton:hover {
                background-color: #F57C00;
            }
        """)
        open_file_btn.clicked.connect(self.open_notes_file)
        
        refresh_btn = QPushButton("🔄 刷新")
        refresh_btn.setStyleSheet("""
            QPushButton {
                background-color: #9C27B0;
                color: white;
                border: none;
                border-radius: 6px;
                padding: 10px 16px;
                font-size: 14px;
                font-weight: 500;
            }
            QPushButton:hover {
                background-color: #7B1FA2;
            }
        """)
        refresh_btn.clicked.connect(self.load_notes)
        
        button_layout.addWidget(save_btn)
        button_layout.addWidget(open_file_btn)
        button_layout.addWidget(refresh_btn)
        button_layout.addStretch()
        
        card.addLayout(button_layout)
        
        # 加载现有笔记
        self.load_notes()
        
        # 创建容器widget
        notes_widget = QWidget()
        notes_widget.setLayout(card)
        return notes_widget
    
    def toggle_view_mode(self):
        """切换视图模式"""
        current_index = self.notes_stack.currentIndex()
        if current_index == 0:  # 当前是编辑模式，切换到时间轴
            self.notes_stack.setCurrentIndex(1)
            self.view_mode_btn.setText("✏️ 编辑模式")
            self.update_timeline_view()
        else:  # 当前是时间轴，切换到编辑模式
            self.notes_stack.setCurrentIndex(0)
            self.view_mode_btn.setText("📅 时间轴视图")
    
    def toggle_todo_visibility(self, state):
        """切换待办事项区域的显示/隐藏"""
        self.todo_widget.setVisible(state == Qt.Checked)
        
        # 如果显示待办事项，确保我们在编辑模式
        if state == Qt.Checked and self.notes_stack.currentIndex() != 0:
            self.notes_stack.setCurrentIndex(0)
            self.view_mode_btn.setText("📅 时间轴视图")
    
    def update_timeline_view(self):
        """更新时间轴视图"""
        # 清空现有时间轴内容
        for i in reversed(range(self.timeline_layout.count())):
            child = self.timeline_layout.itemAt(i).widget()
            if child:
                child.setParent(None)
        
        # 解析笔记内容创建时间轴条目
        notes_file_path = self.get_notes_file_path()
        if notes_file_path and os.path.exists(notes_file_path):
            try:
                with open(notes_file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    self.create_timeline_entries(content)
            except Exception as e:
                error_label = QLabel(f"❌ 无法加载笔记内容: {str(e)}")
                error_label.setStyleSheet("color: #f44336; font-size: 14px; padding: 20px;")
                self.timeline_layout.addWidget(error_label)
        else:
            empty_label = QLabel("📝 暂无笔记内容，请先在编辑模式中添加笔记")
            empty_label.setStyleSheet("""
                QLabel {
                    color: #666;
                    font-size: 16px;
                    padding: 40px;
                    text-align: center;
                    background-color: white;
                    border: 2px dashed #ddd;
                    border-radius: 8px;
                }
            """)
            empty_label.setAlignment(Qt.AlignCenter)
            self.timeline_layout.addWidget(empty_label)
        
        # 添加弹性空间
        self.timeline_layout.addStretch()
    
    def create_timeline_entries(self, content):
        """根据笔记内容创建时间轴条目"""
        lines = content.split('\n')
        current_section = None
        notes_content = []
        todos = []
        project_info = {}
        
        # 解析内容
        for line in lines:
            line = line.strip()
            if line.startswith('# ') and '项目笔记' in line:
                project_info['title'] = line.replace('# ', '').replace(' - 项目笔记', '')
            elif line.startswith('**创建时间:**'):
                project_info['created_time'] = line.replace('**创建时间:**', '').strip()
            elif line.startswith('**项目概述:**'):
                project_info['description'] = line.replace('**项目概述:**', '').strip()
            elif line.startswith('## 笔记内容'):
                current_section = 'notes'
                continue
            elif line.startswith('## 待办事项'):
                current_section = 'todos'
                continue
            elif line.startswith('##'):
                current_section = None
                continue
            
            if current_section == 'notes' and line:
                notes_content.append(line)
            elif current_section == 'todos' and line.startswith('- '):
                todo_text = line[2:].strip()
                if todo_text.startswith('[x]'):
                    todos.append((todo_text[4:].strip(), True))
                elif todo_text.startswith('[ ]'):
                    todos.append((todo_text[4:].strip(), False))
                else:
                    todos.append((todo_text, False))
        
        # 创建项目信息时间轴条目
        if project_info.get('created_time'):
            self.create_timeline_item(
                "🚀 项目创建",
                project_info.get('created_time', '未知时间'),
                f"项目 '{project_info.get('title', '未知项目')}' 创建\n{project_info.get('description', '暂无描述')}",
                "#4CAF50"
            )
        
        # 创建笔记内容时间轴条目
        if notes_content:
            # 获取文件修改时间作为笔记更新时间
            notes_file_path = self.get_notes_file_path()
            if notes_file_path and os.path.exists(notes_file_path):
                mtime = os.path.getmtime(notes_file_path)
                update_time = datetime.fromtimestamp(mtime).strftime('%Y-%m-%d %H:%M:%S')
            else:
                update_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            notes_text = '\n'.join(notes_content[:3])  # 只显示前3行
            if len(notes_content) > 3:
                notes_text += '\n...'
            
            self.create_timeline_item(
                "📝 笔记更新",
                update_time,
                notes_text,
                "#2196F3"
            )
        
        # 创建待办事项时间轴条目
        if todos:
            completed_count = sum(1 for _, completed in todos if completed)
            total_count = len(todos)
            
            todo_summary = f"总计 {total_count} 项任务，已完成 {completed_count} 项"
            if completed_count < total_count:
                recent_todos = [text for text, completed in todos if not completed][:3]
                todo_summary += "\n\n待完成任务：\n" + '\n'.join(f"• {todo}" for todo in recent_todos)
                if len([t for t, c in todos if not c]) > 3:
                    todo_summary += "\n..."
            
            self.create_timeline_item(
                "✅ 任务进展",
                datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                todo_summary,
                "#FF9800"
            )
    
    def create_timeline_item(self, title, time_str, content, color):
        """创建单个时间轴条目"""
        item_widget = QWidget()
        item_widget.setStyleSheet(f"""
            QWidget {{
                background-color: white;
                border-left: 4px solid {color};
                border-radius: 8px;
                margin-bottom: 10px;
            }}
            QWidget:hover {{
                box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            }}
        """)
        
        item_layout = QHBoxLayout(item_widget)
        item_layout.setContentsMargins(15, 15, 15, 15)
        
        # 时间轴点
        timeline_dot = QLabel("●")
        timeline_dot.setStyleSheet(f"""
            QLabel {{
                color: {color};
                font-size: 20px;
                font-weight: bold;
                min-width: 20px;
                max-width: 20px;
            }}
        """)
        timeline_dot.setAlignment(Qt.AlignTop)
        
        # 内容区域
        content_layout = QVBoxLayout()
        content_layout.setSpacing(8)
        
        # 标题和时间
        header_layout = QHBoxLayout()
        
        title_label = QLabel(title)
        title_label.setStyleSheet("""
            QLabel {
                font-size: 16px;
                font-weight: bold;
                color: #333;
            }
        """)
        
        time_label = QLabel(time_str)
        time_label.setStyleSheet("""
            QLabel {
                font-size: 12px;
                color: #666;
                background-color: #f5f5f5;
                padding: 4px 8px;
                border-radius: 4px;
            }
        """)
        
        header_layout.addWidget(title_label)
        header_layout.addStretch()
        header_layout.addWidget(time_label)
        
        # 内容文本
        content_label = QLabel(content)
        content_label.setStyleSheet("""
            QLabel {
                font-size: 14px;
                color: #555;
                line-height: 1.5;
                padding: 8px 0;
            }
        """)
        content_label.setWordWrap(True)
        
        content_layout.addLayout(header_layout)
        content_layout.addWidget(content_label)
        
        item_layout.addWidget(timeline_dot)
        item_layout.addLayout(content_layout)
        
        self.timeline_layout.addWidget(item_widget)
    
    def get_notes_file_path(self):
        """获取项目笔记文件路径"""
        if 'folder_path' in self.project and self.project['folder_path']:
            folder_path = self.project['folder_path']
            if os.path.exists(folder_path):
                notes_filename = f"{self.project['name']}_笔记.md"
                return os.path.join(folder_path, notes_filename)
        return None
    
    def load_notes(self):
        """加载项目笔记"""
        notes_file_path = self.get_notes_file_path()
        if notes_file_path and os.path.exists(notes_file_path):
            try:
                with open(notes_file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    self.parse_notes_content(content)
                    # 将笔记文件添加到资源列表
                    self.add_notes_to_resources()
            except Exception as e:
                QMessageBox.warning(self, "加载失败", f"无法加载笔记文件:\n{str(e)}")
        else:
            # 如果文件不存在，清空编辑器
            self.notes_text.clear()
            self.todo_list.clear()
    
    def parse_notes_content(self, content):
        """解析笔记内容"""
        lines = content.split('\n')
        notes_content = []
        todos = []
        
        current_section = None
        
        for line in lines:
            line = line.strip()
            if line.startswith('## 笔记内容'):
                current_section = 'notes'
                continue
            elif line.startswith('## 待办事项'):
                current_section = 'todos'
                continue
            elif line.startswith('##'):
                current_section = None
                continue
            
            if current_section == 'notes' and line:
                notes_content.append(line)
            elif current_section == 'todos' and line.startswith('- '):
                todo_text = line[2:].strip()
                if todo_text.startswith('[x]'):
                    todos.append((todo_text[4:].strip(), True))
                elif todo_text.startswith('[ ]'):
                    todos.append((todo_text[4:].strip(), False))
                else:
                    todos.append((todo_text, False))
        
        # 设置笔记内容
        self.notes_text.setPlainText('\n'.join(notes_content))
        
        # 设置待办事项
        self.todo_list.clear()
        for todo_text, completed in todos:
            item = QListWidgetItem()
            if completed:
                item.setText(f"✅ {todo_text}")
                item.setData(Qt.UserRole, True)
            else:
                item.setText(f"⬜ {todo_text}")
                item.setData(Qt.UserRole, False)
            self.todo_list.addItem(item)
    
    def add_todo_item(self):
        """添加待办事项"""
        todo_text = self.todo_input.text().strip()
        if todo_text:
            item = QListWidgetItem()
            item.setText(f"⬜ {todo_text}")
            item.setData(Qt.UserRole, False)  # False表示未完成
            self.todo_list.addItem(item)
            self.todo_input.clear()
    
    def toggle_todo_item(self, item):
        """切换待办事项完成状态"""
        completed = item.data(Qt.UserRole)
        todo_text = item.text()[2:]  # 去掉前面的图标
        
        if completed:
            item.setText(f"⬜ {todo_text}")
            item.setData(Qt.UserRole, False)
        else:
            item.setText(f"✅ {todo_text}")
            item.setData(Qt.UserRole, True)
    
    def save_notes(self):
        """保存项目笔记"""
        notes_file_path = self.get_notes_file_path()
        if not notes_file_path:
            QMessageBox.warning(self, "保存失败", "项目没有关联的文件夹，无法保存笔记")
            return
        
        try:
            # 构建笔记内容
            content = f"# {self.project['name']} - 项目笔记\n\n"
            content += f"**创建时间:** {self.project.get('created_time', '未知')}\n\n"
            content += f"**项目概述:** {self.project.get('description', '暂无描述')}\n\n"
            
            # 笔记内容
            content += "## 笔记内容\n\n"
            notes_text = self.notes_text.toPlainText().strip()
            if notes_text:
                content += notes_text + "\n\n"
            else:
                content += "暂无笔记内容\n\n"
            
            # 待办事项
            content += "## 待办事项\n\n"
            if self.todo_list.count() > 0:
                for i in range(self.todo_list.count()):
                    item = self.todo_list.item(i)
                    completed = item.data(Qt.UserRole)
                    todo_text = item.text()[2:]  # 去掉前面的图标
                    if completed:
                        content += f"- [x] {todo_text}\n"
                    else:
                        content += f"- [ ] {todo_text}\n"
            else:
                content += "暂无待办事项\n"
            
            content += "\n## 项目进展\n\n"
            content += "记录项目的重要进展和里程碑...\n"
            
            # 保存文件
            with open(notes_file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            # 将笔记文件添加到资源列表
            self.add_notes_to_resources()
            
            QMessageBox.information(self, "保存成功", f"笔记已保存到:\n{notes_file_path}")
            
        except Exception as e:
            QMessageBox.critical(self, "保存失败", f"无法保存笔记文件:\n{str(e)}")
    
    def add_notes_to_resources(self):
        """将笔记文件添加到项目资源中"""
        notes_file_path = self.get_notes_file_path()
        if notes_file_path and os.path.exists(notes_file_path):
            # 检查是否已经在资源列表中
            if 'resources' not in self.project:
                self.project['resources'] = []
            
            # 检查是否已存在
            for resource in self.project['resources']:
                if resource.get('path') == notes_file_path:
                    return  # 已存在，不重复添加
            
            # 添加笔记文件到资源
            notes_resource = {
                'name': f"{self.project['name']}_笔记.md",
                'path': notes_file_path,
                'type': '项目笔记',
                'description': '项目笔记文件'
            }
            self.project['resources'].append(notes_resource)
            
            # 保存项目数据
            self.parent_tool.update_project_modified_time(self.project['name'], save_immediately=False)
            self.parent_tool.save_data()
            self.parent_tool.refresh_project_list()
            
            # 刷新资源列表显示
            self.load_resources()
    
    def open_notes_file(self):
        """打开笔记文件"""
        notes_file_path = self.get_notes_file_path()
        if notes_file_path and os.path.exists(notes_file_path):
            try:
                if sys.platform.startswith('win'):
                    os.startfile(notes_file_path)
                elif sys.platform.startswith('darwin'):  # macOS
                    subprocess.run(['open', notes_file_path])
                else:  # Linux
                    subprocess.run(['xdg-open', notes_file_path])
            except Exception as e:
                QMessageBox.warning(self, "打开失败", f"无法打开笔记文件:\n{str(e)}")
        else:
            QMessageBox.warning(self, "文件不存在", "笔记文件不存在，请先保存笔记")


class ResourceInventoryDialog(QDialog):
    """资源清单对话框"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent_tool = parent
        self.init_ui()
        self.load_all_resources()
    
    def init_ui(self):
        """初始化UI"""
        self.setWindowTitle("资源清单 - 所有项目资源汇总")
        width, height = get_optimal_window_size()
        self.resize(width, height)
        self.setMinimumSize(800, 600)
        center_window(self)
        self.setModal(True)
        
        # 设置窗口样式
        self.setStyleSheet("""
            QDialog {
                background-color: #f8f9fa;
            }
        """)
        
        layout = QVBoxLayout(self)
        layout.setSpacing(16)
        layout.setContentsMargins(20, 20, 20, 20)
        
        # 标题区域
        title_layout = QHBoxLayout()
        
        title_label = QLabel("📋 资源清单")
        title_label.setStyleSheet("""
            QLabel {
                font-size: 24px;
                font-weight: bold;
                color: #2c3e50;
                margin-bottom: 10px;
            }
        """)
        title_layout.addWidget(title_label)
        
        title_layout.addStretch()
        
        # 刷新按钮
        refresh_btn = QPushButton("🔄 刷新")
        refresh_btn.setStyleSheet("""
            QPushButton {
                background-color: #17a2b8;
                color: white;
                border: none;
                border-radius: 6px;
                padding: 8px 16px;
                font-size: 14px;
                font-weight: 500;
            }
            QPushButton:hover {
                background-color: #138496;
            }
        """)
        refresh_btn.clicked.connect(self.load_all_resources)
        title_layout.addWidget(refresh_btn)
        

        
        layout.addLayout(title_layout)
        
       
        
        # 筛选区域
        filter_layout = QHBoxLayout()
        
        # 项目筛选
        project_filter_label = QLabel("项目:")
        project_filter_label.setStyleSheet("""
            QLabel {
                font-size: 14px;
                font-weight: 600;
                color: #495057;
            }
        """)
        filter_layout.addWidget(project_filter_label)
        
        self.project_filter_combo = QComboBox()
        self.project_filter_combo.setStyleSheet("""
            QComboBox {
                border: 1px solid #e0e0e0;
                border-radius: 6px;
                padding: 8px 12px;
                background-color: white;
                font-size: 14px;
                min-width: 150px;
            }
            QComboBox:hover {
                border-color: #80bdff;
            }
        """)
        self.project_filter_combo.currentTextChanged.connect(self.filter_resources)
        filter_layout.addWidget(self.project_filter_combo)
        
        # 资源类型筛选
        type_filter_label = QLabel("类型:")
        type_filter_label.setStyleSheet("""
            QLabel {
                font-size: 14px;
                font-weight: 600;
                color: #495057;
                margin-left: 20px;
            }
        """)
        filter_layout.addWidget(type_filter_label)
        
        self.type_filter_combo = QComboBox()
        self.type_filter_combo.setStyleSheet("""
            QComboBox {
                border: 1px solid #e0e0e0;
                border-radius: 6px;
                padding: 8px 12px;
                background-color: white;
                font-size: 14px;
                min-width: 120px;
            }
            QComboBox:hover {
                border-color: #80bdff;
            }
        """)
        self.type_filter_combo.currentTextChanged.connect(self.filter_resources)
        filter_layout.addWidget(self.type_filter_combo)
        
        # 搜索框
        search_label = QLabel("搜索:")
        search_label.setStyleSheet("""
            QLabel {
                font-size: 14px;
                font-weight: 600;
                color: #495057;
                margin-left: 20px;
            }
        """)
        filter_layout.addWidget(search_label)
        
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("搜索资源名称...")
        self.search_input.setStyleSheet("""
            QLineEdit {
                border: 1px solid #e0e0e0;
                border-radius: 6px;
                padding: 8px 12px;
                background-color: white;
                font-size: 14px;
                min-width: 200px;
            }
            QLineEdit:focus {
                border-color: #2196F3;
            }
        """)
        self.search_input.textChanged.connect(self.filter_resources)
        filter_layout.addWidget(self.search_input)
        
        filter_layout.addStretch()
        layout.addLayout(filter_layout)
        
        # 资源列表
        self.resource_tree = QTreeWidget()
        self.resource_tree.setHeaderLabels(["资源名称", "所属项目", "资源类型", "文件类型", "资源路径", "引用次数"])
        self.resource_tree.setStyleSheet(DesignSystem.tree_style())
        
        # 禁用列宽调整
        header = self.resource_tree.header()
        header.setSectionsMovable(False)
        header.setSectionResizeMode(QHeaderView.Fixed)
        
        # 禁用水平滚动条，确保表格完全适应可见区域
        self.resource_tree.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        
        # 启用自动换行，确保资源名称可以自动换行
        self.resource_tree.setWordWrap(True)
        
        # 连接窗口大小变化事件，自动调整列宽
        self.resource_tree.header().geometriesChanged.connect(self.adjust_resource_table_columns)
        
        # 启用右键菜单
        self.resource_tree.setContextMenuPolicy(Qt.CustomContextMenu)
        self.resource_tree.customContextMenuRequested.connect(self.show_context_menu)
        
        layout.addWidget(self.resource_tree)
        
        # 按钮区域
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        
        close_btn = QPushButton("关闭")
        close_btn.setStyleSheet("""
            QPushButton {
                background-color: #6c757d;
                color: white;
                border: none;
                border-radius: 6px;
                padding: 10px 24px;
                font-size: 14px;
                font-weight: 500;
                min-width: 80px;
            }
            QPushButton:hover {
                background-color: #5a6268;
            }
        """)
        close_btn.clicked.connect(self.close)
        button_layout.addWidget(close_btn)
        
        layout.addLayout(button_layout)
    
    def load_all_resources(self):
        """加载所有项目的资源（去重处理）"""
        self.all_resources = []
        projects = self.parent_tool.projects if self.parent_tool else []
        
        # 用于去重的字典：(name, path) -> resource_info
        resource_map = {}
        
        for project in projects:
            project_name = project.get('name', '')
            resources = project.get('resources', [])
            
            for resource in resources:
                resource_name = resource.get('name', '')
                resource_path = resource.get('path', '')
                
                # 使用name和path作为唯一标识
                key = (resource_name, resource_path)
                if key in resource_map:
                    # 已存在，添加项目到引用列表（如果还没有）
                    if project_name not in resource_map[key]['projects']:
                        resource_map[key]['projects'].append(project_name)
                else:
                    # 新资源
                    resource_info = {
                        'name': resource_name,
                        'project': project_name,
                        'type': resource.get('type', ''),
                        'file_type': self.get_file_extension(resource_path),
                        'path': resource_path,
                        'category': resource.get('category', ''),
                        'tags': resource.get('tags', []),
                        'status': resource.get('status', ''),
                        'reference_count': 0,
                        'projects': [project_name]  # 记录引用此资源的项目
                    }
                    resource_map[key] = resource_info
        
        # 合并去重后的资源并设置引用次数（引用次数 = 引用该资源的项目数量）
        for key, resource_info in resource_map.items():
            resource_info['reference_count'] = len(resource_info['projects'])
            # 如果被多个项目引用，显示第一个项目名称
            if len(resource_info['projects']) > 1:
                resource_info['project'] = f"{resource_info['projects'][0]} (+{len(resource_info['projects'])-1})"
            self.all_resources.append(resource_info)
        
        self.update_filters()
        self.display_resources(self.all_resources)
    
    def get_file_extension(self, file_path):
        """获取文件扩展名"""
        if not file_path:
            return ''
        return os.path.splitext(file_path)[1].lower()
    
    # 删除更新统计信息方法
    
    def update_filters(self):
        """更新筛选器选项"""
        # 更新项目筛选器
        self.project_filter_combo.clear()
        self.project_filter_combo.addItem("全部项目")
        
        projects = set()
        for resource in self.all_resources:
            if resource['project']:
                projects.add(resource['project'])
        
        for project in sorted(projects):
            self.project_filter_combo.addItem(project)
        
        # 更新资源类型筛选器
        self.type_filter_combo.clear()
        self.type_filter_combo.addItem("全部类型")
        
        resource_types = set()
        for resource in self.all_resources:
            if resource['type']:
                resource_types.add(resource['type'])
        
        for resource_type in sorted(resource_types):
            self.type_filter_combo.addItem(resource_type)
    
    def filter_resources(self):
        """筛选资源"""
        project_filter = self.project_filter_combo.currentText()
        type_filter = self.type_filter_combo.currentText()
        search_text = self.search_input.text().lower()
        
        filtered_resources = []
        
        for resource in self.all_resources:
            # 项目筛选
            if project_filter != "全部项目" and resource['project'] != project_filter:
                continue
            
            # 类型筛选
            if type_filter != "全部类型" and resource['type'] != type_filter:
                continue
            
            # 搜索筛选
            if search_text and search_text not in resource['name'].lower():
                continue
            
            filtered_resources.append(resource)
        
        self.display_resources(filtered_resources)
    
    def display_resources(self, resources):
        """显示资源列表"""
        self.resource_tree.clear()
        
        for resource in resources:
            item = QTreeWidgetItem([
                resource['name'],
                resource['project'],
                resource['type'],
                resource['file_type'],
                resource['path'],
                str(resource.get('reference_count', 1))
            ])
            
            # 设置工具提示
            item.setToolTip(0, f"资源名称: {resource['name']}")
            item.setToolTip(1, f"所属项目: {resource['project']}")
            item.setToolTip(2, f"资源类型: {resource['type']}")
            item.setToolTip(3, f"文件类型: {resource['file_type']}")
            item.setToolTip(4, f"资源路径: {resource['path']}")
            
            # 引用次数的工具提示
            reference_count = resource.get('reference_count', 1)
            projects_list = resource.get('projects', [])
            if reference_count > 1 and projects_list:
                projects_text = '、'.join(projects_list)
                item.setToolTip(6, f"引用次数: {reference_count}\n引用项目: {projects_text}")
            else:
                item.setToolTip(6, f"引用次数: {reference_count}")
            
            # 根据资源类型设置图标颜色
            if resource['type'] == '电子书':
                item.setForeground(2, QColor('#e74c3c'))
            elif resource['type'] == '视频':
                item.setForeground(2, QColor('#3498db'))
            elif resource['type'] == '代码':
                item.setForeground(2, QColor('#2ecc71'))
            elif resource['type'] == '文档':
                item.setForeground(2, QColor('#f39c12'))
            elif resource['type'] == '网页链接':
                item.setForeground(2, QColor('#9b59b6'))
            
            # 根据引用次数设置引用次数列的颜色
            if reference_count > 1:
                item.setForeground(6, QColor('#e74c3c'))  # 红色表示多次引用
                item.setBackground(6, QColor('#fff5f5'))  # 浅红色背景
            else:
                item.setForeground(6, QColor('#6c757d'))  # 灰色表示单次引用
            
            self.resource_tree.addTopLevelItem(item)
    
    def adjust_resource_table_columns(self):
        """动态调整资源表格列宽
        
        根据表格可见区域宽度，按比例分配列宽：
        - 资源名称列：1.4倍（重要，较宽）
        - 所属项目列：1.0倍
        - 资源类型列：0.8倍
        - 文件类型列：0.8倍
        - 资源路径列：1.0倍
        - 引用次数列：0.8倍
        确保所有列都在可见范围内，不出现水平滚动条
        """
        if not hasattr(self, 'resource_tree'):
            return
        
        # 获取表格可见区域宽度
        table_width = self.resource_tree.viewport().width()
        
        # 获取列数
        column_count = self.resource_tree.columnCount()
        
        if column_count == 0:
            return
        
        # 定义各列的宽度比例
        column_ratios = {
            0: 1.4,    # 资源名称：1.4倍（重要，较宽）
            1: 1.0,    # 所属项目：1.0倍
            2: 0.6,    # 资源类型：0.6倍
            3: 0.3,    # 文件类型：0.3倍
            4: 1.9,    # 资源路径：1.9倍（重要，较宽）
            5: 0.6,    # 引用次数：0.6倍
        }
        
        # 计算比例总和
        total_ratio = sum(column_ratios.values())
        
        # 计算各列宽度，确保总宽度不超过可见区域
        header = self.resource_tree.header()
        for col in range(column_count):
            ratio = column_ratios.get(col, 1.0)
            # 使用比例占总和的比例来分配宽度
            width = int(table_width * (ratio / total_ratio))
            header.resizeSection(col, width)
    
    def show_context_menu(self, position):
        """显示右键菜单"""
        item = self.resource_tree.itemAt(position)
        if not item:
            return
        
        menu = QMenu(self)
        menu.setStyleSheet("""
            QMenu {
                background-color: white;
                border: 1px solid #e0e0e0;
                border-radius: 6px;
                padding: 4px;
            }
            QMenu::item {
                padding: 8px 16px;
                border-radius: 4px;
            }
            QMenu::item:selected {
                background-color: #e3f2fd;
                color: #2196F3;
            }
        """)
        
        # 打开文件
        open_action = QAction("📂 打开文件", self)
        open_action.triggered.connect(lambda: self.open_resource_file(item))
        menu.addAction(open_action)
        
        # 打开文件夹
        open_folder_action = QAction("📁 打开所在文件夹", self)
        open_folder_action.triggered.connect(lambda: self.open_resource_folder(item))
        menu.addAction(open_folder_action)
        
        menu.addSeparator()
        
        # 复制路径
        copy_path_action = QAction("📋 复制路径", self)
        copy_path_action.triggered.connect(lambda: self.copy_resource_path(item))
        menu.addAction(copy_path_action)
        

        
        menu.exec_(self.resource_tree.mapToGlobal(position))
    
    def open_resource_file(self, item):
        """打开资源文件"""
        file_path = item.text(4)  # 资源路径列
        if file_path and os.path.exists(file_path):
            try:
                if sys.platform.startswith('win'):
                    os.startfile(file_path)
                elif sys.platform.startswith('darwin'):  # macOS
                    subprocess.run(['open', file_path])
                else:  # Linux
                    subprocess.run(['xdg-open', file_path])
            except Exception as e:
                QMessageBox.warning(self, "打开失败", f"无法打开文件:\n{str(e)}")
        else:
            QMessageBox.warning(self, "文件不存在", "文件不存在或路径无效")
    
    def open_resource_folder(self, item):
        """打开资源所在文件夹"""
        file_path = item.text(4)  # 资源路径列
        if file_path and os.path.exists(file_path):
            folder_path = os.path.dirname(file_path)
            try:
                if sys.platform.startswith('win'):
                    subprocess.run(['explorer', '/select,', file_path])
                elif sys.platform.startswith('darwin'):  # macOS
                    subprocess.run(['open', '-R', file_path])
                else:  # Linux
                    subprocess.run(['xdg-open', folder_path])
            except Exception as e:
                QMessageBox.warning(self, "打开失败", f"无法打开文件夹:\n{str(e)}")
        else:
            QMessageBox.warning(self, "文件不存在", "文件不存在或路径无效")
    
    def copy_resource_path(self, item):
        """复制资源路径"""
        file_path = item.text(4)  # 资源路径列
        if file_path:
            clipboard = QApplication.clipboard()
            clipboard.setText(file_path)
            QMessageBox.information(self, "复制成功", "资源路径已复制到剪贴板")
    

    



class NoteEditDialog(QDialog):
    """笔记编辑对话框"""
    
    def __init__(self, parent=None, note_data=None, project=None):
        super().__init__(parent)
        self.note_data = note_data
        self.project = project
        self.init_ui()
        
        # 如果是编辑模式，加载现有数据
        if note_data:
            self.title_input.setText(note_data.get('title', ''))
            self.content_input.setPlainText(note_data.get('content', ''))
    
    def init_ui(self):
        """初始化UI"""
        self.setWindowTitle("编辑笔记" if self.note_data else "添加笔记")
        width, height = get_optimal_dialog_size(800, 600)
        self.setFixedSize(width, height)
        center_window(self)
        self.setModal(True)
        
        # 设置窗口样式
        self.setStyleSheet("""
            QDialog {
                background-color: #f8f9fa;
            }
        """)
        
        layout = QVBoxLayout(self)
        layout.setSpacing(15)
        layout.setContentsMargins(20, 20, 20, 20)
        
        # 标题
        title_label = QLabel("编辑笔记" if self.note_data else "添加新笔记")
        title_label.setStyleSheet("""
            QLabel {
                font-size: 18px;
                font-weight: bold;
                color: #333;
                margin-bottom: 10px;
            }
        """)
        layout.addWidget(title_label)
        
        # 笔记标题输入
        title_input_label = QLabel("笔记标题:")
        title_input_label.setStyleSheet("""
            QLabel {
                font-size: 14px;
                font-weight: 600;
                color: #333;
                margin-bottom: 5px;
            }
        """)
        layout.addWidget(title_input_label)
        
        self.title_input = QLineEdit()
        self.title_input.setPlaceholderText("请输入笔记标题（可选）")
        self.title_input.setStyleSheet("""
            QLineEdit {
                border: 2px solid #e8e8e8;
                border-radius: 6px;
                padding: 10px 12px;
                font-size: 14px;
                background-color: white;
            }
            QLineEdit:focus {
                border-color: #4CAF50;
            }
        """)
        layout.addWidget(self.title_input)
        
        # 笔记内容输入
        content_input_label = QLabel("笔记内容:")
        content_input_label.setStyleSheet("""
            QLabel {
                font-size: 14px;
                font-weight: 600;
                color: #333;
                margin-bottom: 5px;
                margin-top: 10px;
            }
        """)
        layout.addWidget(content_input_label)
        
        self.content_input = QTextEdit()
        self.content_input.setPlaceholderText("请输入笔记内容...")
        self.content_input.setMinimumHeight(280)
        self.content_input.setStyleSheet("""
            QTextEdit {
                border: 2px solid #e8e8e8;
                border-radius: 8px;
                padding: 12px;
                font-size: 14px;
                background-color: white;
                font-family: 'Microsoft YaHei UI', sans-serif;
                line-height: 1.5;
            }
            QTextEdit:focus {
                border-color: #4CAF50;
            }
        """)
        layout.addWidget(self.content_input)
        
        # 按钮区域
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        
        # 取消按钮
        cancel_btn = QPushButton("取消")
        cancel_btn.setStyleSheet("""
            QPushButton {
                background-color: #6c757d;
                color: white;
                border: none;
                border-radius: 6px;
                padding: 10px 24px;
                font-size: 14px;
                font-weight: 500;
                min-width: 80px;
            }
            QPushButton:hover {
                background-color: #5a6268;
            }
            QPushButton:pressed {
                background-color: #545b62;
            }
        """)
        cancel_btn.clicked.connect(self.reject)
        button_layout.addWidget(cancel_btn)
        
        # 保存按钮
        save_btn = QPushButton("保存")
        save_btn.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 6px;
                padding: 10px 24px;
                font-size: 14px;
                font-weight: 500;
                min-width: 80px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:pressed {
                background-color: #3d8b40;
            }
        """)
        save_btn.clicked.connect(self.accept)
        button_layout.addWidget(save_btn)
        
        layout.addLayout(button_layout)
        
        # 设置焦点到内容输入框
        self.content_input.setFocus()
    
    def get_note_data(self):
        """获取笔记数据"""
        title = self.title_input.text().strip()
        content = self.content_input.toPlainText().strip()
        return {
            'title': title,
            'content': content,
            'timestamp': datetime.now().isoformat()
        }


class RelinkResourceDialog(QDialog):
    """重新链接资源对话框"""
    
    def __init__(self, parent=None, resource_name="", old_file_path=""):
        super().__init__(parent)
        self.resource_name = resource_name
        self.old_file_path = old_file_path
        self.new_file_path = ""
        self.init_ui()
    
    def init_ui(self):
        """初始化UI"""
        self.setWindowTitle("重新链接资源")
        width, height = get_optimal_dialog_size(600, 400)
        self.setFixedSize(width, height)
        center_window(self)
        self.setWindowFlags(self.windowFlags() | Qt.MSWindowsFixedSizeDialogHint)
        
        # 设置对话框样式
        self.setStyleSheet("""
            QDialog {
                background-color: #f8f9fa;
            }
        """)
        
        main_layout = QVBoxLayout(self)
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(0, 0, 0, 0)
        
        # 创建内容区域
        content_widget = QFrame()
        content_widget.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 8px;
                margin: 10px;
            }
        """)
        
        content_layout = QVBoxLayout(content_widget)
        content_layout.setSpacing(20)
        content_layout.setContentsMargins(20, 20, 20, 20)
        
        # 标题
        title_label = QLabel("🔗 重新链接资源")
        title_label.setStyleSheet("""
            QLabel {
                font-size: 18px;
                font-weight: bold;
                color: #1a1a1a;
                margin-bottom: 10px;
            }
        """)
        content_layout.addWidget(title_label)
        
        # 说明文字
        info_label = QLabel(f"资源 '{self.resource_name}' 的文件路径已失效，请选择新的文件路径来重新链接该资源。")
        info_label.setStyleSheet("""
            QLabel {
                font-size: 14px;
                color: #666;
                margin-bottom: 15px;
                line-height: 1.4;
            }
        """)
        info_label.setWordWrap(True)
        content_layout.addWidget(info_label)
        
        # 原路径信息
        old_path_group = QVBoxLayout()
        old_path_label = QLabel("原文件路径:")
        old_path_label.setStyleSheet("""
            QLabel {
                font-size: 13px;
                font-weight: 600;
                color: #333;
                margin-bottom: 5px;
            }
        """)
        old_path_group.addWidget(old_path_label)
        
        self.old_path_display = QLineEdit()
        self.old_path_display.setText(self.old_file_path or "无")
        self.old_path_display.setReadOnly(True)
        self.old_path_display.setStyleSheet("""
            QLineEdit {
                border: 2px solid #ffcdd2;
                border-radius: 6px;
                padding: 10px 12px;
                font-size: 13px;
                background-color: #ffebee;
                color: #c62828;
            }
        """)
        old_path_group.addWidget(self.old_path_display)
        content_layout.addLayout(old_path_group)
        
        # 新路径选择
        new_path_group = QVBoxLayout()
        new_path_label = QLabel("新文件路径:")
        new_path_label.setStyleSheet("""
            QLabel {
                font-size: 13px;
                font-weight: 600;
                color: #333;
                margin-bottom: 5px;
            }
        """)
        new_path_group.addWidget(new_path_label)
        
        path_layout = QHBoxLayout()
        path_layout.setSpacing(10)
        
        self.new_path_edit = QLineEdit()
        self.new_path_edit.setPlaceholderText("请选择新的文件路径")
        self.new_path_edit.setStyleSheet("""
            QLineEdit {
                border: 2px solid #e0e0e0;
                border-radius: 6px;
                padding: 10px 12px;
                font-size: 13px;
                background-color: #fafafa;
            }
            QLineEdit:focus {
                border-color: #4CAF50;
                background-color: white;
            }
        """)
        self.new_path_edit.textChanged.connect(self.on_path_changed)
        path_layout.addWidget(self.new_path_edit)
        
        browse_btn = QPushButton("浏览")
        browse_btn.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;
                color: white;
                border: none;
                border-radius: 6px;
                padding: 10px 20px;
                font-size: 13px;
                font-weight: 500;
                min-width: 80px;
            }
            QPushButton:hover {
                background-color: #1976D2;
            }
        """)
        browse_btn.clicked.connect(self.browse_file)
        path_layout.addWidget(browse_btn)
        
        new_path_group.addLayout(path_layout)
        content_layout.addLayout(new_path_group)
        
        # 文件信息显示
        self.file_info_label = QLabel("💡 请选择要链接的文件")
        self.file_info_label.setStyleSheet("""
            QLabel {
                background-color: #f0f8ff;
                border: 1px solid #e1f5fe;
                border-radius: 6px;
                padding: 15px;
                font-size: 13px;
                color: #0277bd;
                margin: 10px 0;
            }
        """)
        self.file_info_label.setWordWrap(True)
        content_layout.addWidget(self.file_info_label)
        
        # 按钮区域
        button_layout = QHBoxLayout()
        button_layout.setSpacing(10)
        
        cancel_btn = QPushButton("取消")
        cancel_btn.setStyleSheet("""
            QPushButton {
                background-color: #f5f5f5;
                color: #666;
                border: 1px solid #ddd;
                border-radius: 6px;
                padding: 10px 20px;
                font-size: 14px;
                font-weight: 500;
                min-width: 80px;
            }
            QPushButton:hover {
                background-color: #e9e9e9;
                border-color: #ccc;
            }
        """)
        cancel_btn.clicked.connect(self.reject)
        
        self.relink_btn = QPushButton("重新链接")
        self.relink_btn.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 6px;
                padding: 10px 20px;
                font-size: 14px;
                font-weight: 500;
                min-width: 100px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:disabled {
                background-color: #cccccc;
                color: #666666;
            }
        """)
        self.relink_btn.clicked.connect(self.accept)
        self.relink_btn.setEnabled(False)  # 初始状态禁用
        
        button_layout.addStretch()
        button_layout.addWidget(cancel_btn)
        button_layout.addWidget(self.relink_btn)
        
        content_layout.addLayout(button_layout)
        main_layout.addWidget(content_widget)
        
        # 居中显示
        if self.parent():
            parent_geometry = self.parent().geometry()
            x = parent_geometry.x() + (parent_geometry.width() - self.width()) // 2
            y = parent_geometry.y() + (parent_geometry.height() - self.height()) // 2
            self.move(x, y)
    
    def browse_file(self):
        """浏览文件"""
        file_path, _ = QFileDialog.getOpenFileName(
            self, 
            "选择新的资源文件", 
            os.path.dirname(self.old_file_path) if self.old_file_path else "", 
            "所有文件 (*.*)"
        )
        if file_path:
            self.new_path_edit.setText(file_path)
    
    def on_path_changed(self, text):
        """路径输入框内容变化时的处理"""
        path = text.strip()
        self.new_file_path = path
        
        if path and os.path.exists(path):
            # 文件存在，显示文件信息
            try:
                file_size = os.path.getsize(path)
                size_str = self.format_file_size(file_size)
                file_name = os.path.basename(path)
                
                info_text = f"✅ 文件有效\n📄 文件名: {file_name}\n📏 大小: {size_str}\n📁 路径: {path}"
                self.file_info_label.setText(info_text)
                self.file_info_label.setStyleSheet("""
                    QLabel {
                        background-color: #f0fff0;
                        border: 1px solid #c8e6c9;
                        border-radius: 6px;
                        padding: 15px;
                        font-size: 13px;
                        color: #2e7d32;
                        margin: 10px 0;
                    }
                """)
                self.relink_btn.setEnabled(True)
            except Exception as e:
                self.file_info_label.setText(f"⚠️ 文件信息读取失败: {str(e)}")
                self.file_info_label.setStyleSheet("""
                    QLabel {
                        background-color: #fff3e0;
                        border: 1px solid #ffcc02;
                        border-radius: 6px;
                        padding: 15px;
                        font-size: 13px;
                        color: #f57c00;
                        margin: 10px 0;
                    }
                """)
                self.relink_btn.setEnabled(False)
        elif path:
            # 路径不为空但文件不存在
            self.file_info_label.setText("❌ 文件不存在或路径无效")
            self.file_info_label.setStyleSheet("""
                QLabel {
                    background-color: #ffebee;
                    border: 1px solid #ef5350;
                    border-radius: 6px;
                    padding: 15px;
                    font-size: 13px;
                    color: #c62828;
                    margin: 10px 0;
                }
            """)
            self.relink_btn.setEnabled(False)
        else:
            # 路径为空
            self.file_info_label.setText("💡 请选择要链接的文件")
            self.file_info_label.setStyleSheet("""
                QLabel {
                    background-color: #f0f8ff;
                    border: 1px solid #e1f5fe;
                    border-radius: 6px;
                    padding: 15px;
                    font-size: 13px;
                    color: #0277bd;
                    margin: 10px 0;
                }
            """)
            self.relink_btn.setEnabled(False)
    
    def format_file_size(self, size_bytes):
        """格式化文件大小"""
        if size_bytes == 0:
            return "0 B"
        size_names = ["B", "KB", "MB", "GB", "TB"]
        import math
        i = int(math.floor(math.log(size_bytes, 1024)))
        p = math.pow(1024, i)
        s = round(size_bytes / p, 2)
        return f"{s} {size_names[i]}"
    
    def get_new_file_path(self):
        """获取新的文件路径"""
        return self.new_file_path

    def cleanup(self):
        """清理资源"""
        # 停止自动扫描定时器
        if self.auto_scan_timer:
            self.auto_scan_timer.stop()
            self.auto_scan_timer.deleteLater()
            self.auto_scan_timer = None
        
        # 关闭所有打开的项目详情对话框
        for dialog in self.open_project_dialogs:
            if hasattr(dialog, 'close'):
                dialog.close()
        self.open_project_dialogs.clear()


# ==================== IAOS脚本管理器注册（新增，不影响现有代码） ====================

TOOL_INFO = KnowledgeManagerTool.TOOL_INFO


# ==================== IAOS脚本管理器注册类（新增，不影响现有代码） ====================

class KnowledgeManagerRegistry:
    """
    个人知识管理工具 - 脚本管理器注册信息
    
    此类仅供 IAOS 脚本管理器使用，不影响桌面应用运行
    """
    
    # ==================== 方法定义 ====================
    METHODS = {
        # ==================== 数据查询类（无需UI实例） ====================
        'list_projects': {
            'description': '获取项目列表',
            'category': '数据查询',
            'params': {},
            'returns': {
                'type': 'array',
                'description': '项目列表'
            }
        },
        'get_project': {
            'description': '获取项目详情',
            'category': '数据查询',
            'params': {
                'project_id': {
                    'type': 'string',
                    'required': True,
                    'description': '项目ID'
                }
            },
            'returns': {
                'type': 'object',
                'description': '项目详情'
            }
        },
        'get_project_by_name': {
            'description': '根据名称获取项目',
            'category': '数据查询',
            'params': {
                'project_name': {
                    'type': 'string',
                    'required': True,
                    'description': '项目名称'
                }
            },
            'returns': {
                'type': 'object',
                'description': '项目详情'
            }
        },
        'list_resources': {
            'description': '获取项目的资源列表',
            'category': '数据查询',
            'params': {
                'project_id': {
                    'type': 'string',
                    'required': False,
                    'description': '项目ID，不传则返回所有资源'
                },
                'resource_type': {
                    'type': 'string',
                    'required': False,
                    'description': '资源类型筛选'
                }
            },
            'returns': {
                'type': 'array',
                'description': '资源列表'
            }
        },
        'search_resources': {
            'description': '搜索资源',
            'category': '数据查询',
            'params': {
                'keyword': {
                    'type': 'string',
                    'required': True,
                    'description': '搜索关键词'
                }
            },
            'returns': {
                'type': 'array',
                'description': '匹配的资源列表'
            }
        },
        'get_resource_types': {
            'description': '获取资源类型配置',
            'category': '数据查询',
            'params': {},
            'returns': {
                'type': 'object',
                'description': '资源类型配置'
            }
        },
        'get_project_types': {
            'description': '获取项目类型列表',
            'category': '数据查询',
            'params': {},
            'returns': {
                'type': 'array',
                'description': '项目类型列表'
            }
        },
        
        # ==================== 数据操作类（直接操作数据文件） ====================
        'create_project': {
            'description': '创建新项目',
            'category': '数据操作',
            'params': {
                'name': {
                    'type': 'string',
                    'required': True,
                    'description': '项目名称'
                },
                'description': {
                    'type': 'string',
                    'required': False,
                    'description': '项目描述'
                },
                'project_type': {
                    'type': 'string',
                    'required': False,
                    'description': '项目类型'
                },
                'tags': {
                    'type': 'array',
                    'required': False,
                    'description': '项目标签'
                },
                'create_folder': {
                    'type': 'boolean',
                    'required': False,
                    'default': True,
                    'description': '是否创建项目文件夹，默认True'
                },
                'folder_path': {
                    'type': 'string',
                    'required': False,
                    'description': '指定的父文件夹路径，不指定则使用默认路径'
                }
            },
            'returns': {
                'type': 'object',
                'description': '创建结果，包含项目ID和文件夹路径'
            }
        },
        'update_project': {
            'description': '更新项目信息',
            'category': '数据操作',
            'params': {
                'project_id': {
                    'type': 'string',
                    'required': True,
                    'description': '项目ID'
                },
                'name': {
                    'type': 'string',
                    'required': False,
                    'description': '项目名称'
                },
                'description': {
                    'type': 'string',
                    'required': False,
                    'description': '项目描述'
                },
                'project_type': {
                    'type': 'string',
                    'required': False,
                    'description': '项目类型'
                },
                'tags': {
                    'type': 'array',
                    'required': False,
                    'description': '项目标签'
                },
                'status': {
                    'type': 'string',
                    'required': False,
                    'description': '项目状态'
                }
            },
            'returns': {
                'type': 'object',
                'description': '更新结果'
            }
        },
        'delete_project': {
            'description': '删除项目',
            'category': '数据操作',
            'params': {
                'project_id': {
                    'type': 'string',
                    'required': True,
                    'description': '项目ID'
                }
            },
            'returns': {
                'type': 'object',
                'description': '删除结果'
            }
        },
        'add_resource': {
            'description': '添加资源到项目',
            'category': '数据操作',
            'params': {
                'project_id': {
                    'type': 'string',
                    'required': True,
                    'description': '项目ID'
                },
                'name': {
                    'type': 'string',
                    'required': True,
                    'description': '资源名称'
                },
                'path': {
                    'type': 'string',
                    'required': True,
                    'description': '资源路径'
                },
                'resource_type': {
                    'type': 'string',
                    'required': False,
                    'description': '资源类型'
                },
                'category': {
                    'type': 'string',
                    'required': False,
                    'description': '资源分类（参考资料/灵感火花/产出成品）'
                }
            },
            'returns': {
                'type': 'object',
                'description': '添加结果'
            }
        },
        'remove_resource': {
            'description': '从项目中移除资源',
            'category': '数据操作',
            'params': {
                'project_id': {
                    'type': 'string',
                    'required': True,
                    'description': '项目ID'
                },
                'resource_path': {
                    'type': 'string',
                    'required': True,
                    'description': '资源路径'
                }
            },
            'returns': {
                'type': 'object',
                'description': '移除结果'
            }
        },
        'get_project_notes': {
            'description': '获取项目笔记',
            'category': '数据操作',
            'params': {
                'project_id': {
                    'type': 'string',
                    'required': True,
                    'description': '项目ID'
                }
            },
            'returns': {
                'type': 'object',
                'description': '项目笔记内容'
            }
        },
        'save_project_note': {
            'description': '保存项目笔记',
            'category': '数据操作',
            'params': {
                'project_id': {
                    'type': 'string',
                    'required': True,
                    'description': '项目ID'
                },
                'content': {
                    'type': 'string',
                    'required': True,
                    'description': '笔记内容'
                }
            },
            'returns': {
                'type': 'object',
                'description': '保存结果'
            }
        },
        
        # ==================== 应用控制类（需要启动应用） ====================
        'launch': {
            'description': '启动知识管理工具',
            'category': '应用控制',
            'params': {},
            'returns': {
                'type': 'object',
                'description': '启动结果'
            }
        }
    }
    
    # ==================== 方法别名 ====================
    METHOD_ALIASES = {
        'projects': 'list_projects',
        'project': 'get_project',
        'resources': 'list_resources',
        'add_project': 'create_project',
        'remove_project': 'delete_project'
    }
    
    # ==================== 辅助函数 ====================
    @staticmethod
    def _get_data_file_path(filename: str, env: dict = None) -> str:
        """
        获取数据文件路径（复用现有逻辑）
        
        Args:
            filename: 数据文件名
            env: 环境信息字典（由IAOSScriptManager传递）
        
        Returns:
            str: 数据文件完整路径
        """
        if env is None:
            env = {}
        
        # 使用环境信息中的路径
        data_dir = env.get('data_dir', 'data')
        return os.path.join(data_dir, filename)
    
    @staticmethod
    def _get_config_file_path(filename: str, env: dict = None) -> str:
        """
        获取配置文件路径
        
        Args:
            filename: 配置文件名
            env: 环境信息字典（由IAOSScriptManager传递）
        
        Returns:
            str: 配置文件完整路径
        """
        if env is None:
            env = {}
        
        # 使用环境信息中的路径
        config_dir = env.get('config_dir', 'config')
        return os.path.join(config_dir, filename)
    
    @staticmethod
    def _match_id(id1, id2) -> bool:
        """
        比较两个ID是否相等（支持字符串和整数类型）
        
        Args:
            id1: 第一个ID
            id2: 第二个ID
        
        Returns:
            bool: 是否相等
        """
        if id1 == id2:
            return True
        if str(id1) == str(id2):
            return True
        return False
    
    @staticmethod
    def _load_data(filename: str, env: dict = None) -> dict:
        """
        加载数据文件
        
        Args:
            filename: 数据文件名
            env: 环境信息字典（由IAOSScriptManager传递）
        
        Returns:
            dict: 数据内容
        """
        if env is None:
            env = {}
        file_path = KnowledgeManagerRegistry._get_data_file_path(filename, env)
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}
    
    @staticmethod
    def _save_data(filename: str, data: dict, env: dict = None) -> bool:
        """
        保存数据文件
        
        Args:
            filename: 数据文件名
            data: 数据内容
            env: 环境信息字典（由IAOSScriptManager传递）
        
        Returns:
            bool: 是否保存成功
        """
        if env is None:
            env = {}
        file_path = KnowledgeManagerRegistry._get_data_file_path(filename, env)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    
    @staticmethod
    def _load_config(filename: str, env: dict = None) -> dict:
        """
        加载配置文件
        
        Args:
            filename: 配置文件名
            env: 环境信息字典（由IAOSScriptManager传递）
        
        Returns:
            dict: 配置内容
        """
        if env is None:
            env = {}
        file_path = KnowledgeManagerRegistry._get_config_file_path(filename, env)
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}
    
    # ==================== 方法实现 ====================
    @staticmethod
    def _list_projects(env: dict = None) -> list:
        """
        获取项目列表
        
        Args:
            env: 环境信息字典（由IAOSScriptManager传递）
        
        Returns:
            list: 项目列表
        """
        if env is None:
            env = {}
        data = KnowledgeManagerRegistry._load_data('knowledge_manager_data.json', env)
        projects = data.get('content', {}).get('projects', [])
        return [
            {
                'id': project.get('id'),
                'name': project.get('name'),
                'description': project.get('description', ''),
                'project_type': project.get('project_type', ''),
                'status': project.get('status', ''),
                'tags': project.get('tags', []),
                'resource_count': len(project.get('resources', [])),
                'created_time': project.get('created_time'),
                'modified_time': project.get('modified_time')
            }
            for project in projects
        ]
    
    @staticmethod
    def _get_project(project_id, env: dict = None) -> dict:
        """
        获取项目详情
        
        Args:
            project_id: 项目ID（支持字符串或整数）
            env: 环境信息字典（由IAOSScriptManager传递）
        
        Returns:
            dict: 项目详情
        """
        if env is None:
            env = {}
        data = KnowledgeManagerRegistry._load_data('knowledge_manager_data.json', env)
        projects = data.get('content', {}).get('projects', [])
        for project in projects:
            if KnowledgeManagerRegistry._match_id(project.get('id'), project_id):
                return {
                    'success': True,
                    'project': project
                }
        return {
            'success': False,
            'message': f'未找到项目: {project_id}'
        }
    
    @staticmethod
    def _get_project_by_name(project_name: str, env: dict = None) -> dict:
        """
        根据名称获取项目
        
        Args:
            project_name: 项目名称
            env: 环境信息字典（由IAOSScriptManager传递）
        
        Returns:
            dict: 项目详情
        """
        if env is None:
            env = {}
        data = KnowledgeManagerRegistry._load_data('knowledge_manager_data.json', env)
        projects = data.get('content', {}).get('projects', [])
        for project in projects:
            if project.get('name') == project_name:
                return {
                    'success': True,
                    'project': project
                }
        return {
            'success': False,
            'message': f'未找到项目: {project_name}'
        }
    
    @staticmethod
    def _list_resources(project_id=None, resource_type: str = None, env: dict = None) -> list:
        """
        获取资源列表
        
        Args:
            project_id: 项目ID，不传则返回所有资源（支持字符串或整数）
            resource_type: 资源类型筛选
            env: 环境信息字典（由IAOSScriptManager传递）
        
        Returns:
            list: 资源列表
        """
        if env is None:
            env = {}
        data = KnowledgeManagerRegistry._load_data('knowledge_manager_data.json', env)
        projects = data.get('content', {}).get('projects', [])
        
        all_resources = []
        for project in projects:
            if project_id and not KnowledgeManagerRegistry._match_id(project.get('id'), project_id):
                continue
            for resource in project.get('resources', []):
                resource_info = {
                    'id': resource.get('id'),
                    'name': resource.get('name'),
                    'path': resource.get('path'),
                    'type': resource.get('type'),
                    'category': resource.get('category'),
                    'size': resource.get('size'),
                    'project_id': project.get('id'),
                    'project_name': project.get('name')
                }
                if resource_type and resource.get('type') != resource_type:
                    continue
                all_resources.append(resource_info)
        
        return all_resources
    
    @staticmethod
    def _search_resources(keyword: str, env: dict = None) -> list:
        """
        搜索资源
        
        Args:
            keyword: 搜索关键词
            env: 环境信息字典（由IAOSScriptManager传递）
        
        Returns:
            list: 匹配的资源列表
        """
        if env is None:
            env = {}
        data = KnowledgeManagerRegistry._load_data('knowledge_manager_data.json', env)
        projects = data.get('content', {}).get('projects', [])
        
        results = []
        keyword_lower = keyword.lower()
        for project in projects:
            for resource in project.get('resources', []):
                if (keyword_lower in resource.get('name', '').lower() or
                    keyword_lower in resource.get('path', '').lower()):
                    results.append({
                        'id': resource.get('id'),
                        'name': resource.get('name'),
                        'path': resource.get('path'),
                        'type': resource.get('type'),
                        'category': resource.get('category'),
                        'project_id': project.get('id'),
                        'project_name': project.get('name')
                    })
        
        return results
    
    @staticmethod
    def _get_resource_types(env: dict = None) -> dict:
        """
        获取资源类型配置
        
        Args:
            env: 环境信息字典（由IAOSScriptManager传递）
        
        Returns:
            dict: 资源类型配置
        """
        if env is None:
            env = {}
        config = KnowledgeManagerRegistry._load_config('knowledge_manager_config.json', env)
        return config.get('appSpecific', {}).get('resourceTypes', {})
    
    @staticmethod
    def _get_project_types(env: dict = None) -> list:
        """
        获取项目类型列表
        
        Args:
            env: 环境信息字典（由IAOSScriptManager传递）
        
        Returns:
            list: 项目类型列表
        """
        if env is None:
            env = {}
        config = KnowledgeManagerRegistry._load_config('knowledge_manager_config.json', env)
        project_types = config.get('appSpecific', {}).get('projectTypes', {})
        return list(project_types.keys())
    
    @staticmethod
    def _create_project(name: str, description: str = '', project_type: str = '', tags: list = None, 
                        create_folder: bool = True, folder_path: str = '', env: dict = None) -> dict:
        """
        创建新项目
        
        Args:
            name: 项目名称
            description: 项目描述
            project_type: 项目类型
            tags: 项目标签
            create_folder: 是否创建项目文件夹，默认True
            folder_path: 指定的父文件夹路径，不指定则使用默认路径
            env: 环境信息字典（由IAOSScriptManager传递）
        
        Returns:
            dict: 创建结果
        """
        if env is None:
            env = {}
        data = KnowledgeManagerRegistry._load_data('knowledge_manager_data.json', env)
        projects = data.get('content', {}).get('projects', [])
        
        for project in projects:
            if project.get('name') == name:
                return {
                    'success': False,
                    'message': f'项目名称已存在: {name}'
                }
        
        # 生成递增的整数ID
        max_id = 0
        for project in projects:
            pid = project.get('id', 0)
            if isinstance(pid, int) and pid > max_id:
                max_id = pid
            elif isinstance(pid, str) and pid.isdigit():
                max_id = max(max_id, int(pid))
        new_id = max_id + 1
        
        # 创建项目文件夹
        project_folder_path = ''
        folder_created = False
        if create_folder:
            folder_created, project_folder_path = KnowledgeManagerRegistry._create_project_folder(name, folder_path)
        
        new_project = {
            'id': new_id,
            'name': name,
            'description': description,
            'project_type': project_type,
            'type': project_type,
            'status': '未开始',
            'tags': tags or [],
            'resources': [],
            'resource_groups': [],
            'create_folder': create_folder,
            'folder_path': project_folder_path,
            'created_time': time.time(),
            'modified_time': time.time()
        }
        
        if 'content' not in data:
            data['content'] = {}
        if 'projects' not in data['content']:
            data['content']['projects'] = []
        data['content']['projects'].append(new_project)
        
        KnowledgeManagerRegistry._save_data('knowledge_manager_data.json', data)
        
        message = f'项目创建成功: {name}'
        if create_folder:
            if folder_created:
                message += f'，文件夹: {project_folder_path}'
            else:
                message += '，但文件夹创建失败'
        
        return {
            'success': True,
            'project_id': new_project['id'],
            'folder_path': project_folder_path,
            'message': message
        }
    
    @staticmethod
    def _create_project_folder(project_name: str, parent_path: str = '') -> tuple:
        """
        创建项目文件夹
        
        Args:
            project_name: 项目名称
            parent_path: 父文件夹路径，不指定则使用默认路径
        
        Returns:
            tuple: (是否成功, 文件夹路径)
        """
        try:
            # 获取默认项目路径
            if not parent_path:
                config = KnowledgeManagerRegistry._load_config('knowledge_manager_config.json')
                default_path_config = config.get('appSpecific', {}).get('defaultProjectPath', {})
                if isinstance(default_path_config, dict):
                    parent_path = default_path_config.get('value', '')
                else:
                    parent_path = default_path_config if isinstance(default_path_config, str) else ''
            
            # 如果没有配置默认路径，使用 Documents 目录
            if not parent_path:
                parent_path = os.path.expanduser('~/Documents')
            
            # 检查父目录是否存在
            if not os.path.exists(parent_path):
                try:
                    os.makedirs(parent_path, exist_ok=True)
                except Exception as e:
                    logging.error(f'创建父目录失败: {e}')
                    return False, ''
            
            # 清理项目名称，移除不合法的文件名字符
            safe_name = "".join(c for c in project_name if c.isalnum() or c in (' ', '-', '_', '（', '）', '(', ')')).strip()
            if not safe_name:
                safe_name = "新项目"
            
            # 创建项目文件夹路径
            project_folder_path = os.path.join(parent_path, safe_name)
            
            # 如果文件夹已存在，添加数字后缀
            counter = 1
            original_path = project_folder_path
            while os.path.exists(project_folder_path):
                project_folder_path = f"{original_path}_{counter}"
                counter += 1
            
            # 创建文件夹
            os.makedirs(project_folder_path, exist_ok=True)
            
            # 创建项目笔记文件
            try:
                notes_path = os.path.join(project_folder_path, f"{safe_name}_笔记.md")
                with open(notes_path, 'w', encoding='utf-8') as f:
                    f.write(f"# {project_name} 笔记\n\n")
            except:
                pass
            
            # 规范化路径
            normalized_path = os.path.normpath(project_folder_path)
            return True, normalized_path
            
        except Exception as e:
            logging.error(f'创建项目文件夹失败: {e}')
            return False, ''
    
    @staticmethod
    def _update_project(project_id, env: dict = None, **kwargs) -> dict:
        """
        更新项目信息
        
        Args:
            project_id: 项目ID（支持字符串或整数）
            env: 环境信息字典（由IAOSScriptManager传递）
            **kwargs: 要更新的字段
        
        Returns:
            dict: 更新结果
        """
        if env is None:
            env = {}
        data = KnowledgeManagerRegistry._load_data('knowledge_manager_data.json', env)
        projects = data.get('content', {}).get('projects', [])
        
        for project in projects:
            if KnowledgeManagerRegistry._match_id(project.get('id'), project_id):
                if 'name' in kwargs:
                    project['name'] = kwargs['name']
                if 'description' in kwargs:
                    project['description'] = kwargs['description']
                if 'project_type' in kwargs:
                    project['project_type'] = kwargs['project_type']
                if 'tags' in kwargs:
                    project['tags'] = kwargs['tags']
                if 'status' in kwargs:
                    project['status'] = kwargs['status']
                project['modified_time'] = time.time()
                
                KnowledgeManagerRegistry._save_data('knowledge_manager_data.json', data)
                
                return {
                    'success': True,
                    'message': f'项目更新成功: {project_id}'
                }
        
        return {
            'success': False,
            'message': f'未找到项目: {project_id}'
        }
    
    @staticmethod
    def _delete_project(project_id, env: dict = None) -> dict:
        """
        删除项目
        
        Args:
            project_id: 项目ID（支持字符串或整数）
            env: 环境信息字典（由IAOSScriptManager传递）
        
        Returns:
            dict: 删除结果
        """
        if env is None:
            env = {}
        data = KnowledgeManagerRegistry._load_data('knowledge_manager_data.json', env)
        projects = data.get('content', {}).get('projects', [])
        
        for i, project in enumerate(projects):
            if KnowledgeManagerRegistry._match_id(project.get('id'), project_id):
                deleted_name = project.get('name')
                del projects[i]
                KnowledgeManagerRegistry._save_data('knowledge_manager_data.json', data)
                return {
                    'success': True,
                    'message': f'项目已删除: {deleted_name}'
                }
        
        return {
            'success': False,
            'message': f'未找到项目: {project_id}'
        }
    
    @staticmethod
    def _add_resource(project_id, name: str, path: str, resource_type: str = '', category: str = '参考资料', env: dict = None) -> dict:
        """
        添加资源到项目
        
        Args:
            project_id: 项目ID（支持字符串或整数）
            name: 资源名称
            path: 资源路径
            resource_type: 资源类型
            category: 资源分类
            env: 环境信息字典（由IAOSScriptManager传递）
        
        Returns:
            dict: 添加结果
        """
        if env is None:
            env = {}
        data = KnowledgeManagerRegistry._load_data('knowledge_manager_data.json', env)
        projects = data.get('content', {}).get('projects', [])
        
        for project in projects:
            if KnowledgeManagerRegistry._match_id(project.get('id'), project_id):
                new_resource = {
                    'id': str(uuid.uuid4()),
                    'name': name,
                    'path': path,
                    'type': resource_type,
                    'category': category,
                    'added_time': time.time()
                }
                
                if os.path.exists(path):
                    new_resource['size'] = os.path.getsize(path)
                    new_resource['modified_time'] = os.path.getmtime(path)
                
                project.setdefault('resources', []).append(new_resource)
                project['modified_time'] = time.time()
                
                KnowledgeManagerRegistry._save_data('knowledge_manager_data.json', data)
                
                return {
                    'success': True,
                    'resource_id': new_resource['id'],
                    'message': f'资源添加成功: {name}'
                }
        
        return {
            'success': False,
            'message': f'未找到项目: {project_id}'
        }
    
    @staticmethod
    def _remove_resource(project_id, resource_path: str, env: dict = None) -> dict:
        """
        从项目中移除资源
        
        Args:
            project_id: 项目ID（支持字符串或整数）
            resource_path: 资源路径
            env: 环境信息字典（由IAOSScriptManager传递）
        
        Returns:
            dict: 移除结果
        """
        if env is None:
            env = {}
        data = KnowledgeManagerRegistry._load_data('knowledge_manager_data.json', env)
        projects = data.get('content', {}).get('projects', [])
        
        for project in projects:
            if KnowledgeManagerRegistry._match_id(project.get('id'), project_id):
                resources = project.get('resources', [])
                for i, resource in enumerate(resources):
                    if resource.get('path') == resource_path:
                        del resources[i]
                        project['modified_time'] = time.time()
                        KnowledgeManagerRegistry._save_data('knowledge_manager_data.json', data)
                        return {
                            'success': True,
                            'message': f'资源已移除: {resource_path}'
                        }
                return {
                    'success': False,
                    'message': f'未找到资源: {resource_path}'
                }
        
        return {
            'success': False,
            'message': f'未找到项目: {project_id}'
        }
    
    @staticmethod
    def _get_project_notes(project_id, env: dict = None) -> dict:
        """
        获取项目笔记
        
        Args:
            project_id: 项目ID（支持字符串或整数）
            env: 环境信息字典（由IAOSScriptManager传递）
        
        Returns:
            dict: 项目笔记内容
        """
        if env is None:
            env = {}
        data = KnowledgeManagerRegistry._load_data('knowledge_manager_data.json', env)
        projects = data.get('content', {}).get('projects', [])
        
        for project in projects:
            if KnowledgeManagerRegistry._match_id(project.get('id'), project_id):
                notes_file = os.path.join(
                    os.path.dirname(KnowledgeManagerRegistry._get_data_file_path('')),
                    'project_notes',
                    f'{project_id}.md'
                )
                if os.path.exists(notes_file):
                    with open(notes_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                    return {
                        'success': True,
                        'content': content
                    }
                return {
                    'success': True,
                    'content': ''
                }
        
        return {
            'success': False,
            'message': f'未找到项目: {project_id}'
        }
    
    @staticmethod
    def _save_project_note(project_id, content: str, env: dict = None) -> dict:
        """
        保存项目笔记
        
        Args:
            project_id: 项目ID（支持字符串或整数）
            content: 笔记内容
            env: 环境信息字典（由IAOSScriptManager传递）
        
        Returns:
            dict: 保存结果
        """
        if env is None:
            env = {}
        data = KnowledgeManagerRegistry._load_data('knowledge_manager_data.json', env)
        projects = data.get('content', {}).get('projects', [])
        
        for project in projects:
            if KnowledgeManagerRegistry._match_id(project.get('id'), project_id):
                notes_dir = os.path.join(
                    os.path.dirname(KnowledgeManagerRegistry._get_data_file_path('')),
                    'project_notes'
                )
                os.makedirs(notes_dir, exist_ok=True)
                notes_file = os.path.join(notes_dir, f'{project_id}.md')
                
                with open(notes_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                return {
                    'success': True,
                    'message': '笔记保存成功'
                }
        
        return {
            'success': False,
            'message': f'未找到项目: {project_id}'
        }
    
    @staticmethod
    def _launch() -> dict:
        """
        启动应用
        
        Returns:
            dict: 启动结果
        """
        return {
            'success': True,
            'message': '请通过桌面方式启动应用',
            'launch_command': 'python knowledge_manager_tool.py'
        }
    
    # ==================== 入口函数 ====================
    @staticmethod
    def run_script(params: dict) -> dict:
        """
        脚本管理器标准入口函数
        
        Args:
            params: 请求参数，包含：
                - method: 方法名或别名
                - data: 方法参数对象
                - _env: 环境信息对象（由IAOSScriptManager传递）
        
        Returns:
            dict: 标准返回格式
        """
        # 接收环境信息
        env = params.get('_env', {})
        
        method = params.get('method', '')
        data = params.get('data', {})
        
        # 处理方法别名
        if method in KnowledgeManagerRegistry.METHOD_ALIASES:
            method = KnowledgeManagerRegistry.METHOD_ALIASES[method]
        
        # 方法路由映射
        method_map = {
            'list_projects': KnowledgeManagerRegistry._list_projects,
            'get_project': KnowledgeManagerRegistry._get_project,
            'get_project_by_name': KnowledgeManagerRegistry._get_project_by_name,
            'list_resources': KnowledgeManagerRegistry._list_resources,
            'search_resources': KnowledgeManagerRegistry._search_resources,
            'get_resource_types': KnowledgeManagerRegistry._get_resource_types,
            'get_project_types': KnowledgeManagerRegistry._get_project_types,
            'create_project': KnowledgeManagerRegistry._create_project,
            'update_project': KnowledgeManagerRegistry._update_project,
            'delete_project': KnowledgeManagerRegistry._delete_project,
            'add_resource': KnowledgeManagerRegistry._add_resource,
            'remove_resource': KnowledgeManagerRegistry._remove_resource,
            'get_project_notes': KnowledgeManagerRegistry._get_project_notes,
            'save_project_note': KnowledgeManagerRegistry._save_project_note,
            'launch': KnowledgeManagerRegistry._launch,
        }
        
        try:
            if method not in method_map:
                return {
                    'success': False,
                    'code': 404,
                    'message': f'方法未找到: {method}',
                    'data': None
                }
            
            # 将环境信息传递给方法
            result = method_map[method](env=env, **data)
            
            return {
                'success': True,
                'code': 200,
                'message': '执行成功',
                'data': result
            }
        except TypeError as e:
            return {
                'success': False,
                'code': 400,
                'message': f'参数错误: {str(e)}',
                'data': None
            }
        except Exception as e:
            return {
                'success': False,
                'code': 500,
                'message': str(e),
                'data': None
            }


if __name__ == '__main__':
    # 设置Qt属性，支持WebEngine组件
    QApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
    
    app = QApplication(sys.argv)
    
    # 设置应用程序字体
    font = QFont("Microsoft YaHei UI", 9)
    app.setFont(font)
    
    tool = KnowledgeManagerTool()
    tool.show()
    sys.exit(app.exec_())