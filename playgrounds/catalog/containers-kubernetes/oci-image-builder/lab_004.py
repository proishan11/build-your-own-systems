"""Learner implementation stub for OCI Image Builder: Failure and Recovery.

Read exercises/004-failure-recovery.md before coding. The tests in
tests/test_lab_004.py define the project-specific behavior for `recover_oci_image_builder_non_reproducible_layer`.
"""

def recover_oci_image_builder_non_reproducible_layer(failure_report: dict) -> dict:
    """Classify recovery behavior for non-reproducible layer while protecting image manifest."""
    # TODO: Retry transient timeout/unavailable failures while budget remains,
    # fail permanent domain failures, and give up when the retry budget is exhausted.
    raise NotImplementedError
