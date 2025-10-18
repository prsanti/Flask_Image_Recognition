"""
Tests for image preprocessing and prediction functions in model.py using the real Keras model.
"""
import io
import importlib
from typing import Any

import numpy as np
import pytest
from PIL import Image

# Skip this module entirely if Keras isn't available.
keras = pytest.importorskip("keras", reason="Keras not installed; skipping real-model tests")  # pylint: disable=unused-variable


@pytest.fixture(scope="module")
def real_model_module() -> Any:
    """
    Import the real model module or skip if not present.
    """
    try:
        module = importlib.import_module("model")
        return module
    except ImportError as err:  # narrow exception (fixes W0718)
        pytest.skip(f"Could not import real model module: {err}")  # consistent return path (R1710)


def test_preprocess_img_shapes_and_range(real_model_module):
    """
    Test that preprocess_img returns correct shape and value range.
    """
    buf = io.BytesIO()
    Image.new("RGB", (300, 100), color=(128, 64, 32)).save(buf, format="JPEG")
    buf.seek(0)

    arr = real_model_module.preprocess_img(buf)
    assert arr.shape == (1, 224, 224, 3)
    # allow any float dtype
    assert arr.dtype.kind == "f"
    assert np.min(arr) >= 0.0 and np.max(arr) <= 1.0


def test_predict_result_output_type(real_model_module):
    """
    Test that predict_result returns an integer class index.
    """
    buf = io.BytesIO()
    Image.new("RGB", (300, 100), color=(128, 64, 32)).save(buf, format="JPEG")
    buf.seek(0)

    arr = real_model_module.preprocess_img(buf)
    pred = real_model_module.predict_result(arr)
    assert isinstance(pred, (int, np.integer)), "Prediction should be an integer class index"
