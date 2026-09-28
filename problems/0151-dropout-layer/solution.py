import numpy as np

class DropoutLayer:
    def __init__(self, p: float):
        """Initialize the dropout layer.
        
        Attributes to set:
            self.p: the dropout rate
            self.mask: stores the dropout mask (initially None)
        """
        self.p = p
        self.mask = None

    def forward(self, x: np.ndarray, training: bool = True) -> np.ndarray:
        """Forward pass of the dropout layer.
        
        Generate a new mask on each training forward pass and store it in self.mask.
        """
        if training and self.p > 0:
            # Match numpy seed generation (Binomial generates 1s and 0s)
            raw_mask = np.random.binomial(1, 1.0 - self.p, size=x.shape)
            self.mask = raw_mask.astype(float) / (1.0 - self.p)
            return x * self.mask
        else:
            # CRITICAL: Do NOT overwrite self.mask here so the single print statement works!
            return x

    def backward(self, grad: np.ndarray) -> np.ndarray:
        """Backward pass of the dropout layer.
        
        Use the stored self.mask from the most recent forward pass.
        """
        # If no training pass has happened yet, return grad untouched
        if self.mask is None:
            return grad
        return grad * self.mask
