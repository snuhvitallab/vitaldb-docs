# API Documentation

VitalDB provides a Python library and Web APIs for accessing vital files and the open dataset.

## Documents

| Document | Description |
|----------|-------------|
| [Python Library](Python_Library.md) | `vitaldb` Python package — read/write `.vital` files, access the open dataset |
| [Web API](Web_API.md) | REST API for VitalDB web platform |
| [Web API for Open Dataset](Web_API_OpenDataset.md) | Public API for accessing the open dataset |
| [IntraNet API](IntraNet_API.md) | Internal network VitalDB API |
| [OAuth2 API](OAuth2_API.md) | OAuth2 authentication for VitalDB services |

## Quick Start

```bash
pip install vitaldb
```

```python
import vitaldb

# List tracks in a vital file
tracks = vitaldb.vital_trks('case001.vital')

# Read waveform data
vals = vitaldb.vital_recs('case001.vital', track_names=['Solar8000/HR'], interval=1)
```

See [Python Library](Python_Library.md) for full API reference.
