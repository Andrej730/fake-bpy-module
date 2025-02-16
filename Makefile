SOURCE_DIR=/l/Projects/Github/blender-git-main/blender
# blender.exe folder.
BLENDER_DIR="/l/Projects/Github/blender-git-main/build_windows_x64_vc17_Release/bin/Release"
GIT_REF=main
TARGET_VERSION=latest
# Output stubs folder.
BUILD_FOLDER=../build/build_files
TARGET=blender
PACKAGES_PATH=./tools/pip_package/raw_modules/
FAKE_BPY_MODULE_PATH=./src/

.PHONY: pretest test build package

# Will generate package files in BUILD_FOLDER.
build:
	cd src && bash gen_module.sh $(SOURCE_DIR) $(BLENDER_DIR) $(TARGET) $(GIT_REF) $(TARGET_VERSION) $(BUILD_FOLDER)

# Will run pre-tests.
pretest:
	bash tests/run_pre_tests.sh $(FAKE_BPY_MODULE_PATH)

# Ensure to build pip package before running the tests.
test:
	bash tests/run_tests.sh $(PACKAGES_PATH)

# Will run gen_module.sh and will generate .zip file.
package:
	cd tools/pip_package && bash build_pip_package.sh $(TARGET) $(TARGET_VERSION) $(SOURCE_DIR) $(BLENDER_DIR)
