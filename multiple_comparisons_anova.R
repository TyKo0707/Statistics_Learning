M = 0
D = 1

false_alarm <- function(m, n, a) {
  # Creating empty data frame with n observations (rows) and m samples (columns)
  d <- data.frame(matrix(0, n, m))
  # Creating matrix of the possible combinations of variables for the future t-test 
  s <- combn(1:m, 2)
  # Creating vector with length 1000 for subsequent recording 1000 test samples 
  x <- vector("numeric", 1000)
  
  # Creating our own simplified version of t-test that only return
  # p.value (makes the whole function much faster)
  t_test_pval <- function(x, y) {
    se <- sqrt((var(x) + var(y))/n)
    t_stat <- (mean(x) - mean(y))/se
    df <- n + n - 2
    pval <- 2*pt(abs(t_stat), df, lower.tail = F)
    pval
  }
  
  for (q in 1:1000) {
    d <- data.frame(apply(d, 2, function(i) rnorm(n)))
    # Filling empty data frame with random samples (extract from the general population)
    for (i in 1:ncol(s)) {
      TEST <- t_test_pval(d[, s[1, i]], d[, s[2, i]])
      if(TEST < a) x[q] <- 1
      if(TEST < a) break
    }
  }
  x <- as.data.frame(table(x))
  barplot(x$Freq, names.arg = c("No", "Yes"),
          col = c("Red", "Blue"),
          main = x$Freq[2]/1000*100,
          ylab = "Quantity",
          xlab = "Significant differences",
          ylim = c(0,1000))
}

false_alarm(2, 30, 0.05)
