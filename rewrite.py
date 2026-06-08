import os
main = open('app/src/main/java/com/marc/camera/MainActivity.kt','w')
main.write('package com.marc.camera\n\nimport android.os.Bundle\nimport androidx.appcompat.app.AppCompatActivity\n\nclass MainActivity : AppCompatActivity() {\n    override fun onCreate(s: Bundle?) {\n        super.onCreate(s)\n        setContentView(R.layout.activity_main)\n    }\n}\n')
main.close()
print("Done!")
