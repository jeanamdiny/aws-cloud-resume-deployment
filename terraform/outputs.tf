output "api_endpoint" {
  description = "API Gateway endpoint URL for the visitor counter"
  value       = "${aws_apigatewayv2_stage.prod.invoke_url}/counter"
}

output "dynamodb_table_name" {
  value = aws_dynamodb_table.visitor_counter.name
}

output "lambda_function_name" {
  value = aws_lambda_function.visitor_counter.function_name
}