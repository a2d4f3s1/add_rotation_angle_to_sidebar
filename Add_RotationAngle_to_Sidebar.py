import bpy

# アドオン情報
bl_info = {
    "name": "View Rotation Angle to Sidebar",
    "author": "moteki",
    "version": (1, 0),
    "blender": (4, 2, 0),
    "location": "3D View > Sidebar > View",
    "description": "Adds the View Rotation Angle from Preferences to the View sidebar.",
    "warning": "",
    "doc_url": "",
    "category": "3D View",
}

# プリファレンスの回転角度をサイドパネルに追加するパネルクラス
class VIEW3D_PT_ViewPreferences(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'View'
    bl_label = "Preferences"

    def draw(self, context):
        layout = self.layout
        
        # プリファレンスからビューの回転角度のプロパティを取得
        preferences = context.preferences
        
        # UIに表示
        # row = layout.row()
        layout.prop(preferences.view, "rotation_angle", text="Rotation Angle")

# Blenderにクラスを登録
def register():
    bpy.utils.register_class(VIEW3D_PT_ViewPreferences)

# Blenderからクラスを登録解除
def unregister():
    bpy.utils.unregister_class(VIEW3D_PT_ViewPreferences)

# メイン実行
if __name__ == "__main__":
    register()