import * as React from "react"

import { cn } from "../../lib/utils"

const Progress = React.forwardRef<
  HTMLDivElement,
  React.HTMLAttributes<HTMLDivElement> & {
    value: number
  }
>(({ className, value, ...props }, ref) => (
  <div
    className={cn(
      "relative h-2 w-full overflow-hidden rounded-full bg-secondary",
      className
    )}
    ref={ref}
    role="progressbar"
    aria-valuenow={value}
    {...props}
  >
    <div
      className="h-full bg-primary transition-all"
      style={{ width: `${value}%` }}
    />
  </div>
))
Progress.displayName = "Progress"

export { Progress }
