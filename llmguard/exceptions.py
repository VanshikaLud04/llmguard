class LLMGuardException(Exception): pass
class BudgetExceededException(LLMGuardException): pass
class DailyBudgetExceededException(LLMGuardException): pass
class UnknownModelException(LLMGuardException): pass
class AllModelsExhaustedException(LLMGuardException): pass