#!/bin/bash
set -e

uv run -- fastapi run --port $PORT
